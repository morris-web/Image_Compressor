from PIL import Image
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Open the image file
file_path = askopenfilename()
img = Image.open(file_path)
myWidth, myHeight = img.size

# Resize the image
img = img.resize((myWidth, myHeight), Image.ANTIALIAS)

# Save the compressed image
save_path = asksaveasfilename(defaultextension=".jpg")
img.save(save_path + "_compressed.jpg")
