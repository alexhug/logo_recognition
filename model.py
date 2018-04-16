import sys
import argparse
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2
import urllib
import requests
from io import BytesIO


from keras.preprocessing import image
from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions

model = ResNet50(weights='imagenet')
target_size = (224, 224)


def predict(model, img, target_size, top_n=3):
  """Run model prediction on image
  Args:
    model: keras model
    img: PIL format image
    target_size: (w,h) tuple
    top_n: # of top predictions to return
  Returns:
    list of predicted labels and their probabilities
  """
  if tuple(img.shape[1::-1]) != target_size:
    img = cv2.resize(img, dsize=(224, 224))

  x = image.img_to_array(img)
  x = np.expand_dims(x, axis=0)
  x = preprocess_input(x)
  preds = model.predict(x)
  return decode_predictions(preds, top=top_n)[0]

def plot_preds(image, preds):
  """Displays image and the top-n predicted probabilities in a bar graph
  Args:
    image: PIL image
    preds: list of predicted labels and their probabilities
  """
  plt.imshow(image)
  plt.axis('off')

  plt.figure()
  order = list(reversed(range(len(preds))))
  bar_preds = [pr[2] for pr in preds]
  labels = (pr[1] for pr in preds)
  plt.barh(order, bar_preds, alpha=0.5)
  plt.yticks(order, labels)
  plt.xlabel('Probability')
  plt.xlim(0,1.01)
  plt.tight_layout()
  plt.show()

if __name__=="__main__":
  a = argparse.ArgumentParser()
  a.add_argument("-i", "--image", help="path to image")
  a.add_argument("--image_url", help="url to image")
  args = vars(a.parse_args())
  print(args)
  print(args["image"])

  if args["image"] is None and args["image_url"] is None:
    a.print_help()
    sys.exit(1)

  if args["image"] is not None:
    img = cv2.imread(args["image"])
    print(img)
    size = tuple(img.shape[1::-1])
    preds = predict(model, img, target_size)
    plot_preds(img, preds)

  if args["image_url"] is not None:
    response = urllib.request.urlopen(args["image_url"])
    img = np.asarray(bytearray(response.read()), dtype="uint8")
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    preds = predict(model, img, target_size)
    plot_preds(img, preds)