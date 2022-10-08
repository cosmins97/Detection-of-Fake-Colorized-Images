import PIL
import torch
from matplotlib import pyplot as plt
from torchvision import transforms

from models import MainModel
from utils import lab_to_rgb

from fastai.vision.learner import create_body
from torchvision.models.resnet import resnet18
from fastai.vision.models.unet import DynamicUnet

import gdown


def build_res_unet(n_input=1, n_output=2, size=256):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    body = create_body(resnet18, pretrained=True, n_in=n_input, cut=-2)
    net_G = DynamicUnet(body, n_output, (size, size)).to(device)
    return net_G


if __name__ == '__main__':
    # You first need to download the final_model_weights.pt file from my drive
    # using the command: gdown --id 1lR6DcS4m5InSbZ5y59zkH2mHt_4RQ2KV
    # output = "final_model_weights.pt"
    # id = "1lR6DcS4m5InSbZ5y59zkH2mHt_4RQ2KV"
    # gdown.download(id=id, output=output, quiet=False)

    # model = MainModel()
    # device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    # model.load_state_dict(
    #     torch.load(
    #         "final_model_weights.pt",
    #         map_location=torch.device('cpu')
    #     ),
    #     strict=False
    # )
    # path = "../grayscale_images/C.jpg"
    # img = PIL.Image.open(path)
    # img = img.resize((256, 256))
    # # to make it between -1 and 1
    # img = transforms.ToTensor()(img)[:1] * 2. - 1.
    # model.eval()
    # with torch.no_grad():
    #     preds = model.net_G(img.unsqueeze(0).to(device))
    # colorized = lab_to_rgb(img.unsqueeze(0), preds.cpu())[0]
    # plt.imshow(colorized)
    # plt.show()

    net_G = build_res_unet(n_input=1, n_output=2, size=256)
    net_G.load_state_dict(torch.load("resnet18.pth", map_location=torch.device('cpu')),strict=False)
    model = MainModel(net_G=net_G)
    model.load_state_dict(torch.load("final_model_weights.pt", map_location=torch.device('cpu')),
                          strict=False)

    path = "../grayscale_images/cursuri-2.jpg"
    img = PIL.Image.open(path)
    img = img.resize((256, 256))
    # to make it between -1 and 1
    img = transforms.ToTensor()(img)[:1] * 2. - 1.
    model.eval()
    with torch.no_grad():
        preds = model.net_G(img.unsqueeze(0).to(torch.device('cpu')))
    colorized = lab_to_rgb(img.unsqueeze(0), preds.cpu())[0]
    plt.imshow(colorized)
    plt.show()
