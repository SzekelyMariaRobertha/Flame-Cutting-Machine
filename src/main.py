from typing import NamedTuple
import turtle as tur
from turtle import *


class Segment(NamedTuple):
    shape: str
    initPointX: int
    initPointY: int
    finalpointX: int
    finalpointY: int


class Arc(NamedTuple):
    shape: str
    startX: int
    startY: int
    radius: int
    rotation: float
    endAngle: float


def draw_line(line):
    x = (line.initPointX, line.initPointY)
    y = (line.finalpointX, line.finalpointY)

    tur.penup()
    tur.goto(x)
    tur.pendown()
    tur.goto(y)


def draw_circle(arcc):
    tur.penup()
    tur.goto(arcc.startX, arcc.startY)
    tur.pendown()
    tur.right(arcc.rotation)
    tur.circle(arcc.radius, arcc.endAngle)


def main():
    Screen().setup(width=1360, height=700, startx=0, starty=0)
    tur.bgpic("metal.png")
    tur.title("Flame Cutting Machine")
    tur.pencolor("red")
    tur.shape("circle")
    tur.hideturtle()
    tur.speed(1)
    tur.width(5)

    file1 = open("car.txt", "r")
    lines = file1.readlines()
    for line in lines:
        if line.strip():
            s = line.split("=")

            if s[0].__contains__("segment"):
                coords = s[1].split(",")

                startX = int(coords[0])
                startY = int(coords[1])
                endX = int(coords[2])
                endY = int(coords[3])

                segment = Segment(s[0], startX, startY, endX, endY)

                if (startX < -680) or (startX > 680) or (startY < -350) or (startY > 350) or (endX < -680) or (endX > 680) or (endY < -350) or (endY > 350):
                    print("Shape out of window. Please check coordinates for", segment)
                    exit(0)
                else:
                    draw_line(segment)

            else:
                coords = s[1].split(",")
                arc = Arc(s[0], int(coords[0]), int(coords[1]), int(coords[2]), float(coords[3]), float(coords[4]))
                draw_circle(arc)

                position = tur.pos()
                if (position[0] < -680) or (position[0] > 680) or (position[1] < -350) or (position[1] > 350):
                    print("Shape out of window. Please check angle for", arc)
                    exit(0)


if __name__ == "__main__":
    main()
