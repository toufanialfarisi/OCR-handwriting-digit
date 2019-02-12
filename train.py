from sklearn.externals import joblib
from sklearn.svm import LinearSVC
from hog import HOG 
import dataset
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('-d', '--dataset', required=True, help='path to the dataset file')
ap.add_argument('-m', '--model', required=True, help='path to where the model bill be stored')
args = vars(ap.parse_args())

(digits, target)= dataset.load_digits(args['dataset'])
data = []

hog = HOG(orientations=18, pixelsPerCell=(10,10), cellsPerBlock=(1,1), transform=True)

for image in digits:
    image = dataset.deskew(image, 20)
    image = dataset.center_extent(image, (20,20))
    hist = hog.describe(image)
    data.append(hist)
print(np.shape(data))
# model = LinearSVC(random_state=42)
# model.fit(data, target)
# joblib.dump(model, args['model'])
print('done')

# usage
# python train.py -d data/digits.csv -m models/toufan_model.cpickle
# python clasify.py -i images/cellphone.png -m models/toufan_model.cpickle


    