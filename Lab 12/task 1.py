# Importing user-defined functions
from Modules1 import *

#To enter while loop
math_exp = None

while math_exp != 'Exit':

      # Menu
      print('''
History - To view history of inputs given.
Clear - To clear input history.
Exit - To exit the program.
OR
Any Valid Mathematical Expression.
''')

      # User's selected option
      math_exp = input('Enter your selection: ')

      if math_exp.lower() == 'exit':
            print('\nProgram exited successfully.')
            break

      elif math_exp.lower() == 'history':

            # To display calculator's history
            history()

      elif math_exp.lower() == 'clear':

            # To clear the history
            clear()

      else:

            # For output & error handling
            errors(math_exp)
                  
                  
                  
