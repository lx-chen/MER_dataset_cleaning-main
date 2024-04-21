"""
功能：截取一段短视频
"""
import cv2
import numpy as np

def capture_video(video_path, result_video_path, video, result_video, frame_time):
    """
    功能：截取一段短视频
    参数：
        video_path：需要截取的视频路径
        result_video_path：截取后的视频存放的路径
        video：需要截取的视频的名称（不带后缀）
        result_video：截取了的视频的名称（不带后缀）
        start_time：截取开始时间（单位s）
        end_time：截取结束时间（单位s）
    """
    for i in range(len(frame_time)): # len(frame_time)

        # 读取视频
        cap = cv2.VideoCapture(video_path + video)

        # 读取视频帧率
        fps_video = cap.get(cv2.CAP_PROP_FPS)

        # 设置写入视频的编码格式
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')

        # 获取视频宽度和高度
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # 设置写视频的对象
        result_video = 'invisible' + str(i + 1) + '.mp4'  # change file name here  # result_video = 'invisible' + str(i + 1) + '.mp4'
        videoWriter = cv2.VideoWriter(result_video_path + result_video, fourcc, fps_video, (frame_width, frame_height))
        # 获取frame_time中截取视频的时间点hour、minute、second
        hour = frame_time[i][0]
        minute = frame_time[i][1]
        second = frame_time[i][2]
        start_time = hour * (60 * 60) + minute * 60 + second
        end_time = start_time + 1

        # 初始化一个计数器
        count = 0
        while (cap.isOpened()):
            # # 按帧读取视频里的图片
            ret, frame = cap.read()

            if ret == True:
                # 计数器加一
                count += 1
                # 截取相应时间内的视频信息
                if (count > (start_time * fps_video) and count <= (end_time * fps_video)):
                    # 将图片写入视屏
                    videoWriter.write(frame)
                if (count == (end_time * fps_video)):
                    break
            else:
                # 写入视屏结束
                videoWriter.release()
                break



        # 如果视频没有读取结束
        # if ret == True:
        #     for i in range(len(frame_time)):
        #         # 设置写视频的对象
        #         result_video = 'visible' + str(i + 1) + '.mp4'  # change file name here
        #         videoWriter = cv2.VideoWriter(result_video_path + result_video, fourcc, fps_video, (frame_width, frame_height))
        #         # 获取frame_time中截取视频的时间点hour、minute、second
        #         hour = frame_time[i][0]
        #         minute = frame_time[i][1]
        #         second = frame_time[i][2]
        #         start_time = hour * (60 * 60) + minute * 60 + second
        #         end_time = start_time + 1
        #         # 裁剪视频
        #         # 计数器加一
        #         count += 1
        #         # 截取相应时间内的视频信息
        #         if (count > (start_time * fps_video) and count <= (end_time * fps_video)):
        #             # 将图片写入视屏
        #             videoWriter.write(frame)
        #         if (count == (end_time * fps_video)):
        #             break
        # else:
        #     # 写入视屏结束
        #     videoWriter.release()
        #     break



    # while (cap.isOpened()):
    #
    #     # 按帧读取视频里的图片
    #     ret, frame = cap.read()
    #
    #     # 如果视频没有读取结束
    #     if ret == True:
    #
    #         # 计数器加一
    #         count += 1
    #
    #         # 截取相应时间内的视频信息
    #         if (count > (start_time * fps_video) and count <= (end_time * fps_video)):
    #             # 将图片写入视屏
    #             videoWriter.write(frame)
    #
    #         if (count == (end_time * fps_video)):
    #             break
    #
    #     else:
    #         # 写入视屏结束
    #         videoWriter.release()
    #         break

