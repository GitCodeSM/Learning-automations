'''
Auto Searching for multiple pages at a time
'''

# importing the module
import pywhatkit

# example: my_topics = [SoloLearn Programiz Simpliv CodeCademy FreeCodeCamp Coursera Edx GeekForGeeks Stack Overflow]

my_topics = input("input sites: ").split()

# use Try Except to
# handle the Exceptions

for page in my_topics:
  try:
  
  # it will perform the Google search
  #pywhatkit.search("popular python tutorial pages")
    pywhatkit.search(page)
    print("Searching...")
 
  except:
   
  # Printing Error Message
    print("An unknown error occurred")
