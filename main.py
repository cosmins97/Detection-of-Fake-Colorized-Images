import file_handler as fh
import grayscale_methods as grm
import coloring_methods as clm
import os.path

original_images_path = './original_images'
grayscale_images_path = './grayscale_images'
colorized_images_path = './colorized_images'

if __name__ == '__main__':
    original_img_exist = os.path.isdir(original_images_path)
    gray_img_exist = os.path.isdir(grayscale_images_path)
    color_img_exist = os.path.isdir(colorized_images_path)

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
    grm.create_grayscale_images(original_images_path, grayscale_images_path)

    # verify the color images folder
    if not color_img_exist:
        os.mkdir(colorized_images_path)
        print("Colorized Images Folder created.\n")
    else:
        fh.clear_folder(colorized_images_path)
        print("Colorized Images Folder cleared.\n")

    # create the color images from the grayscale ones
    clm.create_color_images(grayscale_images_path, colorized_images_path)
