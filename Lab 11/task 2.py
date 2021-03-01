from Modules2 import *        # Importing modules

password = None         # To enter while loop

while password != 'x':
      print('Enter x to exit the program.')

      password = input('Enter a password: ')

      if password == 'x':
            print('Program exited successfully.')
            break

      pass_strength = strength(password)  # To check the strength of password

      output(pass_strength, password)     # to print the output
