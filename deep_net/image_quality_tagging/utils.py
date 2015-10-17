from models import *
from random import randint
import time
import numpy as np
import keras
import os
from keras.models import model_from_json
from Crypto.Hash import MD5
from django.db.models import Min

from onetimeload import model

def encrypt(data):
    data = data + str(time.time())
    return MD5.new(data).hexdigest()


def get_flat_to_tag():
    result = {}
    tot_images = FlatImages.objects.using('housing_analytics').count()
    if tot_images >= 1:
        num_least_tags = int(
            FlatImages.objects.using('housing_analytics').aggregate(Min('num_user_tags'))['num_user_tags__min'])
        result_images = FlatImages.objects.using('housing_analytics').filter(num_user_tags=num_least_tags)
        random_id = randint(0, len(result_images) - 1)
        result = result_images[random_id].__dict__
        if not result:
            get_flat_to_tag()
    return result

# git clone https://github.com/fchollet/keras.git
# cd keras
# sudo pythons setup.py install

def get_prediction(abc):
    abc = np.array(abc)
    abc = abc.reshape((1, 2500))
    # dir_path = os.path.abspath(os.path.dirname(__file__))
    # model = model_from_json(open(dir_path + '/model.json').read())
    # model.load_weights(dir_path + '/model_weights.h5')

    if model.predict(abc)[:,1] > 0.5:
        return "Good"
    else:
        return "Bad"
