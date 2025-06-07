# [切换到中文](./readme_ZH.md)
# Prerequisites  
1. Python>=3.10 with opencv-python installed, since the parameters expect ndarray-type images. An alternative library [detect](https://github.com/2991535823/sgs_kill) without opencv-python dependency is also available. You may use any preferred image processing library to save the target image as a file before calling ```detect.kill()```  

```python
import detect
# results = detect.kill("C:/Users/Fox/Documents/demo_project/py_c/test.png")
results = detect.kill("./test.png", 0.65)
print(results)
# [b'wind', b'down', b'up', b'wind']
```
# How to Use
1. Install SKit library using: ```pip install .\SKit-1.0-cp310-cp310-win_amd64.whl```

2. Import the library where needed. See example in main.py:

```python
import SKit
import cv2

image = cv2.imread('./test.png')
kill_lib = SKit.Kit()

res = kill_lib.detect(input_array=image)
print(res)
# ['wind', 'down', 'up', 'wind']
```
# Availability
Download older versions directly from the [repository](https://github.com/2991535823/sgs_kill)

Join QQ channel for newer versions: pd33796681

