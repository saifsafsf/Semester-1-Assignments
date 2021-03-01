# To avoid program crash by Warnings
import warnings
warnings.simplefilter('ignore')

def history():
      '''Opens the file containing Calculator's History
            & displays it.'''
      
      print(f'\n\tHISTORY\n')

      try:
            file = open('Cal_History.txt')
            history = file.readlines()

            # Using enumerate for better outlook
            for i, line in enumerate(history):
                  print(f'{i+1}\t{line}')

      # In case of error
      except FileNotFoundError:

            # Create the file
            file = open('Cal_History.txt', 'x')

      # If empty file isn't readable
      except:

            # Ignore it.
            pass

      file.close()

def clear():
      '''Removes the data from the file.'''

      # Opening in write mode to clear all its data
      file = open('Cal_History.txt', 'w')
      print('\nHistory has been cleared.')

      file.close()

def errors(expression):
      '''Takes Mathematical Expression.
            Returns solution or appropriate message about the error.
            Also stores the valid inputs in a file.'''
      try:

            # Evaluating the user's input
            result = eval(expression)
            print(f'\n{expression}: {result:.2f}')

            # Storing in a file
            with open('Cal_History.txt', 'a') as file:
                  file.write(f'{expression}\n')

      # To handle these errors especially
      except NameError:
            print('\nInvalid Input... Mathematical Expressions Only.')

      except ZeroDivisionError:
            print('\nIntegers divided by 0.')

      except SyntaxError:
            print('\nInvalid Input... Syntax Error has occurred.')

      # To handle all the other errors
      except Exception as e:
            print(f'\n{e.__class__} has occurred.')


