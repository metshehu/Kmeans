import random

class KmeansFunction():
    def __init__(self):
        self.x=[]
        self.y=[]
        self.FileForm=''
    def AddPoints(self,count):
        for i in range(count):
            Xval=round(random.uniform(0.00, 100.0), 2)
            Yval=round(random.uniform(0.00, 100.0), 2)

            self.x.append(Xval)
            self.y.append(Yval)

            self.FileForm+=str(Xval)+','+str(Yval)+'\n'
    def GetPoints(self):
        return self.x,self.y
    
    def GetFromFile(self):
        with open("KPos.txt","r") as Ks:
            for i in Ks:
                values=i.split(',')
                self.x.append(float(values[0].strip()))
                self.y.append(float(values[1].strip()))
        print(self.x,"-",self.y)
    
    def WriteTofile(self):
        f=open("KPos.txt",'w')
        f.write(self.FileForm)
        f.close()