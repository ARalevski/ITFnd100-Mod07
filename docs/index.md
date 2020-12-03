# Pickling and Exception Handling in Python

Alexandra Ralevski

Nov. 29, 2020

Foundations of Python

Assignment 07

## Introduction
In Module07 I will be learning about pickling and error handling in Python, and the proper ways to use them.

## Pickling
Pickling allows a user to convert their data into a binary file (using 0’s and 1’s) on the computer. To begin, you must ‘import pickle’ at the beginning of the document, in order to use the built-in pickling functions that python provides. Then, you can read, write, or append to a document and convert the data to binary.

## Exception Handling
Exception handling allows you to ‘catch’ certain errors that a user may make and give them more ‘user friendly’ error messages rather than the built in ones that come with Python. You set up the code using a ‘try/except’ block that will catch any specific or non-specific errors (depending on how you write the code).

## Writing Code using Pickling and Error Handling
I wrote a script to create a list of users pet’s and their names using pickling and error handling. The code is shown below.

```
# ------------------------------------------------- #
# Title: Module07 Assignment
# Description: Code to capture a list of people's pets and their names
# ChangeLog: (Name, Date: MM-DD-YY)
# <ARalevski, 11-29-2020, Created Script>
# ------------------------------------------------- #

import pickle

# -- Data -- #

strFileName = 'PetNames.txt'
pet_lst = []
pet = ''
name = ''

# -- Processing -- #

class Processor:

    @staticmethod
    def read_data_from_file(file_name):
        objFile = open('/Users/aralevski/Documents/_PythonClass/Module07/Assignment07/PetNames.txt', 'rb')
        list_of_data = pickle.load(objFile)
        objFile.close()
        return list_of_data

    @staticmethod
    def save_data_to_file(file_name, list_of_data):
        objFile = open(file_name, 'ab')
        pickle.dump(list_of_data, objFile)
        objFile.close()

# -- Presentation (I/O) -- #

class IO:

    @staticmethod
    def input_new_pet():
        print('Please enter what pets you have and their names!' + '\n')
        try:
            pet = str(input('Enter a pet: ')).lower()
            name = str(input('Enter your pet\'s name: ')).lower()
            if pet.isnumeric():
                raise Exception('Do not use numbers for your pet!')
        except Exception as e:
            print(e)
        pet_lst = [pet, name]
        return pet_lst

# Main Body of Script  ------------------------------------------------------ #

pet, name = IO.input_new_pet() # get user input

Processor.save_data_to_file(strFileName, pet_lst) # store data to binary file using pickling

print(Processor.read_data_from_file(strFileName)) # read data from binary file
```

## Summary
In summary, I learned about pickling and error handling in Python, and have written a code that demonstrates the two. The code allows users to make a list of all their pets and their names, and stores it in a binary file. If a user makes an error while entering the data, the try/except block will catch it and present an error message.  
