import SKit
import cv2
image = cv2.imread('./test.png')
kill_lib=SKit.Kit()

res=kill_lib.detect(input_array=image)
print(res)