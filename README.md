
# Dog Breed Identification using a Pre-Trained Image Classifier

## Project Overview
This project focuses on utilizing a pre-trained image classifier to identify dog breeds. The goal is to enhance programming skills in Python while applying a convolutional neural network (CNN) to classify images as "dogs" or "not dogs."
## Project Description
As part of a citywide dog show, I developed a registration system that verifies submitted images of dogs. The system uses a provided classifier to ensure that only valid dog images are registered. The project involves evaluating different image classification algorithms to determine the most effective one for identifying dog breeds.
## Key Tasks
Image Classification: Implemented a Python-based solution to classify images as "dogs" or "not dogs" using a pre-trained CNN model.
Algorithm Evaluation: Compared the performance of three CNN architectures: AlexNet, VGG, and ResNet, to identify the best model for dog breed classification.
Performance Measurement: Measured the runtime and accuracy of each algorithm to understand the trade-offs between computational efficiency and classification accuracy.

## Technologies Used
Python, NumPy, Matplotlib
## Files Included
get_input_args.py: Retrieves 3 arguments provided by the user when they run the program from the command line. It essentially parses the user's input and returns a collection of these arguments as a variable named "in_arg".

get_pet_labels.py: Take the directory path (from the get_input_args function) as input for processing. The function builds a "results dictionary" based on this processing and returns this dictionary as a variable named "results".

classifier.py: Contains the classifier function for image classification.

adjust_results4_isadog.py: Modifies the "results_dic" dictionary to determine if the image classification model correctly identified images as containing "a dog" or "not a dog". 

calculates_results_stats.py: takes the "results_dic" (from "get_pet_labels.py") as input.

print_results.py: Prints out various summaries of the results.

## Results
The project successfully classified images, providing insights into the accuracy of each CNN architecture. The results highlighted the effectiveness of the chosen model in distinguishing between similar-looking dog breeds.
![App Screenshot](https://i.ibb.co/SVmfdk0/376.png" alt="376" )


