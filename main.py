import file_handler as fh
import grayscale_methods as grm
import os.path

original_images_path = './original_images'
grayscale_images_path = './grayscale_images'

if __name__ == '__main__':
    original_img_exist = os.path.isdir(original_images_path)
    gray_img_exist = os.path.isdir(grayscale_images_path)

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
    gray_images_created = grm.create_grayscale_images(original_images_path, grayscale_images_path)
    print(str(gray_images_created) + " gray image(s) have been created in folder " + str(grayscale_images_path) + ".\n")
