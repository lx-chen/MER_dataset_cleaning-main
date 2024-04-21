import cv2
import os

sourceDir = 'D:/Baiduyun Download/Motrix Download/Put the video apart picture/raw pic' # Source folder
targetDir = 'D:/Baiduyun Download/Motrix Download/Put the video apart picture/Crop' # Target Folder
imageCount = 0
for sRoot,sDirs,sFiles in os.walk(sourceDir):
    break
for sourceName in sFiles:
    sourceFile = sourceDir + "\\"+ sourceName
    image = cv2.imread(sourceFile)
    imgCropped = image[0:300, 500:800]    #切片，图像裁剪
    imageCount+= 1
    fileName = 'frame' + str(imageCount) + '.jpg'  # change file name here
    cv2.imwrite(targetDir + '\\' + fileName, imgCropped)

    # cv2.imshow("imgBefore",img)
    # cv2.imshow("imgAfter",imgCropped)
    #
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

