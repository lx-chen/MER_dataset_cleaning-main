import cv2
import os
import numpy as np
from PIL import Image

def frame2video(im_dir, video_dir, fps):
    im_list = os.listdir(im_dir)
    im_list.sort(key=lambda x: int(x.replace("frame", "").split('.')[0]))  # 最好再看看图片顺序对不
    img = Image.open(os.path.join(im_dir, im_list[0]))
    img_size = img.size  # 获得图片分辨率，im_dir文件夹下的图片分辨率需要一致

    # fourcc = cv2.cv.CV_FOURCC('M','J','P','G') #opencv版本是2
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # opencv版本是3
    videoWriter = cv2.VideoWriter(video_dir, fourcc, fps, img_size)
    # count = 1
    for i in im_list:
        im_name = os.path.join(im_dir + i)
        frame = cv2.imdecode(np.fromfile(im_name, dtype=np.uint8), -1)
        videoWriter.write(frame)
        # count+=1
        # if (count == 200):
        #     print(im_name)
        #     break
    videoWriter.release()
    print('finish')


if __name__ == '__main__':
    sourceDir = 'D:/Baiduyun Download/Motrix Download/Zhongshan Dataset/6/visible'  # 帧存放路径
    targetDir = 'D:/Baiduyun Download/Motrix Download/Zhongshan Dataset/7/visible'  # 合成视频存放的路径
    fps = 30  # 帧率，每秒钟帧数越多，所显示的动作就会越流畅
    for i in range(61):   # 文件夹数量
        sourceDir_pic = sourceDir + "\\" + str(i + 86) + "\\"
        print(sourceDir_pic)
        # for sRoot, sDirs, sFiles in os.walk(sourceDir_pic):
        #     break
        # for sourceName in sFiles:
        #     sourceFile = sourceDir_pic + '\\' + sourceName
        #     print(sourceFile)
        fileName = 'video' + str(i+86) + '.mp4'  # change file name here
        targetDir_video = targetDir + "\\" + fileName
        frame2video(sourceDir_pic, targetDir_video, fps)



