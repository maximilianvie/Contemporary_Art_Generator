# Pipeline for preprocessing images

from PIL import ImageFile,Image
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

import torch
import torchvision.transforms as T
import glob

def preprocessing_of_images():
    destination_path = "dest_path/"
    pattern = "path/of_choice/*.jpg"

    # specify scale and ration parameters
    resize_cropper = T.RandomResizedCrop(size=512, scale=(1.0, 1.0), ratio=(1.0, 1.0))

    counter = 0;

    for img in glob.glob(pattern):

        ImageFile.LOAD_TRUNCATED_IMAGES = True
        print("transforming image" + str(counter))
        orig_img = Image.open(img)
        orig_img = orig_img.convert('RGB')
        resized_crops = resize_cropper(orig_img)

        # in case of different crops, add loop for saving several crops of the same image
        counter = counter + 1
        resized_crops.save(destination_path + "image_" + str(counter) + '.jpg')


if __name__ == '__main__':
    preprocessing_of_images()


