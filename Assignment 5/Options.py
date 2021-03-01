def options(option):
      '''Takes an empty variable
            Returns an option according to the menu.'''

      print(f'''
g - Input teams' details.
s - View a schedule for tournament.
r - Enter results of the current round.
v - View the teams' details
x - Exit the program.
''')              # The menu

      while option != 'g' and option != 's' and option != 'r' and option != 'v' and option != 'x':
            option = input('Select an option: ')
            # To keep asking in case of inavlid input

      return option
