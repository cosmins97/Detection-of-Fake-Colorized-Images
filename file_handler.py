import cv2 as cv
import os


def read_image(path):
    """
    Read image from specified path.
    :param path: a path to a image
    :return: the image from path or None if the file is not supported
    """
    ret_img = cv.imread(cv.samples.findFile(path), cv.IMREAD_COLOR)
    return ret_img


def show_image(img):
    """
    Show the image img.
    :param img: a image
    :return: the image received is shown in a window
    """
    cv.imshow("Display window", img)
    cv.waitKey(0)


def save_image(img, save_path):
    """
    Save the image img to the path save_path.
    :param img: image to be saved
    :param save_path: path to where the image is saved
    :return: nothing
    """
    cv.imwrite(save_path, img)


def clear_folder(path):
    """
    Delete all files from folder at given path.
    :param path: the folder path
    :return: nothing
    """
    for f in os.listdir(path):
        os.remove(os.path.join(path, f))
