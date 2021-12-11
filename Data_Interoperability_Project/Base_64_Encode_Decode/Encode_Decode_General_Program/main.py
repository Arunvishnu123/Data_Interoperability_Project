import base64

if __name__ == '__main__':

  while(True):
   operation = input("Enter E to Encode\nEnter D to decode\n")

   #Encode
   if(operation=="E" or operation=="e"):
      string_E = input("Enter the string to Encode:")
      encoded_Bytes = base64.b64encode(string_E.encode("utf-8"))
      encoded_Str = str(encoded_Bytes, "utf-8")
      print("Encoded Message Output - ",encoded_Str)

   #Decode
   if (operation == "D" or operation == "d"):
       string_D= input("Enter the string to Decode:")
       base64_bytes = string_D.encode("utf-8")
       decoded_Bytes = base64.b64decode(base64_bytes)
       decoded_Str = decoded_Bytes.decode("utf-8")
       print("Decoded Message Output - ",decoded_Str)
