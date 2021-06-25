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
    

def main():
    temp = get_files()
    starting = dict()
    for i in range(5):
        starting[str(i+1)] = picture(temp[i])
        starting[str(i+1)].give_info()
    for i in starting:
        starting[i].give_info()



if __name__ == "__main__":
	main()