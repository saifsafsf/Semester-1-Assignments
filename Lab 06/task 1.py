def print_message(counter):     # counter contains a value out of the list
    print(f'{counter} is present')  # Defining the inner function first
def show_presence(student_list):
    '''show_presence(['abcd', 'qwerty', ...])'''    # Documentation
    for i in student_list:
          print_message(i)  
