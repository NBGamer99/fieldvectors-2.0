import processing_py
# from  import position
from processing_py import *
from math import atan2
from time import sleep


arr = []
arrwd = 10
arrwlen = 5
width = 1000
height = 1000

app = App(width, height)  # create window: width, height
# app.frameRate()


class Arrow:

    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length

    def update(self):
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
        # app.close()
        app.popMatrix()


def draw():
    for i in range(0, arrwd):
        for j in range(0, arrwd):
            arr.append(Arrow(i*width/arrwd, j*height/arrwd, arrwlen))

    # print(arr)
    for k in range(0, len(arr)):
        app.fill(255, 0, 0)
        arr[k].update()

    #  while(k < len(arr)):
    #     k += 1
    #     app.fill(255, 0, 0)
    #     arr[k].update()


while True:
    app.background(0)
    draw()
    app.redraw()


# def mousePressed():
#     global mX,mY
#     mX = mouseX
#     mY = mouseY
