from PIL import Image
""" 
Project title: Andy Warhol Popart Recreation

Image sources:
1) https://www.pngall.com/pink-sparkles-png/download/174444/
2) https://mytopkid.com/picture/mytopkid-com-shailushai-cliparts-12/
3) https://creatorset.com/products/im-just-a-chill-guy-meme-green-screen

"""


def resize_to_square(image, target_size, xoffset, yoffset):
    img = Image.open("Project 2 images/" + image)
    width, height = img.size
    if width > height:
        left = (width - height) // (2 + xoffset)
        top = 0
        right = left + height
        bottom = height
    else:
        top = (height - width) // (2 + yoffset)
        left = 0
        right = width
        bottom = top + width

    img = my_crop(img,(left, top, right, bottom))
    img = my_resize(img, target_size)
    return img

def my_crop(image, box):
    left, top, right, bottom = box
    width = int(right) - int(left)
    height = int(bottom) - int(top)

    # Create a new blank image with the cropped size
    cropped_image = Image.new(mode="RGB", size=(int(width), height))

    for y in range(height):
        for x in range(width):
            # Get pixel from original image
            pixelRGB = image.getpixel((left + x, top + y))
            # Put it in the new image at the corresponding location
            cropped_image.putpixel((x, y), pixelRGB)

    return cropped_image

def my_resize(image, target_size):
    old_width, old_height = image.size
    new_width = int(target_size)
    new_height = int(target_size)

    # Create a new blank image
    resized_image = Image.new(mode="RGB", size = (new_width, new_height))

    for y in range(new_height):
        for x in range(new_width):
            # Map destination pixel to source coordinate
            src_x = int(x * old_width / new_width)
            src_y = int(y * old_height / new_height)

            # Get pixel from original image
            pixelRGB = image.getpixel((src_x, src_y))

            # Put it into resized image
            resized_image.putpixel((x, y), pixelRGB)

    return resized_image

def grid_placement(image1, image2, image3, image4, image5, image6):
    width, height = image1.size

    grid_width = int(width * 2)
    grid_height = int(height * 3)  

    grid_image = Image.new(mode = "RGB", size = (grid_width, grid_height))

    for x in range(width):
        for y in range(height):
            quad1_pixelRGB = image1.getpixel((x,y))
            quad2_pixelRGB = image2.getpixel((x,y))
            quad3_pixelRGB = image3.getpixel((x,y))
            quad4_pixelRGB = image4.getpixel((x,y))
            quad5_pixelRGB = image5.getpixel((x,y))
            quad6_pixelRGB = image6.getpixel((x,y))


            quad1_x, quad1_y = x, y
            quad2_x, quad2_y = int(x + (grid_width/2)), y
            quad3_x, quad3_y = x, int(y + grid_height/3)
            quad4_x, quad4_y = int(x + (grid_width/2)), int(y + grid_height/3)
            quad5_x, quad5_y = x, int(y + grid_height/1.5)
            quad6_x, quad6_y = int(x + grid_width/2), int(y + grid_height/1.5)

            grid_image.putpixel((quad1_x,quad1_y), quad1_pixelRGB)
            grid_image.putpixel((quad2_x,quad2_y), quad2_pixelRGB)
            grid_image.putpixel((quad3_x,quad3_y), quad3_pixelRGB)
            grid_image.putpixel((quad4_x,quad4_y), quad4_pixelRGB)
            grid_image.putpixel((quad5_x,quad5_y), quad5_pixelRGB)
            grid_image.putpixel((quad6_x,quad6_y), quad6_pixelRGB)

    return grid_image                    

def backgroundRGB_change(image, new_RGB_val, threshold):
    
    width, height = image.size

    new_image = image.copy()

    old_r, old_g, old_b = image.getpixel((1,1))

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x,y))
            color_distance = ((r - old_r) ** 2 + (g - old_g) ** 2 + (b - old_b) ** 2) ** 0.5
            if color_distance < threshold:  # Adjust threshold as needed (~150 is good)
                new_image.putpixel((x, y), new_RGB_val)

    return new_image

