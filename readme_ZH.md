# [switch to english](./readme.md)
# 使用前提
1. python>=3.10 需安装opencv-python,因为参数是ndarray类型的图像，也提供了另外一个不需要安装opencv-python的库[detect](https://github.com/2991535823/sgs_kill),你可以选择喜欢的图像处理库将待检测图像保存为文件后再调用```detect.kill()```
```python
import detect
# results = detect.kill("C:/Users/Fox/Documents/demo_project/py_c/test.png")
results = detect.kill("./test.png",0.65)
print(results)
#[b'wind', b'down', b'up', b'wind']
```
# 如何使用
1. 安装SKit库，安装命令```pip install .\SKit-1.0-cp310-cp310-win_amd64.whl```
2. 在需要的地方导入该库，使用示例见[main.py](./main.py)
```python
import SKit
import cv2
image = cv2.imread('./test.png')
kill_lib=SKit.Kit()

res=kill_lib.detect(input_array=image)
print(res)
#['wind', 'down', 'up', 'wind']
```
# 如何获取
1. 旧版直接[仓库](https://github.com/2991535823/sgs_kill)内下载获取
2. 新版加入QQ频道:pd33796681