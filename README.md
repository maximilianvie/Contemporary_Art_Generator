# Contemporary_Art_Generator
Applied Deep Learning WS2022/23 project

# Exercise 1 
Information in the assignment 1 PDF

# Exercise 2
Please read the assignment2.pdf to get and overview of what was done for this exercise. 

## Run the model:
Simply run the train.py file in the code folder.
The model can be configured in the config.py file. (e.g. set Load_Model = True) 

If you want to train the model, images must be present in the test folder. I added some images of my collected dataset. 

To get an overview of the training, tensorboard can be activated. 
Just cd into the code folder in terminal and enter "tensorboard --logdir logs".

During training, sample images will be saved into a subfolder of the folder "code".

The implementation was written by Aladdin Persson (https://github.com/aladdinpersson/Machine-Learning-Collection/tree/master/ML/Pytorch/GANs/ProGAN)
Slight changes were made to fit it to my usecase. More information regarding that in the assignment2.pdf. 

## Run the preprocessing pipeline:
Change the load and save directories accordingly, set custom crop parameters and run it. 

## Pretrained Models
I added my pretrained models to the code folder. You can use them if you want to test training on the ProGAN. Therefore specify in the config file to load the model. It is recommended to start training at 128x128, since the models are trained until this format. The generator.pth and critic.pth files in the code folder represent the model, which I trained on the full dataset. (mentioned in assignment2.pdf) The files in the "abstract_dataset_model" folder represent the model which I trained only on the abstract art pieces. 