def four_color_conversion(image, color1, color2, color3, color4):
    width, height = image.size
    bwg_image = image.copy()

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x,y))
            brightness = (r + g + b) // 3
            if brightness <= (30):
                bwg_image.putpixel((x,y), color1) #Nose
            elif brightness <= (100):
                bwg_image.putpixel((x,y), color2) #Background
            elif brightness <= (150):
                bwg_image.putpixel((x,y), color3) #Skin
            else:
                bwg_image.putpixel((x,y), color4) #Clothes
    
    return bwg_image

def blend_images(image_base, image_top, alpha):
    #Aplha dictates opacity(ranges from 0.0 to 1.0)

    width, height = image_base.size
    blended_image = Image.new("RGB", (width, height))

    old_r, old_g, old_b = image_base.getpixel((1,1))

    for x in range(width):
        for y in range(height):
            
            r1, g1, b1 = image_base.getpixel((x,y))
            r2, g2, b2 = image_top.getpixel((x,y))

            r_blend = int(r1 * (1 - alpha) + r2 * alpha)
            g_blend = int(g1 * (1 - alpha) + g2 * alpha)
            b_blend = int(b1 * (1 - alpha) + b2 * alpha)
            
            if (r1, g1, b1) == (old_r, old_g, old_b):
                blended_image.putpixel((x,y), (r_blend, g_blend, b_blend))
            else:
                blended_image.putpixel((x,y), (r1, g1, b1))

    return blended_image

def implement():
    chillguy = resize_to_square("chillguy.jpg", 1000, 0, -0.75)
    chillguy = backgroundRGB_change(chillguy, (80,80,80), 170) #Converts background so that four color conversion has smoother background/edges
    sparkles = resize_to_square("pinksparkles.jpg", 1000, 0, 0)
    
    sparkles1 = backgroundRGB_change(sparkles, (255, 142, 172), 60)
    sparkles2 = backgroundRGB_change(sparkles, (150, 255, 127), 60)
    sparkles3 = backgroundRGB_change(sparkles, (255, 142, 74), 60)
    
    smurfsparkles1 = backgroundRGB_change(sparkles, (255, 45, 255), 60)
    smurfsparkles2 = backgroundRGB_change(sparkles, (255, 254, 3), 60)
    smurfsparkles3 = backgroundRGB_change(sparkles, (255, 44, 59), 60)


    chillguy1 = four_color_conversion(chillguy,(0, 170, 195), (255, 142, 172), (255, 210, 1), (255, 240, 90) )
    chillguy2 = four_color_conversion(chillguy,(255, 0, 0), (150, 255, 127), (1, 255, 255), (255, 255, 255) )
    chillguy3 = four_color_conversion(chillguy,(120, 5, 255), (255, 142, 74), (1, 255, 1), (255, 240, 90) )


    blended1 = blend_images(chillguy1, sparkles1, 0.5)
    blended2 = blend_images(chillguy2, sparkles2, 0.5)
    blended3 = blend_images(chillguy3, sparkles3, 0.5)

    smurf = resize_to_square("shailushai.jpg", 1000, 0, 0)
    smurf1 = four_color_conversion(smurf, (0, 170, 195), (0, 93, 252), (255, 210, 1), (255, 45, 255))

    smurf2 = four_color_conversion(smurf, (120, 5, 255), (0, 255, 179), (255, 3, 119), (255, 254, 3)) # eyes, skin, nose, background

    smurf3 = four_color_conversion(smurf, (120, 5, 255), (1, 255, 1), (255, 240, 89), (255, 44, 59))

    smurfblend1 = blend_images(smurf1, smurfsparkles1, 0.5)
    smurfblend2 = blend_images(smurf2, smurfsparkles2, 0.5)
    smurfblend3 = blend_images(smurf2, smurfsparkles3, 0.5)

 
    grid = grid_placement(blended1, smurfblend1, blended2, smurfblend2, blended3, smurfblend3)
    grid.save("result.jpg")
    

implement()

