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
    
#RLE for text file
def Text_RLE_Converter():
    Text_file_path = input("Text File path: ").strip() 
    try:
        encoded_message = [] #Encoded text is stored here 
        with open(Text_file_path, 'r', encoding='utf-8') as file: #opening the given file with file path as read. utf - 8 deals with non ASCII characters if they are present
            File_content = file.read() #Reading the contents in the file 

        count = 1
        for each in range(len(File_content)):
            if each + 1 < len(File_content) and File_content[each] == File_content[each + 1]:
                count += 1
            else:
                encoded_message.append(f"{count}|{File_content[each]}")
                count = 1

        return encoded_message
    
    #Handling file error which may occur if the file does not exist or is corrupt 
    except FileNotFoundError:
        print("The text file was not found, try again")
        return Text_RLE_Converter()

    except Exception as Error:
        print(f"Error occured: {Error}")
        return Text_RLE_Converter()
    
#Asking for value and redirecting to the correct function
print("1: Image file, 2: Text file")
Value = input("Enter value: ").strip()
if Value == "1":
    encoded_image = Image_RLE_Converter()
    print(encoded_image)
elif Value == "2":
    encoded_text = Text_RLE_Converter()
    print(encoded_text)
else:
    print("Incorrect value")