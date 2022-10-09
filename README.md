# HandTracking
#手部识别（基于单目摄像头）

## 2022.3.12 （12.00-18.15）  
* 1.本文件中包含单目摄像头距离检测，原理是将像素值换算成厘米，具体使用了numpy里面的拟合方法，给定一堆x的值和一堆y的值可以实现对多项式的拟合。HandDistance-main.py中使用numpy进行二阶多项式进行拟合
* 2.HandTrackingMin.py是‘最轻量化’的手部识别代码
* 3.HandTrackingModul.py是将HandTrackingMin.py转换打包成模块，以方便其他时候使用import HandTrackingModule as htm来调用，但其实本质上是cvzone里面的一部分
* 4.从HandDistance的main.py的代码中不难发现，from cvzone.HandTrackingModule import HandDetector，名字与3是一样的，其实原作者是将代码创建为一个class（类），在最后面def（定义）main，然后加上
if __name__ == "__main__":
    main()
从而实现在其他代码里面使用import来访问HandTrackingModule的效果
* 5.volumeHandControl核心是用mediapipe检测出手的位置，然后根据hand_landmarks中选择21个点中需要的点，通过计算两点之间的距离d=根号（x^2+y^2）得出距离，然后引入pycaw（一个控制windows电脑声音大小的模块），默认值是（-65.25到0），对于windows电脑的0-100音量，所以使用了numpy.interp进行归一化处理，最终达到调声音的效果。
