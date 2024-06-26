import tensorflow as tf
import numpy as np
from PIL import Image

imagePath = 'testImages/' + 'classDemo3.png'
modelPath = 'models/best_model.h5'

model = tf.keras.models.load_model(modelPath)

# Load the image
img = tf.keras.preprocessing.image.load_img(imagePath, target_size=(224, 224))

predictions = model.predict(np.expand_dims(img, axis=0))
predicted_classes = np.argmax(predictions, axis=1)

class_names = ["angry", "disgust", "fear", "happy", "neutral", "sad", "surprise"]
print("----------------------------------------")
print(class_names[predicted_classes.item()])
print("----------------------------------------")

image = Image.open(imagePath)
image.show()