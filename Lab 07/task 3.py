import math     # To use math.sqrt, importing math module
def show_difference(length, width):     # Documentation
    '''show_difference(length, width)
        Returns the difference of areas of inscribed ellipse & circle touching the vertices'''
    area_ell, area_cir = None, None
    def area(length, width):
        nonlocal area_ell, area_cir     # So their vaues are changed by area() func.
        area_ell = (length/2) * (width/2) * 3.1416  # Using formula
        hyp_sqr = (length**2) + (width**2)      # Pythagorean Theorem
        rad = math.sqrt(hyp_sqr)
        area_cir = (3.1416) * (rad**2)      # Using formula
    area(length, width)
    diff = area_cir - area_ell
    print(f'The difference of areas of circle & ellipse: {diff:.4f} unit sq.')   # Displaying output

# show_difference() will be called when the program is run.
# As specified in the question, "Use this function to get the length & width of the rectangle."
# So, this function is used to give values and not the input()
