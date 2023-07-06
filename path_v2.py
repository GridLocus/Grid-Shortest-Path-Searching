import matplotlib.pyplot as plt
import random




collision = []


fourAngle = [[0, 0], [0, 30], [30, 0], [30, 30]]
plt.plot([fourAngle[0][0], fourAngle[1][0]], [fourAngle[0][1], fourAngle[1][1]], color="black")
plt.plot([fourAngle[0][0], fourAngle[2][0]], [fourAngle[0][1], fourAngle[2][1]], color="black")
plt.plot([fourAngle[2][0], fourAngle[3][0]], [fourAngle[2][1], fourAngle[3][1]], color="black")
plt.plot([fourAngle[1][0], fourAngle[3][0]], [fourAngle[1][1], fourAngle[3][1]], color="black")

obstacle = [[[3, 28], [13, 28], [3, 23], [13, 23]], [[17, 20], [20, 20], [17, 17], [20, 17]], [[24, 26], [28, 26], [24, 14], [28, 14]], [[5, 15], [15, 15], [5, 3], [15, 3]], [[20, 10], [27, 10], [20, 4], [27, 4]]]


for a in obstacle:
    if a[0][0] > a[1][0]:
        x1 = a[1][0]
        x2 = a[0][0]
    else:
        x1 = a[0][0]
        x2 = a[1][0]
        
    if a[1][1] > a[2][1]:
        y1 = a[1][1]
        y2 = a[2][1]
    else:
        y1 = a[2][1]
        y2 = a[1][1]
        
    collision.append([x1, x2, y1, y2])
    

def Crash(coorX, coorY):
    # reuturn True of not crash
    global collision
    print("obstacle", obstacle)
    print("CoorXY", coorX, coorY)
    
    for a in collision:
        print("collision", collision)
        if (coorX <= a[1] and coorX >= a[0] and coorY <= a[2] and coorY >= a[3]) or (coorX <= 0 or coorX >= 30 or coorY <= 0 or coorY >= 30):
            #print("Hit")
            return False
        else:
            continue
            #print("OK")
            
    return True



startOK = "False"
endOK = "False"

while True:
    startPointX = random.randint(0, 30)
    startPointY = random.randint(0, 30)
    startOK = Crash(startPointX, startPointY)
    if startOK == True:
        break

startPoint = [startPointX, startPointY]



while True:
    endPointX = random.randint(0, 30)
    endPointY = random.randint(0, 30)
    endOK = Crash(endPointX, endPointY)
    if endOK == True:
        break
    
endPoint = [endPointX, endPointY]

#startPointX = 1
#startPointY = 29
#endPointX = 28
#endPointY = 7
startPoint = [startPointX, startPointY]
endPoint = [endPointX, endPointY]

plt.scatter(startPointX, startPointY, s=100)
plt.scatter(endPointX, endPointY)


print("obstacle", obstacle)
    
for i in obstacle:
    plt.plot([i[0][0], i[1][0]], [i[0][1], i[1][1]], color="red")
    plt.plot([i[0][0], i[2][0]], [i[0][1], i[2][1]], color="red")
    plt.plot([i[2][0], i[3][0]], [i[2][1], i[3][1]], color="red")
    plt.plot([i[1][0], i[3][0]], [i[1][1], i[3][1]], color="red")
    



###################################################################################################
###### Find Path ######
#######################
###### (x1, y1)-----------(?, ?)    ######
###### |                       |    ######
###### |                       |    ######
###### |                       |    ######
###### |                       |    ######
###### |                       |    ######
###### |                       |    ######
###### |                       |    ######
###### (?, ?)-----------(x2, y2)    ######
##########################################

hited = "False"
visited = []
path = [[startPoint.copy()]]

        

def canBranch():
    global path
    global visited
    new = []
    
    for a in path:
        #print("a", a)
        
        #print("canBranch1")
        #print("visited", visited)
        #print("p", [a[len(a)-1][0] + 1, a[len(a)-1][1]])
        if [a[len(a)-1][0] + 1, a[len(a)-1][1]] not in visited:
            if Crash(a[len(a)-1][0] + 1, a[len(a)-1][1]) == True:
                t = a.copy()
                t.append([a[len(a)-1][0] + 1, a[len(a)-1][1]])
                new.append(t)
                visited.append([a[len(a)-1][0] + 1, a[len(a)-1][1]])
        
        #print("canBranch2")
        if [a[len(a)-1][0] - 1, a[len(a)-1][1]] not in visited:
            if Crash(a[len(a)-1][0] - 1, a[len(a)-1][1]) == True:
                t = a.copy()
                t.append([a[len(a)-1][0] - 1, a[len(a)-1][1]])
                new.append(t)
                visited.append([a[len(a)-1][0] - 1, a[len(a)-1][1]])
        
        #print("canBranch3")
        if [a[len(a)-1][0], a[len(a)-1][1] + 1] not in visited:
            if Crash(a[len(a)-1][0], a[len(a)-1][1] + 1) == True:
                t = a.copy()
                t.append([a[len(a)-1][0], a[len(a)-1][1] + 1])
                new.append(t)
                visited.append([a[len(a)-1][0], a[len(a)-1][1] + 1])
        
        #print("canBranch4")
        if [a[len(a)-1][0], a[len(a)-1][1] - 1] not in visited:
           if Crash(a[len(a)-1][0], a[len(a)-1][1] - 1) == True:
               t = a.copy()
               t.append([a[len(a)-1][0], a[len(a)-1][1] - 1])
               new.append(t)
               visited.append([a[len(a)-1][0], a[len(a)-1][1] - 1])
               
        #print("new", new)
    #print("path", path)          
    path = new.copy()
    
    
def hitTarget():
    #print("CheckHitTarget")
    
    global path
    #print("path", path)
    if path == []:
        return True
    for a in path:
        #print("a", a)
        #print("Point", a[len(a)-1][0], a[len(a)-1][1])
        if a[len(a)-1][0] == endPoint[0] and a[len(a)-1][1] == endPoint[1]:
            print("Hit!")
            return a
        else:
            print("Not Hit")
            continue          
    return False


while True:
    #print("Loop")
    #print(hited)
    canBranch()
    hited = hitTarget()
    #print("path", path)
    
    if hited != False:
        print("result", hited)
        break
    
    
for i in range(len(hited)-1):
    plt.plot([hited[i][0], hited[i+1][0]], [hited[i][1], hited[i+1][1]], color='orange')

plt.show()






    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




 