#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# test_classifier_batch.py
#
# PROGRAMMER: Manjiri Chaudhari
# DATE CREATED: 02/12/2025
# REVISED DATE: 06/12/2025
# PURPOSE: Test the classifier() function on multiple images using all three
#          pre-trained CNN models and print the classification results in a table.

import os
from classifier import classifier

# Folder containing images to test
image_folder = "uploaded_images"  # or "pet_images"
image_files = [f for f in os.listdir(image_folder) if f.endswith(".jpg")]

# CNN models to test
models = ["vgg", "alexnet", "resnet"]

# Iterate through all images and all models
for model in models:
    print("\n\n==============================")
    print(f"Results for CNN model: {model.upper()}")
    print("==============================\n")
    
    for img_file in image_files:
        img_path = os.path.join(image_folder, img_file)
        
        # Get predicted label
        predicted_label = classifier(img_path, model)
        
        # Print result in table format
        print(f"{img_file:25} --> Predicted: {predicted_label}")

print("\nAll images classified with all models!")
