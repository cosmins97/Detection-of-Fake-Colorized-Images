import cv2 as cv
import file_handler as fh
import os
import PIL
import torch
from matplotlib import pyplot as plt
from torchvision import transforms

from colorization.loss import *
from colorization.models import *
from colorization.utils import *
from colorization.dataset import *

from fastai.vision.learner import create_body
from torchvision.models.resnet import resnet18
from fastai.vision.models.unet import DynamicUnet


def build_res_unet(n_input=1, n_output=2, size=256):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    body = create_body(resnet18, pretrained=True, n_in=n_input, cut=-2)
    net_G = DynamicUnet(body, n_output, (size, size)).to(device)
    return net_G


def image_to_color(in_path, out_path, color_map):
    """
    Convert a grayscale image to a color image using a color map and saves the result to the specified path.
    :param in_path: Path of the grayscale image.
    :param out_path: Path of the color image.
    :param color_map: Color map used.
    :return: Nothing
    """

    # convert to color
    net_G = build_res_unet(n_input=1, n_output=2, size=256)
    net_G.load_state_dict(torch.load("colorization/resnet18.pth", map_location=torch.device('cpu')), strict=False)
    model = MainModel(net_G=net_G)
    model.load_state_dict(torch.load("colorization/final_model_weights.pt", map_location=torch.device('cpu')),
                          strict=False)

    path = in_path
    img = PIL.Image.open(path)
    img = img.resize((256, 256))
    # to make it between -1 and 1
    img = transforms.ToTensor()(img)[:1] * 2. - 1.
    model.eval()
    with torch.no_grad():
        preds = model.net_G(img.unsqueeze(0).to(torch.device('cpu')))
    colorized = lab_to_rgb(img.unsqueeze(0), preds.cpu())[0]

    plt.imsave(out_path, colorized)

    # fh.save_image(colorized, out_path)


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
