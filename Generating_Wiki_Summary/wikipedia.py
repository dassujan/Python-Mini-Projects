# install libraries
# pip install pywhatkit

# import the package
import pywhatkit as kit

#display welcome message
print("Let's Generate Wiki Summary!\n")

#call the method
search = input("Searching Wikipedia: ")

# kit.info(search)

kit.info(search, lines=3)