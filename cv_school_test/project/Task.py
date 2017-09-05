import os,sys
from PIL import Image


imagesPath = os.path.join("..", "images")
annoFilePath = os.path.join("..", "annotations")
fragmentsFilePath = os.path.join("..", "fragments")

partFileNameList = ["person_292", "person_and_bike_125", "person_and_bike_132"]


def task0_crop():
    for partFileName in partFileNameList:
        imageName = partFileName + ".png"
        imageFile = Image.open(os.path.join(imagesPath, imageName))

        annoFileName = partFileName
        with open(os.path.join(annoFilePath, annoFileName + os.extsep + "txt")) as f:
            annoLines = f.readlines()

        for i, anno in enumerate(annoLines):
            annoNormal = tuple(map(int, anno.split(',')))
            imageCropped = imageFile.crop(annoNormal)
            imageCropped.save(os.path.join(fragmentsFilePath, partFileName + "_" + str(i) + os.extsep + "png"))


task0_crop()

