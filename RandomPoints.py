#f = open("input.txt", "x")
import random
class FileManger():
    def __init__(self,filename,range,length):
        self.filename=filename    
        self.randominput = ''
        self.Range=range
        self.length=length

    def AddInput(self,startingX,endingX,startingY,endingY):
        x=round(random.uniform(startingX, endingX), 2)
        y=round(random.uniform(startingY, endingY), 2)
        self.randominput+=str(x)+','+str(y)+'\n'




    def MakeRandominput(self):
        for i in range (self.Range):
            self.AddInput(0.00,self.length,0.00,self.length)

    def MakeRandomClusters(self,Count):
        Interval=round(self.Range/Count)
        Start=0
        for i in range(Count):
            for j in range(Interval):
                self.AddInput(Start,Start+Interval,0.00,self.length-20)
            Start+=Interval#+20

    def MakeClusters(self,Count):
        Interval=round(self.Range/Count)
        Start=0
        for i in range(Count):
            for j in range(Interval):
                self.AddInput(Start,Start+Interval,Start,Start+Interval)
            Start+=Interval


    def AddtoFile(self):
        f=open(self.filename,'w')
        f.write(self.randominput)
        f.close()


a=FileManger('input.txt',100,100.00)
#a.MakeRandominput()
#a.MakeClusters(4)
a.MakeRandomClusters(3)
a.AddtoFile()