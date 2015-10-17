from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
                       url(r'^tag_images$',
                           views.get_flat_image, name='image_quality_tag'),
                       url(r'^record_result$',
                           views.get_user_tag, name='get_user_tag'),
                       url(r'^upload_image$',
                            views.get_uploaded_image, name='get_uploaded_image'),
                       url(r'^get_prediction$',
                            views.get_predicted_tag, name='get_predicted_tag'),
                       url(r'^list/$', 'list', name='list'),
                       )
