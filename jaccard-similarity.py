# -*- coding:utf-8 -*-


# Import all your necessary libraries here.
import string


# Global variables can be defined here.

# Example texts
text1 = "Jaccard similarity is a metric used to measure how similar two sets are."
text2 = "Jaccard similarity is a way to compare the similarity between two sets."

def tokenize(text: str) -> set:
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation.replace("'", "")))
    return set(text.split())



def jaccard_similarity(text1: str, text2: str) -> float:
    # Jaccard similarity is a measure of how similar two sets are.
    # J(A,B)=|A∪B| / |A∩B| ; Where A and B are two sets.
    # Write your code here.
    
    
    # Score is the Jaccard similarity score between the two strings.
    return score


def main():
    score = jaccard_similarity(text1, text2)
    print(score)




if __name__ == "__main__":
    main()