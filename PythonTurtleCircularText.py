#Python Turtle - WordArt Challenge - www.101computing.net/python-turtle-wordart-challenge/
import turtle
import random
from alphabet import alphabet
from math import cos, sin, atan2, radians, degrees 

myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(0)
window = turtle.Screen()
window.bgcolor("#000000")
myPen.pensize(2)

def displayMessage(message,fontSize,color,x,y,rotationAngle):
  myPen.color(color)
  message=message.upper()
  myPen.penup()
  myPen.goto(x,y)  
  for character in message:
    if character in alphabet:
      letter=alphabet[character]
      myPen.setheading(rotationAngle)
      myPen.penup()
    
      x=0
      y=0
      for dot in letter:
        angle = atan2((dot[1]-y),(dot[0]-x))
        angle= degrees(angle)    
  
        distance = ((dot[0]-x)**2 + (dot[1]-y)**2)**0.5
        myPen.setheading(rotationAngle)
  
        myPen.left(angle)
        myPen.forward(distance*fontSize)
        x = dot[0]
        y = dot[1]
        myPen.pendown()
  
      myPen.penup()
      angle = atan2((0-y),(0-x))
      angle = degrees(angle)    
  
      distance = ((0-x)**2 + (0-y)**2)**0.5
      myPen.setheading(rotationAngle)
  
      myPen.left(angle)
      myPen.forward(distance*fontSize)
  
    myPen.setheading(rotationAngle)
    myPen.penup()
    myPen.forward(fontSize)    
    
    myPen.forward(characterSpacing)
    

#Main Program Starts Here
fontSize = 30
fontColor="#FF00FF"
characterSpacing = 5
cursorX = -150
cursorY = -100

message = "Hello World"
rotationAngle=90
myPen.goto(cursorX,cursorY)

for character in message:
  pos=myPen.position()
  displayMessage(character,fontSize,fontColor,pos[0],pos[1],rotationAngle)
  rotationAngle-=180/(len(message)-1)
