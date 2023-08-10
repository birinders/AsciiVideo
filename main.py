import cv2
import os
import sys
import colorama
from random import randint

os.system("cls")
print("\033[?25l", end="")

colorama.init()

import time

## 6x16 or 8x18

frame_ctr = 0
fps = 0


def move(y, x):
    print("\033[%d;%dH" % (y, x))


def array_printer(arr):
    for x in arr:
        print(*x, sep="")
    # for x in arr:
    #     print("\033[A")
    # print("\033[F")


arr = [[1, 2, 3], [4, 5, 6]]
# array_printer(arr)

try:
    video_capture = cv2.VideoCapture(1)
    ret, frame = video_capture.read()

except cv2.error as e:
    video_capture = cv2.VideoCapture(0)

video_width = frame.shape[1]
video_height = frame.shape[0]

letter_width = 10
letter_height = 20

############################# Window Dimensions #############################
# print(sys.argv[0])
if len(sys.argv) > 1:
    ascii_width = int(sys.argv[1])
else:
    ascii_width = 120
############################# Window Dimensions #############################


ascii_height = int(
    ascii_width * (video_height / video_width) * (letter_width / letter_height)
)
# print(ascii_height)

brt_max = 256
# brt_str = "     .,^*!#@$%"
# brt_str = R"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'."


brt_str = R"""$@BM#*o/\f|()1{}[]?-_+i!lI;:,"^`'.                  """
brt_str = brt_str[::-1]


# brt_str = " █"


brt_len = len(brt_str)
os.system(f"mode con: cols={ascii_width} lines={ascii_height+5}")

# print(frame.shape)

start_time = time.time()

while True:
    move(0, 0)
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray_resized = cv2.resize(gray, (ascii_width, ascii_height))
    # gray_resized = cv2.flip(gray_resized, 1)

    cv2.imshow("cap", frame)
    # print(gray_resized[0][0])

    # ascii_out = [
    #     [brt_str[item * brt_len // brt_max] for item in elem] for elem in gray_resized
    # ]

    for j in range(ascii_height):
        for i in range(ascii_width):
            index = gray_resized[j][i] * brt_len // brt_max
            print(brt_str[index], end="")
        print("")
    # print(f"height = {len(ascii_out)}, width = {len(ascii_out[0])}")
    # array_printer(ascii_out)

    print(f"\n\n{fps} FPS")

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    frame_ctr += 1
    cur_time = time.time()
    if cur_time - start_time > 1:
        fps = frame_ctr
        frame_ctr = 0
        start_time = time.time()
        if randint(0, 200) < 10:
            os.system("cls")


video_capture.release()
# Destroy all the windows
cv2.destroyAllWindows()
# print("hello")
