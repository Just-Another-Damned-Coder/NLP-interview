# -*- coding:utf-8 -*-


# Import all your necessary libraries here.
import pandas as pd



def train(data: pd.DataFrame):
    # Take the data from the csv file 'data/classifier-data.csv'
    # Train a classifier on the data.
    # Save the classifier to a local file.
    
    # Write your code here.
    
    
    pass


def predict(text: str) -> str:
    # Read the classifier from the local file.
    # Predict the label for the input text.
    # Return the predicted label.

    pass


def main():
    # Read the csv file 'data/classifier-data.csv'
    data = pd.read_csv('data/classifier-data.csv', header=0, names=['text', 'label'])
    
    # Train and save the classifier.
    train(data)
    
    
    # Predict the label for the input text.
    text = "yup i think so"
    label = predict(text)
    print(label)



if __name__ == "__main__":
    main()
