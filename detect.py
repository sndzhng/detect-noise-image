from PIL import Image
from statistics import mean
from math import floor

# load image and extract rgb as a list
img = Image.open("noise-image.png")
width, height = img.size
pixel_values = list(img.getdata())

# reverse for below logic
pixel_values.reverse()

# create nested list for devide list for each horizontal pixels
pixel_nested_list = []
i = 0
while i < len(pixel_values):
    pixel_nested_list.append(pixel_values[i:i+width])
    i += width

# get index list of highest grayscale pixel in each horizontal pixels
last_highest_indexs = []
for a_row_pixel in pixel_nested_list:
    last_highest_index = 0
    for pixel_index, pixel_grayscale in enumerate(a_row_pixel):
        if pixel_grayscale[0] == 255:
            last_highest_index = pixel_index
    last_highest_indexs.append(last_highest_index)

# get first lowest grayscale index list that behide highest in each horizontal pixels
first_lowest_indexs = []
for index, a_row_pixel in enumerate(pixel_nested_list):
    first_lowest_index = 0
    lowest_grayscale = 255
    for pixel_index, pixel_grayscale in enumerate(a_row_pixel[last_highest_indexs[index]:]):
        if pixel_grayscale[0] <= lowest_grayscale:
            lowest_grayscale = pixel_grayscale[0]
            first_lowest_index = last_highest_indexs[index] + pixel_index
        else:
            break
    first_lowest_indexs.append(first_lowest_index)

# reverse index back
first_highest_indexs = []
for value in last_highest_indexs:
    first_highest_indexs.append(width - value)
last_lowest_indexs = []
for value in first_lowest_indexs:
    last_lowest_indexs.append(width - value)

# calculate and conclude (+1 for turn index to pixel)
average_highest_pixel = floor(mean(first_highest_indexs)) + 1
average_lowest_pixel = floor(mean(last_lowest_indexs)) + 1
average_changing_pixel = floor(
    (average_highest_pixel + average_lowest_pixel)/2) + 1

print("Total horizontal pixel:", width)
print("Average highest grayscale pixel: ", average_highest_pixel)
print("Average lowest grayscale pixel: ", average_lowest_pixel)
print("Average grayscale changed pixel: ", average_changing_pixel)
