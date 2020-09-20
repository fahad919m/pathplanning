import math
from vpython import *
import random


def fieldValueCalcuation(position,nObstacle):
    distance = (position - nObstacle[0]).mag
    if(distance >  25 ):
        return 0
    elif(distance <= 25 and distance >15):
        fieldValue = math.log(25/distance)*30
    elif(distance<= 15):
        fieldValue = math.log(15/distance)*30
    return fieldValue


def minimum_cost_function(directionSet,obstacleSet,dt,currentposition,goal):
    totalcost = []

    for d in directionSet:
        fieldcost = 0
        counter = 0
        suggestedStep = currentposition + d
        curcost = sqrt(((suggestedStep.x - goal.x)**2) + (( suggestedStep.y - goal.y)**2))

        for each in obstacleSet:
            counter = counter + 1
            fieldcost = fieldcost + fieldValueCalcuation(suggestedStep,each)
        curcost = curcost + fieldcost
        totalcost.append(curcost)

    dx = totalcost[0]-totalcost[1]
    dy = totalcost[2]-totalcost[3]
    x =  vector(dx , dy, 0)
    newPosition = currentposition - x.norm()*dt
    return newPosition


directionSet = [vector(2, 0, 0), vector(-2, 0, 0), vector(0, 2, 0), vector(0, -2, 0)]
totalObstacles = []

box = box(pos=vector(0, 0, 0), length=1000, height=800, width=0.1, color=color.yellow)
startingPoint = sphere(pos=vector(-300, -400, 0), radius=10, color=color.black , make_trail = True)
goalPoint = sphere(pos=vector(250, 400, 0), radius=10, color=color.green )
goal = vector(250, 400, 0)
dt = 2
i = 1

while ((startingPoint.pos - goal).mag >3):
    rate(50)
    startingPoint.pos = minimum_cost_function(directionSet, totalObstacles, dt, startingPoint.pos, goal)
    i = i + 1
    if ( i % 8 == 1):
        temp5 = cylinder(pos=vector(int(random.uniform(-300, 300)), int(random.uniform(-300, 300)), 0),
                     axis=vector(0, 0, 30), radius=10, color=color.red)
        totalObstacles.append([temp5.pos, temp5.radius])
        i = i+1

