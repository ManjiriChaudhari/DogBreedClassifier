# DogBreedClassifier
## Project Overview
This project implements a CNN-based image classifier to identify whether an image contains a dog, and if so, determine its breed. The project uses three pretrained CNN architectures: **VGG**, **AlexNet**, and **ResNet**.  

Objectives:  
1. Identify which pet images are of dogs and which are not.  
2. Classify the breeds of dogs for the images that are identified as dogs.

# Folder Structure
DogBreedClassifier/
│
├── classifier.py                       # CNN classifier function
├── check_images.py                     # Main script to classify images
├── print_results.py                    # Prints summary of classification results
├── print_functions_for_lab_checks.py   # Helper functions for testing/lab
├── get_input_args.py                   # Parses command-line arguments
├── get_pet_labels.py                   # Extracts labels from image filenames
├── pet_images/                         # Default 40 pet images for testing
├── uploaded_images/                    # Folder for user-uploaded test images
│     ├── dog_1.jpg
│     ├── dog_2.jpg
│     ├── cat_animal_01.jpg
│     └── coffee_mug_01.jpg
├── results_screenshots/                # Screenshots of classification results
│     ├── vgg_results.png
│     ├── alexnet_results.png
│     └── resnet_results.png
├── imagenet1000_clsid_to_human.txt     # Mapping of ImageNet class IDs to human-readable labels
├── README.md                           # This file

## Installation
1. Make sure you have Python 3.10+ installed.

2. Create a virtual environment and activate it:
python -m venv venv
.\venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac

3. Install required packages:
pip install torch torchvision pillow

4. Run the command -
# Run test classifier
python test_classifier.py
# Run check_images.py on uploaded images
python check_images.py --dir uploaded_images/ --arch vgg

# Sample Results
VGG Model
AlexNet Model
ResNet Model

# Analysis
Based on classification of uploaded images:
Dog_01.jpg was correctly classified by all models as German Shepherd.
Dog_02.jpg predictions: VGG and ResNet correctly predicted German Shepherd, AlexNet misclassified it.
Non-dog images (Cat, Coffee mug) were mostly correctly classified; ResNet had the highest accuracy.
Best Model: ResNet – it consistently classified dog breeds correctly and identified non-dog images accurately.
