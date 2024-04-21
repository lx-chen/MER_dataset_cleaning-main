import numpy as np
import os

# frame_time = np.array([[0,0,0], [0,0,4], [0,0,17], [0,0,25], [0,1,34], [0,1,54]])
# print(len(frame_time))
# for i in range(len(frame_time)):
#     # 获取frame_time中截取视频的时间点hour、minute、second
#     hour = frame_time[i][0]
#     minute = frame_time[i][1]
#     second = frame_time[i][2]
#     print(hour,minute,second)
#     fileName = 'frame' + str(i) + '.jpg' # change file name here
#     print(fileName)
#
# frame_time_invisible = np.array([[0, 8, 15], [0, 8, 30], [0, 8, 38], [0, 8, 47], [0, 8, 50], [0, 8, 51], [0, 8, 53], [0, 8, 56], [0, 9, 0], [0, 9, 8],
#                         [0, 9, 11], [0, 9, 14], [0, 9, 22], [0, 9, 28], [0, 9, 39], [0, 10, 27], [0, 10, 30], [0, 23, 43], [0, 25, 15], [0, 30 ,36],
#                         [0, 36, 3], [0, 37, 35], [0, 37, 36], [0, 37, 56], [0, 38, 12], [0, 38, 16], [0, 38, 17], [0, 38, 34], [0, 38, 38], [0, 38, 40],
#                         [0, 38, 41], [0, 38, 42], [0, 38, 44], [0, 38, 46], [0, 38, 49], [0, 38, 52], [0, 39, 6], [0, 39, 21], [0, 39, 24], [0, 39, 26],
#                         [0, 44, 19], [0, 51, 38], [0, 59, 33], [1, 1, 7], [1, 4, 17], [1, 4, 31], [1, 7, 1], [1, 20, 35], [1, 25, 22], [1, 25, 26],
#                         [1, 25, 33], [1, 25, 34], [1, 25, 41], [1, 25, 45], [1, 26, 6], [1, 26, 48], [1, 28, 31], [1, 38, 9], [1, 39, 29], [1, 39, 33],
#                         [1, 39, 37], [1, 39, 46], [1, 40, 8], [1, 50, 55], [1, 51, 4], [1, 56, 0], [1, 56, 4], [1, 57, 26], [2, 2, 15], [2, 2, 58],
#                         [2, 5, 42], [2, 5, 55]
#                         ])

sourceDir = "D:/Baiduyun Download/Motrix Download/Zhongshan Dataset/video fragment/invisible"
frames_save_path = "D:/Baiduyun Download/Motrix Download/Zhongshan Dataset/video fragment to frame/invisible"
# 每个视频创建对应一个文件夹
num = 0
for i in range(10):
    isExists = os.path.exists(frames_save_path + "\\"+ str(num + 1))
    if not isExists:
        os.makedirs(frames_save_path + "\\"+ str(num + 1))
        frames_save_path_final = frames_save_path + "\\"+ str(num + 1)
        num += 1
        print(frames_save_path_final)