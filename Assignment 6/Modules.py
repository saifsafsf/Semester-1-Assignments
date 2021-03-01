from Enc_Dec import enc_dec


def register():
      '''Registers students' data in a file.'''

      dict_stud = {}

      dict_stud['Name'] = input('\nEnter Student\'s Name: ')
      dict_stud['CMS_ID'] = input('Enter your CMS ID: ')

      password = input('Make a password: ')

      # Encrypting the password
      enc_pass = enc_dec(password, "En")

      dict_stud['Encrypted_Password'] = enc_pass

      # Writing the dictionary in a file
      with open('students.txt', 'a') as file:
            file.write(f'{dict_stud}\n')

def login():
      '''Returns User's credentials to log in.
            Also, a list of all the students is returned.'''
      
      cms_id = input('\nEnter your CMS ID: ')
      password = input('Enter your password: ')

      # Reading all the data
      with open('students.txt', 'r+') as file:
            data = file.readlines()

      list_studs = []

      # Storing in a list of dictionaries
      for line in data:
            list_studs.append(eval(line))

      return cms_id, password, list_studs

def show():
      '''Shows the record of registered students.'''

      print('\nName\t\t\tCMS ID')
      try:
            # If the file doesn't exist
            file = open('students.txt')

      except:
            # Then create the file
            file = open('students.txt', 'x')
      try:
            # Empty file is not readable
            data = file.readlines()

      except:
            #It should not crash the program
            pass
      file.close()
      list_studs = []

      # Storing the data in a list
      for line in data:
            list_studs.append(eval(line))

      # Displaying all the records
      for dicts in list_studs:
            print(f'{dicts["Name"]}\t\t\t{dicts["CMS_ID"]}')

def main_process(option):
      '''Takes the users' option & takes respective action.'''

      if option.lower() == 'register':
            register()
      
      elif option.lower() == 'show':
            show()
      else:
            print('\nInvalid Input... Try Again.')
      
