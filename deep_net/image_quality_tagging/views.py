from django.shortcuts import render
from utils import *
import json
from models import *
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from PIL import Image
from forms import DocumentForm
from django.conf import settings


def get_options_populated(request):
    http_response = render(
        request, '../templates/image_quality_tagging/default_options.html')
    return http_response

def get_uploaded_image(request):
    http_response = render(
        request, '../templates/image_quality_tagging/image_upload.html')
    return http_response


def get_predicted_tag(request):

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            file_name = str(request.FILES['docfile'].name)
            file_name = file_name.replace(" ", "_")
            file_path = settings.MEDIA_ROOT + "/documents/" + file_name
            file_url = settings.MEDIA_URL + "/documents/" + file_name
            img_actual = Image.open(file_path)
            img_actual = img_actual.convert("L")
            img_actual = img_actual.resize((50, 50), Image.ANTIALIAS)
            predict_tag = get_prediction(list(img_actual.getdata()))
            # img_actual.save(file_path, quality=95)

            http_response = HttpResponse()
            response = {
                'image_path': file_path,
                'image_url': file_url
            }
            prediction_result = {
                'predicted': predict_tag
            }
            http_response = render(
                request, '../templates/image_quality_tagging/display_prediction.html',  {"image_data": response, "prediction_result": prediction_result})
            if not request.COOKIES.get('uid'):
                value = encrypt(
                    str(request.COOKIES.get('csrftoken')) + str(request.META.get('HTTP_USER_AGENT')))
                http_response.set_cookie(key='uid', value=value)
            return http_response
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        '../templates/image_quality_tagging/index.html',
        context_instance=RequestContext(request)
    )
    # image_encoded = request.POST.get('image_encoded')
    # image_name = request.POST.get('image_name')
    #
    # image_tag = get_prediction(image_encoded)
    #
    # http_response = HttpResponse()
    # response = {
    #     'image_tag': image_tag,
    #     'image_encoded': image_encoded,
    #     'image_name': image_name
    # }
    # http_response = render(
    #     request, '../templates/image_quality_tagging/index.html',  {"image_data": response})
    #
    # if not request.COOKIES.get('uid'):
    #     value = encrypt(
    #         str(request.COOKIES.get('csrftoken')) + str(request.META.get('HTTP_USER_AGENT')))
    #     http_response.set_cookie(key='uid', value=value)
    # return http_response
    #
    # return HttpResponseRedirect('./tag_images')

def get_flat_image(request):
    result = get_flat_to_tag()
    if not result:
        response = {
            'status': 'fail',
            'message': 'Database empty'
        }
        return HttpResponseNotFound(json.dumps(response))

    http_response = HttpResponse()
    response = {
        'flat_id': result['flat_id'],
        'service': result['service'],
        'image_encoded': result['image_encoded'],
        'image_name': result['image_name']
    }
    print "Image encoded ",
    print response['image_encoded']
    http_response = render(
        request, '../templates/image_quality_tagging/image-tagging.html',  {"image_data": response})
    if not request.COOKIES.get('uid'):
        value = encrypt(
            str(request.COOKIES.get('csrftoken')) + str(request.META.get('HTTP_USER_AGENT')))
        http_response.set_cookie(key='uid', value=value)
    return http_response


def get_user_tag(request):
    uid = request.COOKIES.get('uid')
    if not request.POST or not uid:
        return HttpResponseRedirect('./tag_images')

    flat_id = request.POST.get('flat_id')
    image_encoded = request.POST.get('image_encoded')
    img_wall_tag = request.POST.get('img_wall')
    img_cleanliness_tag = request.POST.get('img_cleanliness')
    img_spacious_tag = request.POST.get('img_spacious')
    img_flat_overall_tag = request.POST.get('img_flat_overall')
    img_windows_size_tag = request.POST.get('img_windows_size')

    user_tag_dict = {
        'uid': request.COOKIES.get('uid'),
        'image_encoded': image_encoded,
        'flat_id': flat_id,
        'img_wall': img_wall_tag,
        'img_cleanliness': img_cleanliness_tag,
        'img_spacious': img_spacious_tag,
        'img_flat_overall': img_flat_overall_tag,
        'img_windows_size': img_windows_size_tag,
    }

    image_obj = FlatImages.objects.using('housing_analytics').get(
        flat_id=flat_id, image_encoded=image_encoded)
    image_obj.num_user_tags += 1
    image_obj.save()

    try:
        flat_obj = FlatImageTag.objects.using('housing_analytics').get(
            uid=uid, image_encoded=image_encoded)
        for key, value in user_tag_dict.iteritems():
            setattr(flat_obj, key, value)
        flat_obj.save()
    except FlatImageTag.DoesNotExist:
        obj = FlatImageTag(**user_tag_dict)
        obj.save()

    return HttpResponseRedirect('./tag_images')
