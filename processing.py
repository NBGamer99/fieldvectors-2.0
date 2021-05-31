import processing_py
from processing_py import *
from math import atan2


arr = []
arrwd = 10        #arrow density
arrwlen = 5       #arrow length
width = 1000      #width of the canvas
height = 1000     #heigth of the canvas

app = App(width, height)     # create window: width, height



class Arrow:           #create instanceses of every arrow

    def __init__(self, x, y, length):    #get arrow coordinates
        self.x = x
        self.y = y
        self.length = length

    def update(self):                   #get change of arrows orientation
        angle = atan2(app.mouseY-self.y, app.mouseX-self.x)
        app.pushMatrix()
        app.translate(self.x, self.y)
        app.rotate(angle)
        app.beginShape()
        app.vertex(0, -self.length)
        app.vertex(5*self.length, -self.length)
        app.vertex(5*self.length, -3*self.length)
        app.vertex(9*self.length, 0)
        app.vertex(5*self.length, 3*self.length)
        app.vertex(5*self.length, self.length)
        app.vertex(0, self.length)
        app.endShape(0)
        app.popMatrix()


def draw():
    for i in range(0, arrwd):
        for j in range(0, arrwd):
            arr.append(Arrow(i*width/arrwd, j*height/arrwd, arrwlen))

    for k in range(0, len(arr)):
        app.fill(255, 0, 0)
        arr[k].update()

while True:
    app.background(0)
    draw()
    app.redraw()

