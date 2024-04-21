"""
功能：裁剪视频尺寸
"""
import cv2
cap=cv2.VideoCapture("D:/Baiduyun Download/Motrix Download/video.mp4")
#获取视频参数
width=cap.get(3)
high=cap.get(4)
fps=cap.get(5)

# size=(int(width/2),int(high))
size=(300,300)
#定义编解码器并创建VideoWriter对象
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('D:/Baiduyun Download/Motrix Download/cut video/video.mp4v',fourcc,fps,size)

while(cap.isOpened()):
    ret,frame=cap.read()
    # target=frame[0:int(high),int(width/4):int(width/2+width/4)]    #注意这里是高宽
    target = frame[0:300, 500:800]  # 注意这里是高宽
    out.write(target)

    # cv2.imshow("frame_src",frame)
    # cv2.imshow("frame",target)
    # k=cv2.waitKey(1)
    # if(k==ord('q')):	#退出播放并停止采集
    #     break
print("视频裁剪完成")
print("原视频尺寸："+str(int(width))+'*'+str(int(high)))
print("裁剪后尺寸："+str(int(width/2))+'*'+str(int(high)))
cv2.destroyAllWindows()
cap.release()
out.release()

