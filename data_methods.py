import cv2 as cv
from matplotlib import pyplot as plt

import file_handler as fh
import os

import numpy as np

from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

import pickle


def get_histogram_from_image(path):
    img = cv.imread(path)
    img2 = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h, s, v = img2[:, :, 0], img2[:, :, 1], img2[:, :, 2]
    hist_h = cv.calcHist([h], [0], None, [256], [0, 256])
    hist_s = cv.calcHist([s], [0], None, [256], [0, 256])
    hist_v = cv.calcHist([v], [0], None, [256], [0, 256])
    # plt.plot(hist_h, color='r', label="h")
    # plt.plot(hist_s, color='g', label="s")
    # plt.plot(hist_v, color='b', label="v")
    # plt.legend()
    # plt.show()

    hue_array = []
    sat_array = []
    brg_array = []
    hist_array = []

    for i in hist_h:
        hue_array.append(i[0])
    hist_array.append(hue_array)

    for i in hist_s:
        sat_array.append(i[0])
    hist_array.append(sat_array)

    for i in hist_v:
        brg_array.append(i[0])
    hist_array.append(brg_array)

    return hist_array


def get_histograms(folder_path, limit):
    counter = 0

    for file in os.listdir(folder_path):
        original_file_path = os.path.join(folder_path, file)

        h = get_histogram_from_image(original_file_path)

        # print(original_file_path)
        # print(h[0])
        # print(h[1])
        # print(h[2])

        counter += 1

        if counter == limit:
            break


def train_model(original_img_folder, colorized_img_folder, limit):
    # 0 for original, 1 for colorized
    dataset = []
    classes = []

    counter = 0

    for file in os.listdir(original_img_folder):
        file_path = os.path.join(original_img_folder, file)
        hist = get_histogram_from_image(file_path)
        hist_arr = np.array(hist)
        dataset.append(hist_arr.flatten())
        classes.append(0)

        counter += 1
        if counter > limit:
            break

    counter = 0

    for file in os.listdir(colorized_img_folder):
        file_path = os.path.join(colorized_img_folder, file)
        hist = get_histogram_from_image(file_path)
        hist_arr = np.array(hist)
        dataset.append(hist_arr.flatten())
        classes.append(1)

        counter += 1
        if counter > limit:
            break

    # print(classes)

    pca = PCA(n_components=15)

    result = pca.fit_transform(dataset)

    filename = 'pca.sav'
    pickle.dump(pca, open(filename, 'wb'))

    X_train, X_test, y_train, y_test = train_test_split(result, classes, test_size=0.25)

    rfc = RandomForestClassifier(n_jobs=1)
    print("rfc")
    rfc.fit(X_train, y_train)

    filename = 'trained_model.sav'
    pickle.dump(rfc, open(filename, 'wb'))

    y_pred = rfc.predict(X_test)

    accuracy_score(y_test, y_pred)

    print(classification_report(y_test, y_pred))
