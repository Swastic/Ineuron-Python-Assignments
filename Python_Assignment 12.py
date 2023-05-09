#!/usr/bin/env python
# coding: utf-8

# Q1: PdfFileReader() needs to be opened in read-binary mode by passing 'rb'. PdfFileWriter() needs to be opened in write-binary mode by passing 'wb'.

# Q2: You can get a Page object by calling the getPage() method on a PdfFileReader object and passing it the page number of the page you're interested in.

# Q3: The total number of pages in the document is stored in the numPages attribute of a PdfFileReader object.

# Q4: first read the Pdf using the PdfFileReader Class.

# Q5: pageObj.rotateClockwise(180)
# 
# The rotateClockwise() and rotateCounterClockwise() methods. The degrees to rotate is passed as an integer argument

# Q6: Paragraph Object : A document contains multiple paragraphs. A paragraph begins on a new line and contains multiple
# runs. The Document object contains a list of Paragraph objects for the paragraphs in the document. (A new paragraph begins whenever the user presses ENTER or RETURN while typing in a Word document.)
# 
# Run Objects : Runs are contiguous groups of characters within a paragraph with the same style

# Q7: !pip install python-docx
# import docx
# doc = docx.Document('abc.docx')
# doc.paragraphs
# By using doc.paragraphs

# Q8: A Run object has bold, underline,italic,strike and outline variables

# Q9: Runs can be further styled using text attributes. Each attribute can be set to one of three values:
# True (the attribute is always enabled, no matter what other styles are applied to the run),
# False (the attribute is always disabled),
# None (defaults to whatever the run’s style is set to)
# 
# True always makes the Run object bolded and False makes it always not bolded, no matter what the style’s bold setting is. None will make the Run object just use the style’s bold setting.

# Q10: By Calling the docx.Document() function.

# Q11: 
# import docx
# doc = docx.Document()
# 
# doc.add_paragraph('Hello there!')
# doc.save('hellothere.docx')

# Q12: integer from 0 to 4
# The arguments to add_heading() are a string of the heading text and an integer from 0 to 4. The integer 0 makes the heading the Title style, which is used for the top of the document. Integers 1 to 4 are for various heading levels, with 1 being the main heading and 4 the lowest subheading
