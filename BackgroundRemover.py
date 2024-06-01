from rembg import remove #pip install rembg

input_image = "yourimage.jpg"
output_image = "output.png"

with open(input_image,"rb") as i:
    with open(output_image,"wb") as o:
        input_file = i.read()
        output_file = remove(input_file)
        o.write(output_file)