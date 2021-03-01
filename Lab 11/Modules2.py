def strength(password):
      '''Takes a password.
            Returns its strength out of 10.'''
      
      pass_strength = 0

      # If length of password is Good.
      if 16 >= len(password) >= 8:
            pass_strength += 2

      # If password has a special character
      if ('$' in password) or ('@' in password) or ('#' in password):
            pass_strength += 3

      lower, upper, alpha, num = False, False, False, False

      # If a letter(lower or upper) or a number is found
      for a in password:
            if a.islower():
                  lower = True

            elif a.isupper():
                  upper = True

            elif a.isdigit():
                  num = True

            if a.isalpha():
                  alpha = True

      # In case of alphanumeric
      if num == True and alpha == True:
            pass_strength += 3

      # In case of lowercse & uppercase
      if upper == True and lower == True:
            pass_strength += 2

      return pass_strength

def output(pass_strength, password):
      '''Takes password & its strength
            Returns Strength with appropriate comments.'''

      # If strength exceeds 8
      if pass_strength > 8:

            # Storing password in a file
            file = open('passwords.txt', 'a')
            file.write(f'{password}\n')
            file.close()

            # Giving comments
            print(f'\nStrength: {pass_strength}/10.\nYour password is STRONG!\n')

      else:

            # Giving comments
            print(f'\nStrength: {pass_strength}/10.')
            print(f'\nYour password is weak.\nTry adding atleast 1 symbol, 1 lowercase & 1 uppercase letter.')
            print('\nAlso, make sure it\'s alphanumeric & has more than 8 characters but not more than 16.')
            print('\nNow, Try Again.\n')
