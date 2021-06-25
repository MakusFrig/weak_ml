from PIL import Image



def open_file(x):
    try:
        im = Image.open(f'{x}.png', 'r')
    except:
        im = Image.open(f"{x}.jpg", 'r')
    print(im.mode)
    starting_mode = im.mode
    im = im.convert("RGB")

    temp = list(im.getdata())
    temp2 = []
    for i in temp:
        for e in i:
            temp2.append(e)
            
    return temp2


def parse(img):
    temp = []
    temp2 = []
    for i in range(2,len(img), 3):
        temp.append(img[i-2:i+1])
    for i in temp:
        if i != [0, 0, 0] and i != [255, 255, 255]:
            temp2.append(i)
    return temp2

def get_average(img):

    failure = True
    r = []
    g = []
    b = []
    for i in img:
        r.append(i[0])
        g.append(i[1])
        b.append(i[2])
    rs, gs, bs = 0,0,0
    for i in r:
        try:
            rs+=i
        except:
            if failure:
                print(i)
                failure = False
    for i in g:
        gs += i
    for i in b:
        bs += i
    return [int(rs/len(r)), int(gs/len(g)), int(bs/len(b))]

class picture:
    
    def __init__(self, image):
        self.name = image
        print(image)
        self.average = get_average(parse(open_file(image)))
        
    def give_info(self):
        print(f"The average rgb value of {self.name} is {self.average}")
        

