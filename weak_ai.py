


class average_type:

    def __init__(self, 
                    rgb, #this will be a dictionary which holds the average rgb values for each picture 
                    name): #the name is the type of picture i.e. "iron", or "Gold"
        self.name = name
        self.rgb = rgb
        self.length = len(rgb)
        
        rs, gs, bs = 0,0,0
        
        for i in self.rgb:
            rs+= self.rgb[i][0]
            gs+= self.rgb[i][1]
            bs+= self.rgb[i][2]
            
        self.average = [rs/self.length, gs/self.length, bs/self.length] #this is the gross average, not the most accurate
        
        rs, gs, bs = 0,0,0
        #this is to get a maximum from the values
        for i in self.rgb:
            if self.rgb[i][0] > rs:
                rs = self.rgb[i][0]
            if self.rgb[i][0] > gs:
                gs = self.rgb[i][0]
            if self.rgb[i][0] > bs:
                bs = self.rgb[i][0]
        self.maximum = [rs, gs, bs]
                
        rs, gs, bs = 255, 255, 255        
        #this is to get a minimum from the values
        for i in self.rgb:
            if self.rgb[i][0] < rs:
                rs = self.rgb[i][0]
            if self.rgb[i][0] < gs:
                gs = self.rgb[i][0]
            if self.rgb[i][0] < bs:
                bs = self.rgb[i][0]
        self.minimum = [rs, gs, bs]
        
        '''
        Now we have a loose average, a minnimum, a maximum, and the raw data all stored in one.
        
        '''

        