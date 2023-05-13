#!/usr/bin/env python
# coding: utf-8

# Q1: The RGB color model is extended in this specification to include “alpha” to allow specification of the opacity of a color.

# Q2: Pillow offers the ImageColor. getcolor() function so you don't have to memorize RGBA values for the colors you want to use. This function takes a color name string as its first argument, and the string 'RGBA' as its second argument, and it returns an RGBA tuple.

# Q3: The box. tuple submodule provides read-only access for the tuple userdata type. It allows, for a single tuple: selective retrieval of the field contents, retrieval of information about size, iteration over all the fields, and conversion to a Lua table.

# Q4: from PIL import Image
# 
# im = Image.open('whatever.png')
# width, height = im.size

# Q5: To get an Image object for a 100x100 image, excluding the lower-left quarter of it, you would need to use the HTML5 Canvas API to manipulate the image data.

# Q6: To save images, we can use the PIL.save() function. This function is used to export an image to an external file. 

# Q7: The 'ImageDraw' module provides simple 2D graphics support for Image Object. Generally, we use this module to create new images, annotate or retouch existing images and to generate graphics on the fly for web use. The graphics commands support the drawing of shapes and annotation of text.

# Q8: Image objects doesn't have drwa method but by using ImageDraw. First, we import Image and ImageDraw. Then we create a new image, in this case, a 200×200 white image, and store the Image object in it. We pass the Image object to the ImageDraw.Draw() function to receive an ImageDraw object. This object has several methods for drawing shapes and text onto an Image object. Store the ImageDraw object in a variable like draw so you can use it easily in the following example.
