# My first python program

import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by Nastase Valentin")
wn.bgcolor("black")  # bgcolor is "background color"
wn.setup(width=800, height=600)
wn.tracer(0)

# Scor 
scor_a = 0
scor_b = 0

# Paleta A
paleta_a = turtle.Turtle()
paleta_a.speed(0)
paleta_a.shape("square")
paleta_a.shapesize(stretch_wid=6 , stretch_len=1)
paleta_a.color("white")
paleta_a.penup()
paleta_a.goto(-350, 0 )


# Paleta B
paleta_b = turtle.Turtle()
paleta_b.speed(0)
paleta_b.shape("square")
paleta_b.shapesize(stretch_wid=6 , stretch_len=1)
paleta_b.color("white")
paleta_b.penup()
paleta_b.goto(350, 0 )

# Mingea
mingea = turtle.Turtle()
mingea.speed(0)
mingea.shape("square")
mingea.color("white")
mingea.penup()
mingea.goto(0, 0)
mingea.dx = 0.2
mingea.dy = 0.2 


# Text scor
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0, 260)
text.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "bold"))


# Function for paleta_a
def paleta_a_up():
    y = paleta_a.ycor()
    y += 20
    paleta_a.sety(y)

def paleta_a_down():
    y = paleta_a.ycor()
    y -= 20
    paleta_a.sety(y) 

    ### Functions for paleta_b  
def paleta_b_up():
    y = paleta_b.ycor()
    y += 20
    paleta_b.sety(y)

def paleta_b_down():
    y = paleta_b.ycor()
    y -= 20
    paleta_b.sety(y)      

# Tastele 
wn.listen()
wn.onkeypress(paleta_a_up, "w")    
wn.onkeypress(paleta_a_down, "s") 
wn.onkeypress(paleta_b_up, "Up")    
wn.onkeypress(paleta_b_down, "Down") 


# Main game loop
while True:
    wn.update()

    ### Misca mingea 
    mingea.setx(mingea.xcor() + mingea.dx)
    mingea.sety(mingea.ycor() + mingea.dy)

    # Margini  
    if mingea.ycor() > 290: 
       mingea.sety(290)
       mingea.dy *= -1
       winsound.PlaySound("perete.wav", winsound.SND_ASYNC)

    if mingea.ycor() < -290: 
       mingea.sety(-290)
       mingea.dy *= -1   
       winsound.PlaySound("perete.wav", winsound.SND_ASYNC)

    if mingea.xcor() > 390:
       mingea.goto(0, 0)
       mingea.dx *= -1  
       scor_a += 1 
       text.clear()
       text.write("Player A: {}  Player B: {}".format(scor_a, scor_b), align="center", font=("Courier", 24, "bold"))
       winsound.PlaySound("out.wav", winsound.SND_ASYNC)


    if mingea.xcor() < -390:
       mingea.goto(0, 0)
       mingea.dx *= -1  
       scor_b += 1 
       text.clear()  
       text.write("Player A: {}  Player B: {}".format(scor_a, scor_b), align="center", font=("Courier", 24, "bold"))
       winsound.PlaySound("out.wav", winsound.SND_ASYNC)


    # Coleziune pentru Minge si Paleta
    if (mingea.xcor() > 340 and mingea.xcor() < 350) and (mingea.ycor() < paleta_b.ycor() + 40 and mingea.ycor() > paleta_b.ycor() -40):
        mingea.setx(340)
        mingea.dx *= -1
        winsound.PlaySound("paleta.wav", winsound.SND_ASYNC)

    if (mingea.xcor() < -340 and mingea.xcor() > -350) and (mingea.ycor() < paleta_a.ycor() + 40 and mingea.ycor() > paleta_a.ycor() -40):
        mingea.setx(-340)
        mingea.dx *= -1 
        winsound.PlaySound("paleta.wav", winsound.SND_ASYNC)   

   