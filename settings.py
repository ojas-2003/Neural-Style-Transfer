import torch

DEVICE = torch.device('mps')
SIZE = 512
EPOCHS = 300
STYLE_PATH = './input/colors.jpeg'
STYLE_WEIGHT = 1000000
CONTENT_PATH = './input/bike.jpg'
CONTENT_WEIGHT = 1
OUTPUT_PATH = './output/bike_col.png'
