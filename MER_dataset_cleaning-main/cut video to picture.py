"""
功能：将视频转换成图片
"""
import cv2
import os
def video2frame(video_path, frames_save_path, time_interval):
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0
    count_real = 0
    # while count_real <= 28:
    while success:
        success, image = vidcap.read()
        count += 1
        if count % time_interval == 0:
            # count_real += 1
            # cv2.imencode(".jpg", image)[1].tofile(frames_save_path + "/frame%d.jpg" % count_real)
            cv2.imencode(".jpg", image)[1].tofile(frames_save_path + "/frame%d.jpg" % count)
        print(count)


if __name__ == '__main__':
    # 单个视频裁剪
    video_path ="D:/CS dataset/Zhongshan Dataset 2023.1.12/video/11.mp4"
    frames_save_path = "D:/CS dataset/Zhongshan Dataset 2023.1.12/video2pic/11"
    time_interval = 1
    video2frame(video_path, frames_save_path, time_interval)

    # # 多个视频裁剪
    # sourceDir = "D:/CS dataset/Zhongshan Dataset 2023.1.12/video"
    # frames_save_path = "D:/CS dataset/Zhongshan Dataset 2023.1.12/video2pic"
    # time_interval = 1
    # for sRoot, sDirs, sFiles in os.walk(sourceDir):
    #     break
    # num = 0   # num = 0
    # for sourceName in sFiles:
    #     sourceFile = sourceDir + '\\' + sourceName
    #     print(sourceName)
    #     # 每个视频创建对应一个文件夹
    #     isExists = os.path.exists(frames_save_path + "\\" + str(num + 1))
    #     if not isExists:
    #         os.makedirs(frames_save_path + "\\" + str(num + 1))
    #         frames_save_path_final = frames_save_path + "\\" + str(num + 1)
    #         num += 1
    #         # print(frames_save_path_final)
    #     video2frame(sourceFile, frames_save_path_final, time_interval)