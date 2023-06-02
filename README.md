# HandTracking
* 手部识别（基于单目摄像头）

###  2022.3.12 （12:00-18:15）  

* 此仓库中涉及单目摄像头距离检测，调用numpy中的拟合方法，将像素单位换算成厘米单位，使用多项式进行拟合。


- [x] 单目摄像头手部距离识别
- [x] 针对不同用户手部大小不一致导致距离识别不精准的问题，加入手动调参功能
- [ ] 摄像头畸变导致测距不准尚未解决
- [ ] 摄像头标定流程说明尚未完善

### 文件说明
* HandDistance-main.py中使用numpy进行二阶多项式进行拟合

* ```HandTrackingMin.py```为‘最轻量化’的手部识别代码

* ```HandTrackingModul.py```是将HandTrackingMin.py转换打包成模块，以方便其他时候使用import HandTrackingModule as htm来调用，但其实本质上是cvzone里面的一部分

* 从HandDistance的```main.py```的代码```from cvzone.HandTrackingModule import HandDetector```中发现，原作者是将代码创建为一个class，在最后面def main()，然后加上
  ```bash
  if __name__ == "__main__":
  	main()
  ```
  从而实现在其他代码里面使用import来访问```HandTrackingModule```的效果
  
* ```VolumeHandControl.py```核心是用```mediapipe```检测出手的位置，然后根据```hand_landmarks.png```中选择21个点关键点中需要的关键点，通过计算两点之间的距离
$d = \sqrt{X^{2}+Y^{2}}$将结果导入pycaw（一个控制windows电脑声音大小的模块），默认值是（-65.25到0），对于windows电脑的0-100音量，所以使用了```numpy.interp```进行归一化处理，最终达到调声音的效果。
