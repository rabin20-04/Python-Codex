# import i_to_import  # for our ease we write any name here it is tii
# to import whole file or module

import i_to_import as tii  # for our ease we write any name here it is tii


courses = ["math", "science", "mechanics", "fluid"]

# index =       i_to_import.find_index(courses, "math")
index = tii.find_index(courses, "math")
print(index)


# to import the function

# from i_to_import import find_index
# index = find_index(courses, "math")


# this will import everything but will be very hard to read as which came from where
# The statement from i_to_import import * is used in
#  Python to import all the contents (functions, classes, variables, etc.)
# from the module i_to_import into the current namespace.
