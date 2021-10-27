# install Libraries
# pip install PyPDF2
# pip install pyttsx3

# import the necessary package
import pyttsx3 
import PyPDF2

book = open('keyboard-shortcuts-windows.pdf','rb')    # rb stand for readingbook
pdf_reader = PyPDF2.PdfFileReader(book)     # book store in pdf method
num_pages = pdf_reader.numPages     # book store in num_pages method

play = pyttsx3.init()   # initialize python Text to Speech
print('Playing Audio Book')

# run a for loop num of pages in pdf file 
for num in range(0, num_pages):
	page = pdf_reader.getPage(num)

	data = page.extractText()   # extract as text method

	play.say(data)      # say method on play and pass data
	play.runAndWait()   # runAndWait method on play and pass data