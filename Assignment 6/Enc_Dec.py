def enc_dec(text, opt):
      '''Encrypts or decrypts the text, as per given 'opt' "En" OR "De" '''    # Documentation
      output = ''       # Defining variable
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
            }           # Defining rules of encryption/decryption
      
      for char in text:
            for key, value in rules.items():
                  if char == key and opt == 'En':
                        output += value   # Storing encrypted text
                        break
                  elif char == value and opt == 'De':
                        output += key     # Storing decrypted text
                        break
                  elif char not in rules:
                        output += char    # e.g for spaces
                        break
      return output
