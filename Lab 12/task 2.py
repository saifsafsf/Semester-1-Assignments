# Importing module
from tkinter import *

# Making window
window = Tk()

# Title
window.title('Calculator')

# Textbox
txt_box = Entry(window, width=70)
txt_box.grid(row=0, column=0, sticky = 'nswe', columnspan = 5)

# All the texts on buttons
txts = ['Cls', 'Back', ' ', 'Close',
        7, 8, 9, '/',
        4, 5, 6, '*',
        1, 2, 3, '-',
        0, '.', '=', '+']

# Button Counter
k = 0

# i for row number
for i in range(1, 6):

      # j for column number
      for j in range(1, 5):

            # Button with text from list & button counter as index
            bttn = Button(window,
                          text = f'{txts[k]}',
                          width=10, height=2,
                          font=('Cambria Bold', 14))

            # Position in grid
            bttn.grid(row=i, column=j)

            k += 1

# End of Tkinter program
window.mainloop()
