import cv2 as cv
import file_handler as fh
import os


def image_to_color(in_path, out_path, color_map):
    """
    Convert a grayscale image to a color image using a color map and saves the result to the specified path.
    :param in_path: Path of the grayscale image.
    :param out_path: Path of the color image.
    :param color_map: Color map used.
    :return: Nothing
    """
    img = fh.read_image(in_path, cv.IMREAD_GRAYSCALE)

    # convert to color
    imgC = cv.applyColorMap(img, color_map)

    fh.save_image(imgC, out_path)


def create_color_images(in_path, out_path):
    """
    Take all images from the in path and create colorized versions of them at out path.
    :param in_path: Path to the grayscale images
    :param out_path: Path to the colorized images
    :return: Nothing.
    """
    counter = 0
    color_map = cv.COLORMAP_WINTER

    print("Converted to color:")

    for file in os.listdir(in_path):
        original_file_path = os.path.join(in_path, file)

        if os.path.isfile(original_file_path):
            gray_file_path = os.path.join(out_path, file)
            image_to_color(original_file_path, gray_file_path, color_map)
            counter += 1
            print(file)

    print("\n" + str(counter) + " color image(s) have been created in folder " + str(out_path) + ".\n")
