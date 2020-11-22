"""
Author username(s): moenchlm, najs
Date: 11/10/20
Assignment/problem number: P13
Assignment/problem title: Image Processing
"""

import image
import math

def color2gray(color): # For exercise 9.3.1
    """Convert a color to a shade of gray.
    Parameter: color, a tuple representing an RGB color
    Produces: a tuple representing an equivalent gray
    """
    brightness = (color[0] + color[1] + color[2]) // 3
    return (brightness, brightness, brightness)

def grayscale(photo): # For exercise 9.3.1
    """Convert a color image to grayscale.
    Parameter: photo, an Image object
    Produces: a new grayscale Image object
    """
    width = photo.width()
    height = photo.height()
    newPhoto = image.Image(width, height, title = 'Grayscale image')
    for y in range(height):
        for x in range(width):
            color = photo.get(x,y)
            newPhoto.set(x, y, color2gray(color))
    return newPhoto

def brighter_color(color, factor): # For exercise 9.3.4
    """Increase all components of the color by factor.
    """
    r = min(color[0] * factor, 255)
    g = min(color[1] * factor, 255)
    b = min(color[2] * factor, 255)
    color = (r, g, b)
    return color

def brighten(photo, factor):       # For exercise 9.3.4
    """Make the photo brighter by making  each pixel brighter.
    """
    height = photo.height()
    width = photo.width()
    for y in range(height):
        for x in range(width):
            color = photo.get(x, y)
            photo.set(x, y, brighter_color(color, factor))
    return photo

def reduce(photo):
    """
    Reduce an imaage to one half of its size.

    Parameters
    ----------
    photo : an image object
        

    Returns
    -------
    A new reduced image object.

    """
    width = photo.width()
    height = photo.height()
    root_two = math.sqrt(2)
    halfwidth = math.trunc(width / root_two)
    halfheight = math.trunc(height / root_two)
    newPhoto = image.Image(halfwidth, halfheight, title = 'Reduced Image')
    for y in range(0, height, math.trunc(root_two)):
        for x in range(0, width, math.trunc(root_two)):
            color = photo.get(x, y)
            newPhoto.set(math.trunc(x // root_two), math.trunc(y // root_two), color)
    return newPhoto

def blur(photo):
    """
    Makes a new image that is blurrier than the old one

    Parameters
    ----------
    photo : .GIF
        an iterable image object as described in the image module.

    Returns
    -------
    blurPhoto : .GIF
        an iterable image object as described in the image module.

    """
    offsets = [ (-1, -1), (-1, 0), (-1, 1), (0, -1), 
               (0, 1), (1, -1), (1, 0), (1, 1)]
    height = photo.height()
    width = photo.width()
    blurPhoto = image.Image(width, height, title = "Blurred Image")
    for y in range(height):
        for x in range(width):
            kernelAvgR = 0
            kernelAvgG = 0
            kernelAvgB = 0
            #print("The current coord is " + str((x, y)))
            neighbors = 1
            for offset in offsets:
                xOff = x + offset[0]
                yOff = y + offset[1]
                #print("The current offset is " + str((xOff, yOff)))
                if xOff > 0 and xOff < width:
                    if yOff > 0 and yOff < height:
                        #print(neighborcolor)
                        neighbors += 1
                        #print("The current coord has " + str(neighbors) + " neighbors")
                        kernelRGB = photo.get(xOff, yOff)
                        kernelAvgR += kernelRGB[0]
                        kernelAvgG += kernelRGB[1]
                        kernelAvgB += kernelRGB[2]
                        #print(kernelAvgR, kernelAvgG, kernelAvgB)
            kernelAvgR = kernelAvgR // neighbors
            kernelAvgG = kernelAvgG // neighbors
            kernelAvgB = kernelAvgB // neighbors
            #print(kernelAvgR, kernelAvgG, kernelAvgB)
            blurPhoto.set(x, y, (kernelAvgR, kernelAvgG, kernelAvgB))
    return blurPhoto

def repeat_blur(photo, times):
    """
    Makes a photo blurrier by a fixed amount for a given number of iterations

    Parameters
    ----------
    photo : .GIF
        an iterable image object as described in the image module.
    times : int
        the number of times the photo shall be blurred.

    Returns
    -------
    blurPhoto : .GIF
    an iterable image object as described in the image module.
    
    """
    height = photo.height()
    width = photo.width()
    blurPhoto = image.Image(width, height, title = "Blurred Image")
    for x in range(width):
        for y in range(height):
            coordColor = photo.get(x, y)
            blurPhoto.set(x, y, coordColor)
    for i in range(times):
        blurPhoto = blur(blurPhoto)
    return blurPhoto

def crop(photo, topleft_x, topleft_y, width, height):
    """
    

    Parameters
    ----------
    photo : .GIF
        an iterable image object as described in the image module.
    topleft_x : int
        the leftmost x coordinate to be copied from the old image to the new.
    topleft_y : int
        the uppermost y coordinate to be copied from the old image to the new.
    width : int
        the width of the new image/the slice from the old.
    height : int
        the height of the new image/the slice from the old.

    Returns
    -------
    cropPhoto : .GIF
    an iterable image object as described in the image module, now cropped.

    """
    cropPhoto = image.Image(width, height, title = "Cropped Image")
    for x in range(topleft_x, width):
        for y in range(topleft_y, height):
            coordColor = photo.get(x, y)
            cropPhoto.set(x, y, coordColor)
    return cropPhoto

def main():
    penguin = image.Image(file='penguin.gif', title='Penguin')
    penguin.show()
    blurpenguin = blur(penguin)
    blurpenguin.show()
    penguinModified = grayscale(penguin)
    penguinModified.show()
    littlepenguin = reduce(penguin)
    littlepenguin.show()
    fourblurPenguin = repeat_blur(penguin, 4)
    fourblurPenguin.show()
    croppedPenguin = crop(penguin, 30, 50, 139, 200)
    croppedPenguin.show()
    brighterpenguin = brighten(penguin, 2)
    brighterpenguin.show()
    image.mainloop()
if __name__=='__main__':
    main()
