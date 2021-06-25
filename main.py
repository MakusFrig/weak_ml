from PIL import Image
from setup import *
from weak_ai import *
import os

def get_files():
    temp = []
    for i in os.listdir():
        if i[0:5] == "image":
            temp.append(i.split(".")[0])
    return temp
    
def test(pic, a_t): #a type picture and a type average_type
    temp_margin = error_margin(a_t.average)
    if pic.average[0] > a_t.average[0]:
        r_percent = (temp_margin.r_error[0]-(pic.average[0]-a_t.average[0]))/temp_margin.r_error[0]
    else:
        r_percent = pic.average[0]/temp_margin.r_error[1]
        
        
        
    if pic.average[1] > a_t.average[1]:
        g_percent = (temp_margin.g_error[0]-(pic.average[1]-a_t.average[1]))/temp_margin.g_error[0]
    else:
        g_percent = pic.average[1]/temp_margin.g_error[1]
        
        
        
    if pic.average[2] > a_t.average[2]:
        b_percent = (temp_margin.b_error[0]-(pic.average[2]-a_t.average[2]))/temp_margin.b_error[0]
    else:
        b_percent = pic.average[2]/temp_margin.b_error[1]
    print(r_percent, g_percent, b_percent)

def main():
    temp = get_files()
    starting = dict()
    for i in range(5):
        starting[str(i+1)] = picture(temp[i])
    for i in starting:
        starting[i].give_info()
        
    iron = average_type(starting, "iron")
    test_image = picture("test_image")
    iron.give_info()
    test_image.give_info()
    test(test_image, iron)
    
    
    test_image2 = picture("test_image2")
    test_image2.give_info()
    test(test_image2, iron)



if __name__ == "__main__":
	main()
