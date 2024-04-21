#removes small images (<80x80) and resize all remaining images to 80x80
import os
import cv2

# 调整单个文件夹中人脸尺寸
# sourceDir = 'D:/CS dataset/Zhongshan Dataset 2023.1.12/2.only eyes picture/1.faceCrop/visible' # Source folder
# targetDir = 'D:/CS dataset/Zhongshan Dataset 2023.1.12/2.only eyes picture/2.resize face/visible' # Target Folder

sourceDir = 'D:/CS dataset/Zhongshan Dataset 2023.3.19-1.12 combine/1.Zhongshan data combine1.12-3.19/dataset_common2_expansion_only_eye/test/invisible' # Source folder
targetDir = 'D:/CS dataset/Zhongshan Dataset 2023.3.19-1.12 combine/1.Zhongshan data combine1.12-3.19/dataset_common2_expansion_only_eye_224/test/invisible' # Target Folder
imageCount = 0
for sRoot,sDirs,sFiles in os.walk(sourceDir):
    break
for sourceName in sFiles:
    sourceFile = sourceDir+'\\'+sourceName
    image = cv2.imread(sourceFile)
    if image.shape[0] != 100:   # ！=80
        imageCount+=1
        # fileName = 'invisible'+str(imageCount)+'.jpg' #change file name here
        fileName = sourceName
        imageResize = cv2.resize(image,(224,224)) # resize to 80x80 pixel    # (192,64)
        cv2.imwrite(targetDir+'\\'+fileName,imageResize)


# # 连续调整多个文件夹中人脸尺寸
# sourceDir = 'D:/Baiduyun Download/Motrix Download/Zhongshan Dataset/5/visible' # Source folder
# targetDir = 'D:/Baiduyun Download/Motrix Download/Zhongshan Dataset/6/visible' # Target Folder
# imageCount = 0
# for i in range(61):  # 文件夹数量
#     sourceDir_pic = sourceDir + "\\" + str(i + 1)
#     for sRoot,sDirs,sFiles in os.walk(sourceDir_pic):
#         break
#     for sourceName in sFiles:
#         sourceFile = sourceDir_pic+'\\'+sourceName
#         image = cv2.imread(sourceFile)
#         if (image.shape[0]!= 80 or image.shape[1]!= 80):   # ！=80
#             imageCount+=1
#             # fileName = 'invisibility'+str(imageCount)+'.jpg' #change file name here
#             imageResize = cv2.resize(image,(80,80)) # resize to 80x80 pixel    # (80,80)
#             cv2.imwrite(targetDir + "\\" + str(i + 1) + '\\'+sourceName,imageResize)
#             print(targetDir + "\\" + str(i + 1) + '\\'+sourceName)