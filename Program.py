from math import sqrt
import matplotlib.pyplot as plt
from K import Kmeans 
from K import Node
# x axis values
x = [0.3]
# corresponding y axis values
y = [0.1]
colors={'pink':[],'blue':[],'red':[]}
color=['pink','blue','red']

K=Kmeans.KmeansFunction()
#K.AddPoints(3)
# K.WriteTofile()
K.GetFromFile()
Kposx,Kposy = K.GetPoints()

Moduels=[]
def CalcuateDistance(x1,y1,x2,y2):
        #√((x2 – x1)² + (y2 – y1)²)
        val=(x2-x1)**2 + (y2-y1)**2
        if(val<0):
            val*=-1
        return sqrt(val)

def Compare(x1,y1):        
    Dist=[]
    for i in range(len(Kposx)):
        dis=CalcuateDistance(Kposx[i],Kposy[i],x1,y1)
        Dist.append(dis)
    index=0
    print(Dist,"this is Dist")
    for i in range(len(Dist)):
            
        if(Dist[index]>Dist[i]):
            print(index,Dist[index],Dist[i])
            index=i
    print(Dist[index],"this is the winner")
    return color[index]


with open('input.txt') as r:
    for i in r:
        values=i.split(',')
        Xval=float(values[0].strip())
        Yval=float(values[1].strip())
        x.append(Xval)
        y.append(Yval)
        colors[Compare(Xval,Yval)].append([Xval,Yval])
            


for i in Moduels:
    index=color[i.Compare(Kposx,Kposx)]
    colors[index].append([i.GetX,i.GetY])

# plotting the points 


i=0
for key in colors:
    plt.scatter(Kposx[i], Kposy[i], label= "circle", color= key, 
                s=100)
    i+=1

#plt.scatter(x, y, label= "circle", color= "green", s=30)


for key,val in colors.items():
    for j in val:
        plt.scatter(j[0], j[1], label= "circle", color=key, s=30)



 












plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('K-maens')
plt.show()