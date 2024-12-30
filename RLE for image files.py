from PIL import Image #To allow the program to access the iamge through file path 

#RLE for image file
def Image_RLE_Converter():
    Image_File_path = input("Enter File path: ").strip()
    try:
        image = Image.open(Image_File_path)
        Image_RGB = image.convert("RGB") #Changes the image to RGB if is converted to the grayscale
        Pixel_list = list(Image_RGB.getdata()) #Allows to store pixel value of a picture
        Encoded_Image = []#Encoded image pixels are stored here
        count = 1
        #Checks for each pixel in Pixel_list 
        for each_pixel in range(1, len(Pixel_list)):
            if Pixel_list[each_pixel] == Pixel_list[each_pixel - 1]:
                count += 1
            else:
                Encoded_Image.append([Pixel_list[each_pixel - 1], count])
                count = 1

        #Appending encoded values in Encoded_Image
        Encoded_Image.append([Pixel_list[-1], count])
        return Encoded_Image
    
    #Handling file error which may occur if the file does not exist or is corrupt 
    except FileNotFoundError:
        print(f"Image file not found. Please try again.")
        return Image_RLE_Converter()  

    except Exception as Error:
        print(f"Error occurred: {Error}")
        return Image_RLE_Converter()
Image_RLE_Converter()