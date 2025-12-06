#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# TODO 0: Add your information below for Programmer & Date Created.                                                                             
# PROGRAMMER: Manjiri Chaudhari
# DATE CREATED: 02/12/2025                                  
# REVISED DATE: 06/12/2025     
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
#          Note that the true identity of the pet (or object) in the image is 
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this 
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
from time import time, sleep

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results


# Main program function defined below
def main():
    # TODO 0: Measure start time
    start_time = time()

    # ---- FOR TESTING TIMING ONLY ----
    sleep(5)
    # ---------------------------------

    # TODO 1: Get command-line arguments
    in_arg = get_input_args()

    check_command_line_arguments(in_arg)

    # TODO 2: Create pet image labels dictionary
    results = get_pet_labels(in_arg.dir)

    check_creating_pet_image_labels(results)

    # TODO 3: Classify images and compare labels
    classify_images(in_arg.dir, results, in_arg.arch)

    check_classifying_images(results)

    # TODO 4: Adjust for dogs vs non-dogs
    adjust_results4_isadog(results, in_arg.dogfile)

    check_classifying_labels_as_dogs(results)

    # TODO 5: Compute statistics
    results_stats = calculates_results_stats(results)

    check_calculating_results(results, results_stats)

    # TODO 6: Print final results
    print_results(results, results_stats, in_arg.arch, True, True)

    # TODO 0: Measure end time
    end_time = time()

    # TODO 0: Compute total runtime (formatted)
    tot_time = end_time - start_time

    print("\nTotal Elapsed Runtime:",
          str(int(tot_time/3600)) + ":" +
          str(int((tot_time % 3600) / 60)) + ":" +
          str(int((tot_time % 3600) % 60)))


if __name__ == "__main__":
    main()

