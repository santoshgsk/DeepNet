import numpy as np
from keras.models import model_from_json

# git clone https://github.com/fchollet/keras.git
# cd keras
# sudo pythons setup.py install

def get_prediction():
	abc = np.ones(300)
	abc = abc.reshape((1, 300))
	model = model_from_json(open('model.json').read())
	model.load_weights('model_weights.h5')

	if model.predict(abc)[:,1] > 0.5:
		return "Good"
	else:
		return "Bad"
