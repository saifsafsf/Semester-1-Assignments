import Enc_Dec          # Importing module

def frequency(text, option):       # To find frequency
      '''Returns frequency of rules used.'''
      used_rules = []
      rules = {
            'a' : 'i',
            'e' : 'o',
            'i' : 'u',
            'o' : 'a',
            'u' : 'e',
            'b' : 'm',
            'd' : 't',
            'g' : 'b',
            'm' : 'd',
            't' : 'g',
            '1' : '5',
            '3' : '7',
            '5' : '9',
            '7' : '1',
            '9' : '3'
            }
      for key, value in rules.items():
            if text.count(key) != 0 and option == 'En':     # for encryption
                  used_rules.append(f'{key} → {value}\t\t{text.count(key)}')
            if text.count(value) != 0 and option == 'De':   # for decryption
                  used_rules.append(f'{value} → {key}\t\t{text.count(value)}')
      used_rules.sort()       # Sorting as required
      return used_rules
         
option = None     # Defining variable

while option != 'x':
      input_str = input('Enter your text: ')
      
      print(f'''
En - Encryption
De - Decryption
X - Exit the Program
''')
      option = input('Select an option: ')

      if option == 'X':
            print('Program exited successfully.')
            break
      elif option == 'En' or option == 'De':
            output = Enc_Dec.enc_dec(input_str, option)    # Encrypting/Decrypting

            print(f'{option}crypted Text: {output}\n')
            print('Rules\t\tFrequency')

            freq_list = frequency(input_str, option)       # Frequency list

            for val in freq_list:
                  print(f'{val}')
            print()
      else:
            print('Invalid Input... Try again.\n')          # Out-of-options input
