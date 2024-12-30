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
Text_RLE_Converter()