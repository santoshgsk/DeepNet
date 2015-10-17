import os
from keras.models import model_from_json

dir_path = os.path.abspath(os.path.dirname(__file__))
model = model_from_json(open(dir_path + '/model.json').read())
model.load_weights(dir_path + '/model_weights.h5')
