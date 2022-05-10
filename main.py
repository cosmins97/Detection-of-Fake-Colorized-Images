import file_handler as fh
import grayscale_methods as grm
import coloring_methods as clm
import data_methods as dm
import os.path

original_images_path = './original_images'
grayscale_images_path = './grayscale_images'
colorized_images_path = './colorized_images'

# parameters and operations
image_limit = 10
create_grayscale = 0
create_colorized = 0
create_histograms = 0

train_model = 1
image_train_limit = 100

if __name__ == '__main__':
    original_img_exist = os.path.isdir(original_images_path)
    gray_img_exist = os.path.isdir(grayscale_images_path)
    color_img_exist = os.path.isdir(colorized_images_path)

    if create_grayscale:
        # verify the original images folder
        if not original_img_exist:
            print("Original Images Folder Path doesn't exist.\n")
            exit(0)

        # verify the grayscale images folder
        if not gray_img_exist:
            os.mkdir(grayscale_images_path)
            print("Grayscale Images Folder created.\n")
        else:
            fh.clear_folder(grayscale_images_path)
            print("Grayscale Images Folder cleared.\n")

        # create the grayscale images from the original ones
        grm.create_grayscale_images(original_images_path, grayscale_images_path, image_limit)

    if create_colorized:
        # verify the grayscale images folder
        if not gray_img_exist:
            print("Greayscale Images Folder Path doesn't exist.\n")
            exit(0)

        # verify the color images folder
        if not color_img_exist:
            os.mkdir(colorized_images_path)
            print("Colorized Images Folder created.\n")
        else:
            fh.clear_folder(colorized_images_path)
            print("Colorized Images Folder cleared.\n")

        # create the color images from the grayscale ones
        clm.create_color_images(grayscale_images_path, colorized_images_path, image_limit)

    if create_histograms:
        # verify the original images folder
        if not original_img_exist:
            print("Original Images Folder Path doesn't exist.\n")
            exit(0)

        # verify the colorized images folder
        if not color_img_exist:
            print("Colorized Images Folder Path doesn't exist.\n")
            exit(0)

        dm.get_histograms(colorized_images_path, image_limit)

    if train_model:
        # verify the original images folder
        if not original_img_exist:
            print("Original Images Folder Path doesn't exist.\n")
            exit(0)

        # verify the colorized images folder
        if not color_img_exist:
            print("Colorized Images Folder Path doesn't exist.\n")
            exit(0)

        dm.train_model(original_images_path, colorized_images_path, image_train_limit)
