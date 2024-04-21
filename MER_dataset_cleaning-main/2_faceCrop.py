"""
功能：人脸识别与裁剪
"""
# face detection
# to remove multiple face images, non face images and corrupt/non convertible images
import os
import cv2
import mediapipe as mp

def faceBox(frame):#face bounding box
    try:
        frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    except:
        return []
    # imgCropped = frameRGB[0:700, 500:800]  # 切片，图像裁剪
    results = findFace.process(frameRGB)   # frameRGB
    myFaces = []
    if results.detections != None:
        for face in results.detections:
            bBox = face.location_data.relative_bounding_box
            myFaces.append(bBox)
    return myFaces



if __name__ == '__main__':
    # 裁剪单个文件夹中的人脸图片
    sourceDir = "D:/CS dataset/Zhongshan Dataset 2023.1.12/dataset/visible"
    targetDir = 'D:/CS dataset/Zhongshan Dataset 2023.1.12/2.only eyes picture/1.faceCrop/visible'  # Target Folder
    imageCount = 0  # for file naming
    errorCount = 0
    findFace = mp.solutions.face_detection.FaceDetection()
    for sRoot, sDirs, sFiles in os.walk(sourceDir):
        break
    for sourceName in sFiles:
        sourceFile = sourceDir + '\\' + sourceName
        image = cv2.imread(sourceFile)
        faceBoxes = faceBox(image)
        if len(faceBoxes) == 1:
            imageCount += 1
            fileName = 'frame' + str(imageCount) + '.jpg'  # change file name here
            height, width, channel = image.shape
            x, y, w, h = int(faceBoxes[0].xmin * width), int(faceBoxes[0].ymin * height), int(
                faceBoxes[0].width * width), int(faceBoxes[0].height * height)
            print(h)
            # 裁剪人脸
            # cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),1)
            # croppedImage = image[y - 10:y + h, x:x + w]  # 这里可以调整裁剪的大小

            # 仅裁剪眼周位置
            h_eyse = h//3    #取整，因为切片索引只能取整
            croppedImage = image[y - 5 : y + h_eyse, x : x + w]  # 这里可以调整裁剪的大小

            try:
                cv2.imwrite(targetDir + '\\' + fileName, croppedImage)
            except:
                errorCount += 1
                print(errorCount)
                continue



    # # 裁剪多单个文件夹中的人脸图片    复制4.video fragment to frame中文件直接覆盖
    # sourceDir = "D:/Baiduyun Download/Motrix Download/Zhongshan Dataset/4/visible"  # Source folder
    # targetDir = 'D:/Baiduyun Download/Motrix Download/Zhongshan Dataset/5/visible'  # Target Folder
    # imageCount = 0  # for file naming
    # errorCount = 0
    # findFace = mp.solutions.face_detection.FaceDetection()
    # for i in range(1):   # 文件夹数量
    #     sourceDir_pic = sourceDir + "\\" + str(i + 1)   #  sourceDir_pic = sourceDir + "\\" + str(i + 1)
    #     print(sourceDir_pic)
    #     for sRoot, sDirs, sFiles in os.walk(sourceDir_pic):
    #         break
    #     for sourceName in sFiles:
    #         sourceFile = sourceDir_pic + '\\' + sourceName
    #         print(sourceFile)
    #         image = cv2.imread(sourceFile)
    #         faceBoxes = faceBox(image)
    #         if len(faceBoxes) == 1:
    #             imageCount += 1
    #             # fileName = 'frame' + str(imageCount) + '.jpg'  # change file name here
    #             height, width, channel = image.shape
    #             x, y, w, h = int(faceBoxes[0].xmin * width), int(faceBoxes[0].ymin * height), int(
    #                 faceBoxes[0].width * width), int(faceBoxes[0].height * height)
    #             # cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),1)
    #             croppedImage = image[y - 10:y + h, x:x + w]  # 这里可以调整裁剪的大小
    #             try:
    #                 cv2.imwrite(targetDir + '\\' + str(i + 1) + '\\' + sourceName, croppedImage)
    #                 print(targetDir + '\\'+ str(i + 1) + '\\' + sourceName)
    #             except:
    #                 errorCount += 1
    #                 print(errorCount)
    #                 continue
