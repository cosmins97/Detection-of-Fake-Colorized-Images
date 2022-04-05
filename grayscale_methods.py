import cv2 as cv
import file_handler as fh
import os


def pixel_to_grayscale(pixel):
    """
    Turn the given pixel to grayscale.
    :param pixel: a pixel from a color image
    :return: the value of that pixel in greyscale
    """
    # color values
    r = float(pixel[2])
    g = float(pixel[1])
    b = float(pixel[0])

    # compute gray value
    gray = (r + g + b) / 3

    return gray


def image_to_grayscale(in_path, out_path):
    """
    Turn the image at path in_path to grayscale and save it at path out_path.
    :param in_path: the path to the original image
    :param out_path: the path to the grayscale image
    :return: a black/white image saved at the specified location
    """
    # read image
    img = fh.read_image(in_path, cv.IMREAD_COLOR)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    fh.save_image(gray, out_path)


def create_grayscale_images(in_path, out_path):
    """
    Take all images from the in path and create grayscale versions of them at out path.
    :param in_path: Path to the original images
    :param out_path: Path to the grayscale images
    :return: Nothing.
    """
    counter = 0

    print("Converted to greyscale:")

    for file in os.listdir(in_path):
        original_file_path = os.path.join(in_path, file)

        if os.path.isfile(original_file_path):
            gray_file_path = os.path.join(out_path, file)
            image_to_grayscale(original_file_path, gray_file_path)
            counter += 1
            print(file)

    print("\n" + str(counter) + " gray image(s) have been created in folder " + str(out_path) + ".\n")

