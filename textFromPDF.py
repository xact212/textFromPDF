import fitz
import sys

#input syntax: start, end, output file name, pdf name

doc = fitz.open(sys.argv[4])

specialCharacterMap = {

}

uppercaseChars = ["A", "B", "C", "D", "E", "F", "G", "H", "I" ,"J", "K" ,"L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowercaseChars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

#much of this code comes from the PyMuPDF Documentation, specifically from the section about font information
def flags_decomposer(flags):
    """Make font flags human readable."""
    l = []
    if flags & 2 ** 0:
        l.append("superscript")
    if flags & 2 ** 1:
        l.append("italic")
    if flags & 2 ** 2:
        l.append("serifed")
    else:
        l.append("sans")
    if flags & 2 ** 3:
        l.append("monospaced")
    else:
        l.append("proportional")
    if flags & 2 ** 4:
        l.append("bold")
    return ", ".join(l)

def checkForParagraph(prevX, currX, outFH, prevInPTag, pTagThresh):
    deltaX = currX - prevX
    print("deltaX", deltaX,"curr x:", currX,"prev x:", prevX)
    if abs(deltaX) >= pTagThresh:
        if not prevInPTag:
            outFH.write("\n<p>\n")
        else:
            outFH.write("\n</p>\n")
        return not prevInPTag
    else:
        return prevInPTag

def writePagesToFile(startPage, endPage, fileName):
    outputFile = open(fileName, "w") #overwrite old file contens
    outputFile.write("")

    outputFile = open(fileName, "a") #add new file contents
    outputFile.write("<HTML>")
    filePos = 0
    prevInEmph = False
    prevInPTag = False
    prevChar = ""
    prevX = 0
    pTagThresh = 10
    for page in range(startPage, endPage): #adds additional text deliminating page numbers
        outputFile.write("\n<h4>Page " + str(page + 1) + "</h4>\n")

        # read page text as a dictionary, suppressing extra spaces in CJK fonts
        blocks = doc[page].get_text("dict", flags=11)["blocks"]
        for b in blocks:  # iterate through the text blocks
            if not prevInPTag:
                outputFile.write("\n<p>\n")
            else:
                outputFile.write("\n</p>\n")
            prevInPTag = not prevInPTag
            for l in b["lines"]:  # iterate through the text lines
                for s in l["spans"]:  # iterate through the text spans
                    for char in s["text"]:

                        #prevInPTag = checkForParagraph(prevX, s["origin"][0], outputFile, prevInPTag, pTagThresh)
                        #prevX = s["origin"][0]
                        
                        if (prevChar in lowercaseChars or prevChar in nums) and char in uppercaseChars: #add newlines
                            outputFile.write("\n")
                        if prevChar == "." and char == " ":
                            outputFile.write("\n")
                            continue
                        font_properties = { "flags" : flags_decomposer(s["flags"]) }
                        if "italic" in font_properties["flags"] or "bold" in font_properties["flags"]: #add em tags for bold/italic
                            if not prevInEmph:
                                outputFile.write("<em>")
                                prevInEmph = not prevInEmph
                        elif prevInEmph:
                            outputFile.write("</em>")
                            prevInEmph = not prevInEmph
                        try: #don't include non ascii characters and print them out for debugging
                            char.encode("ascii")
                        except:
                            print(char)
                            continue
                        try: #try mapping character with character map. if it succeeds, replace with replacement character
                            replacement = specialCharacterMap[char]
                            outputFile.write(replacement)
                            prevChar = replacement
                            continue
                        except:
                            pass
                        outputFile.write(char)
                        prevChar = char
                    
                    
        outputFile.write("</HTML>")
    

print("Writing to file...")
writePagesToFile(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])
print("Successfully wrote to file!")

