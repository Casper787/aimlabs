import random
from graphics import *

def main(win):
    # Final stat elements
    score = 0
    hits = 0
    # Main game internal instructions 
    for i in range(5):
        # Target elements
        r = randomColorGenerator()
        g = randomColorGenerator()
        b = randomColorGenerator()
        x = randomCoordinateGenerator()
        y = randomCoordinateGenerator()
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
            hits += 1
            continue
    showAccuracy(hits)
    closingScreen(score)
        
    
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
    
def closingScreen(score):
    print("Your score was: ",score)
    closingText = Text(Point(150, 100), "You have completed your session\n\n\n Thanks for playing\n\n Click to close")
    closingText.setTextColor("white")
    closingText.draw(win)
    win.getMouse()
    win.close()
    
def randomColorGenerator():
    return random.randrange(10, 256)

def randomCoordinateGenerator():
    return random.randrange(10,290)

def showAccuracy(hits):
    hitsText = hits/5 * 100
    accuracyText = Text(Point(150, 100), "Your total accuracy was\n")
    accuracytext2 = Text(Point(150,125), hitsText)
    accuracytext2.setTextColor("white")
    accuracyText3 = Text(Point(150, 150), "Click to continue")
    accuracyText.setTextColor("white")
    accuracyText3.setTextColor( "white")
    accuracyText.draw(win)
    accuracytext2.draw(win)
    accuracyText3.draw(win)
    win.getMouse()
    accuracyText.undraw()
    accuracytext2.undraw()
    accuracyText3.undraw()
    
win = GraphWin("Aim Lab", 300, 300)
win.setBackground("black")
startingScreen()
main(win)