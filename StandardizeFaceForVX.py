import os, glob
from PIL import Image

path = "D:/Projects/ツクール/雨/1_face/"
files = glob.glob(path + "*.png")
os.makedirs(path+"result",exist_ok=True)
count = 0
newImg = None
for f in files:
    if count%8==0:
        newImg = Image.new("RGBA", (96*4, 96*2))
    img = Image.open(f)
    img_resize = img.resize((96, 96),Image.LANCZOS)
    newImg.paste(img_resize, (count%4*96, count%8//4*96))
    if count%8 == 7:
        #ftitle, fext = os.path.splitext(f)
        #index = ftitle.rfind("\\")
        #ftitle = ftitle[:index] + "/result" + ftitle[index:]
        newImg.save(path + "result/" + str(count//8) + "_ace.png")
    count+=1
if count%8!=0:
    newImg.save(path + "result/" + str(count//8) + "_ace.png")
