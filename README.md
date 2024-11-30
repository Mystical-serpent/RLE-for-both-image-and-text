RLE(Run-Length-Encoding) is a lossless compression technique which looks out for repeating elements in an image or text file. It then combines all those element in one if it is same. For example: if str = 'aaaabbbb' then after RLE it should be:
4|a, 4|b. So, 4 represents the number of times the element was repeated and "|" divides the element with the count of it to avoid confusions and errors when trying to reverse the compression. 
This algorithm does that with both image and text files. However the compression reversing algorithm is still underdevelopment.
