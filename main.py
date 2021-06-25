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
    '''
    the following if else statements calculate the percentage of how far off the rgb values are
    from the average rgb values, they then print this to the screen
    
    '''
    
    if pic.average[0] > a_t.average[0]:
        r_percent = (temp_margin.r_error[0]-(pic.average[0]-a_t.average[0]))/temp_margin.r_error[0]*100
    else:
        r_percent = pic.average[0]/temp_margin.r_error[1]*100
        
        
        
    if pic.average[1] > a_t.average[1]:
        g_percent = (temp_margin.g_error[0]-(pic.average[1]-a_t.average[1]))/temp_margin.g_error[0]*100
    else:
        g_percent = pic.average[1]/temp_margin.g_error[1]*100
        
        
        
    if pic.average[2] > a_t.average[2]:
        b_percent = (temp_margin.b_error[0]-(pic.average[2]-a_t.average[2]))/temp_margin.b_error[0]*100
    else:
        b_percent = pic.average[2]/temp_margin.b_error[1]*100
        
    '''
    The next three if statements are for if one of the rgb values is outside of the minimum and/or maximum
    values which are a part of the average_type
    '''
        
    if pic.average[0] > a_t.maximum[0] or pic.average[0] < a_t.minimum[0]:
        print("Warning, \"r\" value maximum/minium dependencies not met")
    
    if pic.average[1] > a_t.maximum[1] or pic.average[1] < a_t.minimum[1]:
        print("Warning, \"g\" value maximum/minium dependencies not met")
        
    if pic.average[2] > a_t.maximum[2] or pic.average[2] < a_t.minimum[2]:
        print("Warning, \"b\" value maximum/minium dependencies not met")
    
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
