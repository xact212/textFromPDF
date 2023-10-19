This program etxracts text from a pdf file and puts it in a .txt file without 
the formatting issues you would get if you attempted to copy paste the pdf 
into another document directly. Relies on this library: https://pypi.org/project/pypdf/
which will need to be installed on the host machine via this command: pip install pypdf


To use this program:
    1. Open up a Command Line Interface (Windows Command Prompt, Moba Xterm)
    2. Navigate to where you downloaded the program folder 
    using this command: cd [program folder path here]
    If you have trouble finding the program folder, open the file 
    explorer, and find the folder in there. At the top of the file explorer
    there shold be a bar in the middle with a folder icon to the left of it.
    Click on the white space of this bar and copy the filepath you have 
    selected to paste it into your Command Line Interface
    3. Now run this command: python3 textFromPDF.py [starting page] [ending page] [output filename].txt
    4. You can now access the text the progam output by opening the output text file

