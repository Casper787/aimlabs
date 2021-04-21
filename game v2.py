{\rtf1\ansi\ansicpg1252\cocoartf2578
\cocoatextscaling0\cocoaplatform0{\fonttbl}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
}

from graphics import *
from time import *
import random

def main():
    # Screen definition
    win = GraphWin("Aim Lab", 300, 300)
    win.setBackground("black")
    # Main game instructions
    for i in range(5):
        # Target elements
        r = random.randrange(10, 256)
        g = random.randrange(10, 256)
        b = random.randrange(10, 256)
        x = random.randrange(10,290)
        y = random.randrange(10,290)
        center = Point(x, y)
        #Target
        color = color_rgb(r, g, b)
        circle1 = Circle(center, 10)
        # Target hitbox
        p1 = Point(center.getX() - 5, center.getY() + 5)
        p2 = Point(center.getX() + 5, center.getY() - 5)
        hitBox = Rectangle(p1, p2)
        circle1.setFill(color)
        circle1.draw(win)
        click = win.getMouse()
        # User input effect
        # if TRUE show user they have hit the target, add points to score
        # if FALSE show user they have missed the target, does not add points to score
        if(click.getX() > p1.getX() and click.getX() < p2.getX() and click.getY() < p1.getY() and click.getY() > p2.getY()):
            circle1.undraw()
            print("Hit detected")
            continue
        else:
            print("Miss!")
            circle1.undraw()

    
    win.getMouse()
    win.close()
    
    
main()
    
