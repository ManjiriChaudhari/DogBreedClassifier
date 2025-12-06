#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Manjiri Chaudhari
# DATE CREATED: 02/12/2025
# REVISED DATE: 02/12/2025
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          also prints misclassified dogs and misclassified breeds of dogs
#          using the results dictionary (results_dic).  

def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user requests.
    
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
                    idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int) where 1 = match, 0 = no match
                    idx 3 = 1/0 (int) where 1 = pet image is a dog, 0 = not a dog
                    idx 4 = 1/0 (int) where 1 = classifier says dog, 0 = not a dog
      results_stats_dic - Dictionary with counts and percentages of results
      model - CNN model architecture used (resnet, alexnet, vgg)
      print_incorrect_dogs - True to print misclassified dogs (default False)
      print_incorrect_breed - True to print misclassified breeds (default False)
      
    Returns:
      None - prints the summary
    """

    # Print summary statistics
    print("\n\n*** Results Summary for CNN Model Architecture:", model.upper(), "***")
    print("{:25}: {:3d}".format('Number of Images', results_stats_dic['n_images']))
    print("{:25}: {:3d}".format('Number of Dog Images', results_stats_dic['n_dogs_img']))
    print("{:25}: {:3d}".format('Number of NON-Dog Images', results_stats_dic['n_notdogs_img']))
    
    print("\n% Correct Matches: {:.1f}%".format(results_stats_dic['pct_match']))
    print("% Correct Dogs: {:.1f}%".format(results_stats_dic['pct_correct_dogs']))
    print("% Correct Breed: {:.1f}%".format(results_stats_dic['pct_correct_breed']))
    print("% Correct NON-Dogs: {:.1f}%".format(results_stats_dic['pct_correct_notdogs']))
    
    # Print incorrectly classified dogs
    if print_incorrect_dogs:
        if (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs']
            != results_stats_dic['n_images']):
            print("\nINCORRECT Dog/NOT Dog Assignments:")
            for key, value in results_dic.items():
                if value[3] != value[4]:
                    print("Pet Image: {:>26}   Classifier Label: {:>30}".format(value[0], value[1]))
    
    # Print incorrectly classified breeds
    if print_incorrect_breed:
        if results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']:
            print("\nINCORRECT Dog Breed Assignment:")
            for key, value in results_dic.items():
                if value[3] == 1 and value[4] == 1 and value[2] == 0:
                    print("Pet Image: {:>26}   Classifier Label: {:>30}".format(value[0], value[1]))
