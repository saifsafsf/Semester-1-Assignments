from os.path import isfile    # Importing modules
from Modules import *

option = None                 # Defining to enter while loop
file_name = None

while option != 'x':

      option = menu()         # For menu & to get option

      if option == 'r':
            file_name = input('Enter file name: ')

            if isfile(file_name):         # Checking if file exists
                  data = read(file_name)        # Storing the data in 'data'

                  # To show on top of menu in next loop
                  print(f'\n\t{file_name}')

            else:
                  print('The file doesn\'t exist. Try Again.')
                  continue

      elif option == 's':

            # Reading the file if not read before.
            if file_name == None:
                  file_name = input('Enter file name: ')

                  if isfile(file_name):
                        data = read(file_name)

                  else:
                        print('The file doesn\'t exist. Try Again.')
                        continue

            # For number of sentences & total words
            num_sentences, total_words = statistics(data)

            print(f'Number of sentences: {num_sentences}\nNumber of words: {total_words}')
            print(f'\n\t{file_name}')

      elif option == 'e':

            # Reading the file if not read before.
            if file_name == None:
                  file_name = input('Enter file name: ')

                  if isfile(file_name):
                        data = read(file_name)

                  else:
                        print('The file doesn\'t exist. Try Again.')
                        continue

            # Finding & writing the frequency in output
            words = search(data)

            # Writing the words in another file
            store(data, words)

            print(f'\n\t{file_name}')

      elif option == 'x':

            print('Program exited successfully.')
            break

      else:
            # In case of invalid input.
            print('Invalid Input... Try Again.')
