# Poker Automation Bot README

## Overview

Welcome to the Poker Automation Bot project! This Python-based application leverages various libraries and a neural network to automate poker gameplay. Follow the instructions below to set up and run the code successfully.

## Installation

Before running the code, make sure to install the required Python libraries. You can install them using the following command:

```bash
pip install numpy pandas matplotlib opencv-python binarytree tensorflow
```

## Data Preparation

1. Store the "cards" folder and the "poker hands" folder in your preferred path.
2. Update the file paths in the code to reflect the location of the stored folders.

## Neural Network Training

1. Run the neural network with the training data located in the "poker-zip" folder.
2. Test the neural network with the provided test data, and record the accuracy for future reference.

## GUI Instructions

Follow these steps in the GUI to simulate poker gameplay:

1. **Hand to Dealer:**
   - Click to give 3 cards to the dealer initially.

2. **Hand to Players:**
   - Click to distribute 2 cards to each of the 5 players.

3. **Hand to Dealer1:**
   - Click to add 1 additional card to the existing 3 cards for the dealer.

4. **Hand to Dealer2:**
   - Click to add 1 additional card to the existing 4 cards for the dealer.

5. **Current Status:**
   - Click to display the current status, including permutations of cards and the possible best hands for each player in the form of binary trees.

6. **Stop:**
   - Click to end the GUI and terminate the code.

## Note

Ensure you follow the specified order of clicking buttons for the desired output. Refer to the provided instructions for a seamless poker simulation experience.

Feel free to explore and modify the code to suit your preferences and requirements. Happy coding!
