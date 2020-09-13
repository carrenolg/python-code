# example import module

# from report import get_description_without_import as do_it
import sys

# description = do_it()
# print("Today's weather:", description)

# In this variable (sys.path) Python look for files to import the modules
for place in sys.path:
    print(place)
