import cv2
import os
import sys
from random import randint

os.system("cls")
print("\033[?25l", end="")

frame_ctr = 0
fps = 0


def array_printer(arr):
    for x in arr:
        print(*x, sep="")


frame = cv2.imread("me_3.jpg")

video_width = frame.shape[1]
video_height = frame.shape[0]

letter_width = 9
letter_height = 20

############################# Window Dimensions #############################
# print(sys.argv[0])
if len(sys.argv) > 1:
    ascii_width = int(sys.argv[1])
else:
    ascii_width = 180
############################# Window Dimensions #############################
ascii_height = int(
    ascii_width * (video_height / video_width) * (letter_width / letter_height)
)

brt_max = 256
# brt_str = "     .,^*!#@$%"
# brt_str = R"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'."


brt_str = R"""$@BM#*o/\f|()1{}[]?-_+i!lI;:,"^`'.       """
brt_str = brt_str[::-1]


brt_len = len(brt_str)
os.system(f"mode con: cols={ascii_width} lines={ascii_height+5}")

os.system("cls")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

gray_resized = cv2.resize(gray, (ascii_width, ascii_height))
# gray_resized = cv2.flip(gray_resized, 1)

cv2.imshow("cap", frame)
# print(gray_resized[0][0])

# ascii_out = [
#     [brt_str[item * brt_len // brt_max] for item in elem] for elem in gray_resized
# ]
os.system(f"mode con: cols={ascii_width} lines={ascii_height+2}")

for j in range(ascii_height):
    for i in range(ascii_width):
        index = gray_resized[j][i] * brt_len // brt_max
        print(brt_str[index], end="")
    print("")
# print(f"height = {len(ascii_out)}, width = {len(ascii_out[0])}")
# array_printer(ascii_out)


# Destroy all the windows
cv2.destroyAllWindows()
