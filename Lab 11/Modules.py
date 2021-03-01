def menu():
      '''Returns the option selected by user out of a menu.'''

      # The Menu
      print(f'''
r - Read file
s - Statistics
e - Export words from file
x - Exit the program
''')

      # Taking Input
      option = input('Select an option: ')
      print()

      return option

def read(file_name):
      '''Reads given file.
            Returns data read from it.'''

      print('\nReading the file...')

      file = open(file_name)

      # Reading the file
      data = file.read()
      file.close()

      print('File has been read successfully.\n')

      return data

def statistics(data):
      '''Takes data from a file
            Returns Number of sentences & words'''

      # Defining variable for later use
      total_words = 0

      # Splitting paragraph into sentences
      sentences = data.split('. ')
      num_sentences = len(sentences)      # Number of sentences

      for sentence in sentences:

            # Splitting sentences into words
            words = sentence.split(' ')
            num_words = len(words)
            total_words += num_words      # Number of words

      return num_sentences, total_words

def search(data):
      '''Takes data from a file
            Returns words & their frequencies'''

      user_inp = input('Enter space-seperated terms: ')

      # Splitting string into list of words
      words = user_inp.split(' ')

      words.sort(key = data.count)        # Sorting according to their frequencies

      print('\nWords\t\tFrequency')

      for word in words:
            print(f'{word}\t\t{data.count(word)}')

      return words

def store(data, words):
      '''Takes data from a file & specific words.
            Writes words & their frequencies in a file'''

      file = open('lab_test3.txt', 'a')
      file.write('Words\t\tFrequency\n')

      for word in words:

            # Writing with proper formatting
            file.write(f'{word}\t\t{data.count(word)}\n')

      file.close()
