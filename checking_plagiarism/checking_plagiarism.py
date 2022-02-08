# difflib module is nothing just a module in python which provides functions like comparing data btw files
# SequenceMatcher is a class in difflib which compare the sequence of characters or elements betwen files as long as they are hashable
from difflib import SequenceMatcher
# open function opens the files in reading mode
with open('file-1.txt') as file1, open('file-2.txt') as file2:
    file1_data = file1.read()    # Read file1.txt data and store in file1_data
    file2_data = file2.read()    # Read file2.txt data and store in file2_data
    # None, 1st file, 2nd file are passes as an argumnet in SequenceMatcher function and result stored in similarity
    # None is passed so that not a single element is ignored during comparison
    similarity = SequenceMatcher(None, file1_data, file2_data).ratio()
    # Now print the similarities in the form of %
    print(f"The contents are {similarity*100}% common.")