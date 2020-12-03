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

