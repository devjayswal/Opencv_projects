"""
 This file have funtionality of  record  screen  using opencv  

"""


import numpy as np
import cv2
import pyautogui as pag

# Taking resolution
rs = pag.size()

# Taking Input path
fn = input("Please enter file name")
fps = 20.0

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter(fn, fourcc, fps, rs)


#Creating Recording module

cv2.namedWindow("Live_Screen_captureing",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live_Screen_captureing", (600,400))

while True:
    img = pag.screenshot()
    f = np.array(img)
    f = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)
    output.write(f)
    cv2.imshow("Live_Screen_captureing", f)
    if cv2.waitKey(1) & 0xFF == 27:
        break

output.release()
cv2.destroyAllWindows()