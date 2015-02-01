from turtle import *
import turtle

def turtlecolors():
	# background color
	bgcolor = raw_input("Enter background color: ")
	pencolor= raw_input("Enter Pen Color: ")
	fillcolor = raw_input("Enter Fill Color: ")
	
	# background color if empty = white
	if not bgcolor:	
		wn = turtle.Screen()
		wn.bgcolor("white")
	else:
		wn.bgcolor(bgcolor)
	
	# pen color and fill color
	if not pencolor:
		color("black", "white")
	elif not fillcolor:
		color("black", "white")
	else:
		color(pencolor, fillcolor)
		
def turtlemovement():
	fd = 

def turtlegraphics():
	begin_fill()
	while True:
		forward(fd)
		left(170)
		if abs(pos()) < 1:
			break
	end_fill()
	done()
print(turtlecolors())
print(turtlegraphics())
