# -*- coding:utf-8 -*-


# Import all your necessary libraries here.



# Global variables can be defined here.

stop_words = ['a', 'and', 'in', 'is', 'it', 'of', 'on', 'to', 'the', 'that', 'by', 'with', 'has', 'were', 'from', 'but', 'as', 'also', 'their', 'its', 'into', 'within', 'made', 'no']


# Conditions :
# 1. The function should convert the input text to lowercase.
# 2. The function should remove all punctuation from the text except for apostrophes (').

def tokenize(text: str) -> list:
    # Write your code here.

    
    
    
    
    # 'tokens' is the result of tokenizing the input text.
    return tokens




def main():
    # Read the file 'data/tokenizer-data.txt' and tokenize its content.
    # Check the function arguments clearly and then call the function.
    
    # Read the file here ;
    
    
    # 'text' is the content of the file.
    tokens = tokenize(text)
    assert isinstance(tokens, list)
    print(tokens)
    
    # Now remove the stop words from the tokens, then print the unique tokens.

if __name__ == '__main__':
    main()

