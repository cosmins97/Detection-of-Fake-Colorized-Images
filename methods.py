import cv2 as cv


def read_image(path):
    """
    :param path: a path to a image
    :return: the image from path or None if the file is not supported
    """
    ret_img = cv.imread(cv.samples.findFile(path), cv.IMREAD_COLOR)
    return ret_img


def show_image(img):
    """
    :param img: a image
    :return: the image received is shown in a window
    """
    cv.imshow("Display window", img)
    cv.waitKey(0)


def save_image(img, save_path):
    """
    :param img: image to be saved
    :param save_path: path to where the image is saved
    :return: nothing
    """
    cv.imwrite(save_path, img)


def pixel_to_grayscale(pixel):
    """
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
    :param in_path: the path to the original image
    :param out_path: the path to the grayscale image
    :return: a black/white image saved at the specified location
    """
    # read image
    img = read_image(in_path)

    # get width and height
    height = img.shape[0]
    width = img.shape[1]

    # go through pixels
    for h in range(0, height):
        for w in range(0, width):
            # get a pixel
            pixel = img[h][w]
            # transform it in b/w using a method
            img[h][w] = pixel_to_grayscale(pixel)

    show_image(img)