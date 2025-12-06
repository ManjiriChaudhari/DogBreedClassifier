#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# print_results.py

# PROGRAMMER: Manjiri Chaudhari
# DATE CREATED: 02/12/2025
# REVISED DATE: 06/12/2025
# PURPOSE: Prints summary statistics of the results and optionally
#          prints misclassified dogs and dog breeds.

def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and optionally misclassified dogs
    and breeds.
    """
    print("\n\n*** Results Summary for CNN Model Architecture:", model.upper(), "***")
    print("{:25}: {:3d}".format('Number of Images', results_stats_dic['n_images']))
    print("{:25}: {:3d}".format('Number of Dog Images', results_stats_dic['n_dogs_img']))
    print("{:25}: {:3d}".format('Number of NON-Dog Images', results_stats_dic['n_notdogs_img']))
    
    # Print percentage statistics
    print("\n% Correct Matches: {:.1f}%".format(results_stats_dic['pct_match']))
    print("% Correct Dogs: {:.1f}%".format(results_stats_dic['pct_correct_dogs']))
    print("% Correct Breed: {:.1f}%".format(results_stats_dic['pct_correct_breed']))
    print("% Correct NON-Dogs: {:.1f}%".format(results_stats_dic['pct_correct_notdogs']))
    
    # Print incorrectly classified dogs
    if print_incorrect_dogs and (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'] != results_stats_dic['n_images']):
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        for key, value in results_dic.items():
            if value[3] != value[4]:  # misclassified dog/not-dog
                print("Pet Image: {:>26}   Classifier Label: {:>30}".format(value[0], value[1]))
    
    # Print incorrectly classified breeds
    if print_incorrect_breed and (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']):
        print("\nINCORRECT Dog Breed Assignment:")
        for key, value in results_dic.items():
            if value[3] == 1 and value[4] == 1 and value[2] == 0:  # breed mismatch
                print("Pet Image: {:>26}   Classifier Label: {:>30}".format(value[0], value[1]))