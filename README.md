# DogBreedClassifier
## Project Overview
This project implements a CNN-based image classifier to identify whether an image contains a dog, and if so, determine its breed. The project uses three pretrained CNN architectures: **VGG**, **AlexNet**, and **ResNet**.  

Objectives:  
1. Identify which pet images are of dogs and which are not.  
2. Classify the breeds of dogs for the images that are identified as dogs.

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

# Results

# VGG Model
==============================
Results for CNN model: VGG
==============================

Cat_animal_01.jpg         --> Predicted: Egyptian cat, cat
coffee_mug_01.jpg         --> Predicted: cup
dog_1.jpg                 --> Predicted: German shepherd, German shepherd dog, German police dog, alsatian
dog_2.jpg                 --> Predicted: German shepherd, German shepherd dog, German police dog, alsatian

# AlexNet Model 
==============================
Results for CNN model: ALEXNET
==============================

Cat_animal_01.jpg         --> Predicted: tabby, tabby cat, cat
coffee_mug_01.jpg         --> Predicted: eggnog
dog_1.jpg                 --> Predicted: German shepherd, German shepherd dog, German police dog, alsatian
dog_2.jpg                 --> Predicted: malinois

# ResNet Model 
==============================
Results for CNN model: RESNET
==============================

Cat_animal_01.jpg         --> Predicted: Egyptian cat, cat
coffee_mug_01.jpg         --> Predicted: coffee mug
dog_1.jpg                 --> Predicted: German shepherd, German shepherd dog, German police dog, alsatian
dog_2.jpg                 --> Predicted: German shepherd, German shepherd dog, German police dog, alsatian

All images classified with all models!

(Screenshots of Results are uploaded in Result_Screenshots Folder.)

# Analysis
Based on classification of uploaded images:
Dog_01.jpg was correctly classified by all models as German Shepherd.
Dog_02.jpg predictions: VGG and ResNet correctly predicted German Shepherd, AlexNet misclassified it.
Non-dog images (Cat, Coffee mug) were mostly correctly classified; ResNet had the highest accuracy.
Best Model: ResNet – it consistently classified dog breeds correctly and identified non-dog images accurately.
