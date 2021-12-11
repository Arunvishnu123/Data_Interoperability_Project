import base64
from PIL import Image
from io import BytesIO

with open(r'C:\Users\ARUN\OneDrive\Desktop\Data_Interoperability_Project\Base_64_Encode_Decode\Decode_Image_What_is_this\base64.txt','r') as handle:
       li =[]
       lines = handle.readlines()
       print(lines)
       print(lines)
       for line in lines:
             tt = line.split()
             li.append(tt)
             print(li)
       #print(li[7][1][27:-3])

image = Image.open(BytesIO(base64.b64decode(li[7][1][27:-3])))
image.save(r'C:\Users\ARUN\OneDrive\Desktop\Data_Interoperability_Project\Base_64_Encode_Decode\Decode_Image_What_is_this\what_is_this.png', 'PNG')
