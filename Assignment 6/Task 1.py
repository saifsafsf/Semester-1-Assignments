from Enc_Dec import enc_dec

# Importing all user_defined functions from...
from Modules import *

# To enter while loop
option = None

while option != 'exit':
      # Menu
      print(f'''
register - Register new student.
show - Show registered students.
login - Student Login.
exit - Exit the Program.
''')
      option = input('Select an option: ')

      # To register new students OR show records of registered students
      if option.lower() == 'register' or option.lower() == 'show':
            main_process(option)

      # To exit the program
      elif option.lower() == 'exit':
            print('Program exited successfully.')
            break

      # To login as a user
      elif option.lower() == 'login':
            cms_id, password, list_studs = login()

            # To stay logged in
            while option.lower() != 'out':

                  # To find similar dictionary to match credentials
                  for dicts in list_studs:

                        # Decrypting the stored password to compare
                        actual_pass = enc_dec(dicts['Encrypted_Password'], 'De')

                        # If match is found
                        if cms_id == dicts['CMS_ID'] and password == actual_pass:

                              # Menu changes a little
                              print(f'''
change - Change username.
delete - Delete this account.
out - Log out.
register - Register new student.
show - Show registered students.
''')
                              option = input('Select an option: ')

                              # To change username
                              if option == 'change':
                                    username = input('\nEnter new username: ')

                                    # Updating previous username
                                    dicts['Name'] = username

                                    print('\nUsername changed successfully.')
                                    break

                              # To delete a record
                              elif option == 'delete':

                                    # Confirmation
                                    confirm = input('Are you sure? Yes/No: ')

                                    if confirm.lower() == 'yes':

                                          # Removed from the list of dictionaries
                                          list_studs.remove(dicts)

                                          print('\nYour data has been erased successfully.')

                                          # To log out
                                          option = 'out'
                                    break

                              # To log out
                              elif option == 'out':
                                    break

                              # To show old records OR register new ones
                              else:
                                    main_process(option)
                                    break
                  # If CMS ID & password don't match
                  else:
                        print('\nInvalid Credentials...')
                        option = 'out'

                  # Writing altered list of dictionaries in the file
                  with open('students.txt', 'w') as file:
                        for dicts in list_studs:
                              file.write(f'{str(dicts)}\n')
      # Out-of-menu input
      else:
            print('\nInvalid Input... Try Again.')