if __name__ == '__main__':
    video_path = "D:/Baiduyun Download/Motrix Download/Zhongshan Dataset/1.cut video/"
    # result_video_path = "D:/Baiduyun Download/Motrix Download/Zhongshan Dataset/video fragment/visible/"
    result_video_path = "D:/Baiduyun Download/Motrix Download/Zhongshan Dataset/3/visible/"
    video = "video.mp4v"
    result_video = "visible1.mp4"
    # frame_time_visible = np.array([[0,0,0], [0,0,4], [0,0,17], [0,0,25], [0,1,34], [0,1,54], [0,2,7], [0,2,17], [0,8,18], [0,10,10],
    #                        [0,10,11], [0,10,25], [0,10,28], [0,15,51], [0,16,40], [0,17,30], [0,18,46], [0,20,28], [0,21,7], [0,22,36],
    #                        [0,24,13], [0,26,46], [0,26,55], [0,27,34], [0,31,14], [0,31,25], [0,34,11], [0,34,40], [0,35,23], [0,40,6],
    #                        [0,40,30], [0,40,55], [0,41,7], [0,42,46], [0,52,32], [0,52,57], [0,53,34], [0,55,34], [0,55,36], [0,56,7],
    #                        [0, 56, 18], [0, 58, 27], [0, 59, 16], [1, 0, 44], [1, 2, 32], [1, 2, 56], [1, 7, 45], [1, 8, 45], [1, 9, 37], [1, 10, 11],
    #                        [1, 11, 23], [1, 11, 31], [1, 12, 30], [1, 13, 46], [1, 15, 25], [1, 18, 42], [1, 19, 28], [1, 22, 54], [1, 25, 13], [1, 28, 17],
    #                        [1, 28, 44], [1, 33, 3], [1, 33, 35], [1, 34, 29], [1, 35, 10], [1, 36, 22], [1, 40, 51], [1, 41, 36], [1, 44, 6], [1, 44, 25],
    #                        [1, 45, 18], [1, 46, 8], [1, 46, 50], [1, 47, 32], [1, 48, 27], [1, 49, 20], [1, 49, 56], [1, 50, 0], [1, 50, 31], [1, 52, 27],
    #                        [1, 53, 28], [1, 56, 30], [1, 56, 57], [1, 58, 37], [1, 59, 21]
    #                        ])

    frame_time_visible = np.array([[2,8,2], [2,8,20], [2,9,2], [2,12,6], [2,17,17], [2,17,55], [2,18,31], [2,19,52], [2,22,27], [2,23,13],
                                   [2, 24, 31], [2, 25, 8], [2, 26, 39], [2, 29, 36], [2, 30, 24], [2, 31, 26], [2, 31, 59], [2, 33, 6], [2, 34, 56], [2, 37, 22],
                                   [2, 38, 24], [2, 39, 31], [2, 42, 44], [2, 43, 4], [2, 46, 3], [2, 46, 38], [2, 48, 1], [2, 48, 58], [2, 51, 32], [2, 52, 34],
                                   [2, 54, 46], [2, 56, 38], [2, 57, 14], [3, 0, 13], [3, 1, 18], [3, 2, 21], [3, 3, 6], [3, 5, 51], [3, 6, 6], [3, 7, 10],
                                   [3, 8, 42], [3, 10, 1], [3, 10, 53], [3, 11, 17], [3, 14, 1], [3, 15, 7], [3, 18, 35], [3, 21, 11], [3, 22, 15], [3, 23, 15],
                                   [3, 23, 46], [3, 24, 31], [3, 24, 43], [3, 25, 19], [3, 27, 56], [3, 28, 22], [3, 28, 42], [3, 29, 39], [3, 30, 38], [3, 32, 1],
                                   [3, 32, 43],
                                 ])

    # frame_time_invisible = np.array([[0, 8, 15], [0, 8, 30], [0, 8, 38], [0, 8, 47], [0, 8, 50], [0, 8, 51], [0, 8, 53], [0, 8, 56], [0, 9, 0],[0, 9, 8],
    #                                 [0, 9, 11], [0, 9, 14], [0, 9, 22], [0, 9, 28], [0, 9, 39], [0, 10, 27], [0, 10, 30], [0, 23, 43], [0, 25, 15], [0, 30, 36],
    #                                 [0, 36, 3], [0, 37, 35], [0, 37, 36], [0, 37, 56], [0, 38, 12], [0, 38, 16], [0, 38, 17], [0, 38, 34], [0, 38, 38], [0, 38, 40],
    #                                 [0, 38, 41], [0, 38, 42], [0, 38, 44], [0, 38, 46], [0, 38, 49], [0, 38, 52], [0, 39, 6], [0, 39, 21], [0, 39, 24], [0, 39, 26],
    #                                 [0, 44, 19], [0, 51, 38], [0, 59, 33], [1, 1, 7], [1, 4, 17], [1, 4, 31], [1, 7, 1], [1, 20, 35], [1, 25, 22], [1, 25, 26],
    #                                 [1, 25, 33], [1, 25, 34], [1, 25, 41], [1, 25, 45], [1, 26, 6], [1, 26, 48], [1, 28, 31], [1, 38, 9], [1, 39, 29], [1, 39, 33],
    #                                 [1, 39, 37], [1, 39, 46], [1, 40, 8], [1, 50, 55], [1, 51, 4], [1, 56, 0], [1, 56, 4], [1, 57, 26], [2, 2, 15], [2, 2, 58],
    #                                 [2, 5, 42], [2, 5, 55]
    #                                 ])

    frame_time_invisible = np.array([[2, 7, 27], [2, 12, 23], [2, 12, 27], [2, 12, 38], [2, 13, 31], [2, 14, 27], [2, 14, 28], [2, 15, 35], [2, 16, 8], [2, 16, 27],
                                     [2, 17, 52], [2, 18, 36], [2, 18, 50], [2, 20, 11], [2, 24, 37], [2, 27, 40], [2, 27, 53], [2, 44, 28], [2, 45, 47], [2, 52, 55],
                                     [2, 52, 58], [2, 53, 3], [2, 53, 8], [2, 53, 17], [2, 54, 57], [2, 56, 0], [2, 59, 37],[3, 0, 39], [3, 2, 39], [3, 14, 51],
                                     [3, 17, 48], [3, 18, 31], [3, 20, 21], [3, 20, 43], [3, 20, 48], [3, 21, 21], [3, 21, 22], [3, 21, 26], [3, 21, 40], [3, 22, 2],
                                     [3, 22, 6], [3, 22, 25], [3, 22, 26], [3, 22, 29], [3, 22, 35], [3, 23, 5], [3, 23, 9], [3, 23, 18], [3, 23, 21],
                                    ])

    capture_video(video_path, result_video_path, video, result_video, frame_time_visible)
    # 切成帧
    """
    import cv2
    video = "./result/result_test_video.mp4"
    cap = cv2.VideoCapture(video)
    frame_id = 0
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            cv2.imwrite('./2/'+str(frame_id)+'.jpg',frame)
            frame_id+=1
        else:
            cap.release()
    """