from pypdf import PdfReader 
import sys
#input syntax: start, end, output file name, pdf name

reader = PdfReader(sys.argv[4])

def writePagesToFile(startPage, endPage, fileName) :
    outputFile = open(fileName, "w") #overwrite old file contens
    outputFile.write("")
    outputFile = open(fileName, "a") #add new file contents
    for page in range(startPage, endPage): #adds additional text deliminating page numbers
        outputFile.write("Page " + str(page) + "[DO NOT INCLUDE PAGE # IN FULL TEXT]\n" + 
        reader.pages[page].extract_text() + "\n")    

print("Writing to file...")
writePagesToFile(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])
print("Successfully wrote to file!")