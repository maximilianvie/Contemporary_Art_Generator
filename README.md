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

During training sample images will be saved into a subfolder of the folder "code".

The implementation was written by Aladdin Persson (https://github.com/aladdinpersson/Machine-Learning-Collection/tree/master/ML/Pytorch/GANs/ProGAN)
Slight changes were made to fit it to my usecase. More information regarding that in the assignment2.pdf. 

## Run the preprocessing pipeline:
Change the load and save directories accordingly, set custom crop parameters and run it. 
