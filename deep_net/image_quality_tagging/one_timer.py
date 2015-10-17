import sys
import os
import requests
import json

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path = [os.path.join(SCRIPT_DIR + '/../')] + sys.path
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "analytics.settings")

from models import *
from common.models import Buy_Flat, Rent_Flat
from django.conf import settings

NUM_FLATS = 200


def get_active_flats(service):
    if service == 'buy':
        result = Buy_Flat.objects.using(
            'housing_production').filter(status_id=2)[0:NUM_FLATS]
    else:
        result = Rent_Flat.objects.using(
            'housing_production').filter(status=2)[0:NUM_FLATS]
    return result


def create_database():
    for service in ['rent', 'buy']:
        active_flats = get_active_flats(service)
        for flat in active_flats:
            objects = []
            flat_id = flat.id
            try:
                if service == 'buy':
                    flat_data_host = settings.BUY_API
                else:
                    flat_data_host = settings.RENT_API

                url = flat_data_host + str(flat_id)
                response = requests.get(url)
                result = json.loads(response.text)['result']
                images = result['images']
            except Exception as e:
                continue
            if images:
                for image in images:
                    flat_obj = FlatImages(
                        flat_id=flat_id, service=service, image_name=image[2], image_encoded=image[0])
                    objects.append(flat_obj)
                FlatImages.objects.bulk_create(objects)

if __name__ == "__main__":
    create_database()
