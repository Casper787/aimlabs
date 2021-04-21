{\rtf1\ansi\ansicpg1252\cocoartf2578
\cocoatextscaling0\cocoaplatform0{\fonttbl}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
}

from graphics import *
import random

def main(win):
    score = 0
    # Main game internal instructions
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
        # check if target was hit
        # if comparison == TRUE, target was hit
        # if comparsion == FALSE, target was not hit
        if(hitRecognition(click, p1, p2, center, circle1) == 1):
            score += 10
            continue
        
    print("Your score was: ",score)
    win.getMouse()
    win.close()
    
def startingScreen():
    # Screen welcome message
    # startingScreen() welcomes the user to play and instructs them to "click" in order to begin playing
    welcomeText = Text(Point(150, 100), "Welcome\n to\n the\n Lab\n\n\n\n Click to continue")
    welcomeText.setTextColor("white")
    welcomeText.draw(win)
    win.getMouse()
    welcomeText.undraw()
    
def hitRecognition(click, p1, p2, center, circle1):
    # User input management
    # hitRecognition(*object and input details*) takes in the users input, in this case the user's click
    #     it will compare it to the location of the target currently being displayed
    #     if the click matches the coordinates of the target, it will return 1 and continue the loop this function
    #     was called from
    # if TRUE show user they have hit the target, allow the loop calling this function to add points to score
    if(click.getX() > p1.getX() and click.getX() < p2.getX() and click.getY() < p1.getY() and click.getY() > p2.getY()):
        circle1.undraw()
        print("Hit detected")
        return 1
    # if FALSE show user they have missed the target, does not add points to score
    else:
        print("Miss!")
        circle1.undraw()
        return 0
    
win = GraphWin("Aim Lab", 300, 300)
win.setBackground("black")
startingScreen()
main(win)
