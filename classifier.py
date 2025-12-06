import ast
from PIL import Image
import torchvision.transforms as transforms
import torchvision.models as models
import torch

# Load pretrained models
resnet18 = models.resnet18(pretrained=True)
alexnet = models.alexnet(pretrained=True)
vgg16 = models.vgg16(pretrained=True)

model_dict = {'resnet': resnet18, 'alexnet': alexnet, 'vgg': vgg16}

# Load ImageNet labels
with open('imagenet1000_clsid_to_human.txt') as f:
    imagenet_classes_dict = ast.literal_eval(f.read())

def classifier(img_path, model_name):
    # Load image
    img_pil = Image.open(img_path).convert('RGB')

    # Preprocess
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])
    img_tensor = preprocess(img_pil).unsqueeze(0)
    img_tensor.requires_grad_(False)

    # Select model and eval mode
    model = model_dict[model_name].eval()

    # Predict
    with torch.no_grad():
        output = model(img_tensor)

    # Get predicted index and return label
    pred_idx = output.cpu().numpy().argmax()
    return imagenet_classes_dict[pred_idx]
