# DogBreedClassifier
## Project Overview
This project implements a CNN-based image classifier to identify whether an image contains a dog, and if so, determine its breed. The project uses three pretrained CNN architectures: **VGG**, **AlexNet**, and **ResNet**.  

Objectives:  
1. Identify which pet images are of dogs and which are not.  
2. Classify the breeds of dogs for the images that are identified as dogs.

## Folder Structure
├── classifier.py # Contains the classifier function using pretrained CNNs
├── check_images.py # Main program to classify images
├── print_results.py # Function to print results and misclassifications
├── uploaded_images/ # Folder for your uploaded images to classify
├── pet_images/ # Folder containing training/test images
├── screenshots/ # Folder containing result screenshots
│ ├── vgg_results.png
│ ├── alexnet_results.png
│ └── resnet_results.png
├── run_models_batch_uploaded.sh # Script to run batch classification on uploaded images
└── README.md

bash
Copy code

## Installation
1. Make sure you have Python 3.10+ installed.
2. Create a virtual environment and activate it:
```bash
python -m venv venv
.\venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac
Install required packages:

bash
Copy code
pip install torch torchvision pillow
Running the Project
Place the images you want to classify inside the uploaded_images/ folder.

Run the batch classification script for all models:

bash
Copy code
sh run_models_batch_uploaded.sh
Alternatively, you can test a single image using:

bash
Copy code
python test_classifier.py
Sample Results
VGG Model

AlexNet Model

ResNet Model

Analysis
Based on classification of uploaded images:

Dog_01.jpg was correctly classified by all models as German Shepherd.

Dog_02.jpg predictions: VGG and ResNet correctly predicted German Shepherd, AlexNet misclassified it.

Non-dog images (Cat, Coffee mug) were mostly correctly classified; ResNet had the highest accuracy.

Best Model: ResNet – it consistently classified dog breeds correctly and identified non-dog images accurately.
