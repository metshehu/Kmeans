from math import sqrt
import matplotlib.pyplot as pltt
from K import Kmeans 
from matplotlib.widgets import Slider, Button


LEARNINGRATE=0.01

# x axis values
x = []
# corresponding y axis values
y = []
c=[]
colors={'pink':[],'blue':[],'red':[]}#,'yellow':[],'green':[],'orange':[]}
GRUPINGS=len(colors)

color=[]

for key,val in colors.items():
    color.append(key)


nodes=[]

K=Kmeans.KmeansFunction()
K.AddPoints(GRUPINGS)
K.WriteTofile()
#K.GetFromFile()
Kposx,Kposy = K.GetPoints()

plt ,ax = pltt.subplots()

with open('input.txt') as r:
    for i in r:
        values=i.split(',')
        Xval=float(values[0].strip())
        Yval=float(values[1].strip())
        x.append(Xval)
        y.append(Yval)
def CacluteDistance1Poit(x1,x2):
    return (x2-x1)
def CalcuateDistance(x1,y1,x2,y2):
        #√((x2 – x1)² + (y2 – y1)²)
        val=(x2-x1)**2 + (y2-y1)**2
        return sqrt(val)



def ShortestDistence(values):
    index=0
    for i in range(GRUPINGS):
        if(values[index]>values[i]):
            index=i
    return color[index]

def Compare(x1,y1):        
    Dist=[]
    for i in range(GRUPINGS):
        dis=CalcuateDistance(Kposx[i],Kposy[i],x1,y1)
        Dist.append(dis)
    return ShortestDistence(Dist)

def UpdateNodeColors():
    global Kposx,Kposy
    for key in colors:
        colors[key]=[]
    ResetValues()
    for i in range(len(nodes)):
        nodes[i].set_color(c[i])


def UpdateKPos():
    i =0
    for i in range(GRUPINGS):
        val=colors[color[i]]
        
        for j in val:
            Kposx[i]-=LEARNINGRATE * (CacluteDistance1Poit(j[0],Kposx[i]))
            Kposy[i]-=LEARNINGRATE * (CacluteDistance1Poit(j[1],Kposy[i]))
        i+=1    




def ResetValues():
    global c 
    c=[]
    for i in range(len(x)):
        colorChosen=Compare(x[i],y[i])
        colors[colorChosen].append([x[i],y[i]])
        c.append(colorChosen)



def AddTo():
    ResetValues()
    global Kposx,Kposy
    #Perecnte=len(x)/10/GRUPINGS
    #for key,val in colors.items():
     #   if(len(val)<Perecnte):
      #      print(key,val)
       #     colors['blue']=[]
        #    colors['red']=[]
         #   colors['pink']=[]
          #  K.Delet()
           # K.AddPoints(3)
            #K.WriteTofile()
            #Kposx,Kposy = K.GetPoints()
            #AddTo()
    
AddTo()

def update(val):
    UpdateKPos()
    UpdateNodeColors()
    Kslider.set_offsets(list(zip(Kposx, Kposy)))
    plt.canvas.draw_idle()



# plotting the points 


Kslider =ax.scatter(Kposx, Kposy, label= "circle", color= color, marker='s',s=100)
#plt.scatter(x, y, label= "circle", color= "green", s=30)
for i in range(len(x)):
    nodes.append(ax.scatter(x[i], y[i], label= "circle", color=c[i], s=30))


plt.subplots_adjust(bottom=0.25)
slider_ax = pltt.axes([0.15, 0.1, 0.65, 0.03])
slider = Slider(slider_ax, 'Size', 1, 100, valinit=0)



slider.on_changed(update)
pltt.xlabel('x - axis')
pltt.ylabel('y - axis')
pltt.title('K-maens')
pltt.show()
