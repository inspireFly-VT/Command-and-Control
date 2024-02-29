import numpy as np
from PIL import Image
import PIL
from io import BytesIO
# import BytesIO
# https://www.digitalocean.com/community/tutorials/python-io-bytesio-stringio way to reduce number of libraries used?

out = BytesIO()
# Read Image 
with Image.open(r"C:\Users\7domo\Pictures\rebel friend.jpg",'r') as img:
    img.show()  #show image for fun
    img.save(out, format="JPEG") #image data now saved in 'out'
image_in_bytes = out.getvalue() #loads image data as bytes into image_in_bytes, can transmit this data?
print(image_in_bytes)

#theoretical transmission occurs here, GS now has image_in_bytes

with open('test.jpg', 'wb') as f:
    f.write(image_in_bytes)
    print("File Saves at C:\Users\*USER NAME HERE*")


