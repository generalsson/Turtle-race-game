import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Race")
screen.bgcolor("lightblue")

# Set up the finish line
finish_line = turtle.Turtle()
finish_line.speed(0)
finish_line.penup()
finish_line.goto(250, 200)
finish_line.pendown()
finish_line.goto(250, -200)
finish_line.hideturtle()

# Set up the turtles
turtles = []
colors = ["red", "blue", "green", "purple", "orange"]
for i in range(5):
    turtle_obj = turtle.Turtle()
    turtle_obj.speed(0)
    turtle_obj.shape("turtle")
    turtle_obj.color(colors[i])
    turtle_obj.penup()
    turtle_obj.goto(-250, 175 - i * 75)
    turtles.append(turtle_obj)


# Define the race function
def race():
    winner = None
    while not winner:
        for turtle_obj in turtles:
            turtle_obj.forward(random.randint(1, 5))
            if turtle_obj.xcor() >= 250:
                winner = turtle_obj
                break

    # Display the winner
    winner.penup()
    winner.goto(0, 0)
    winner.write("Winner!", align="center", font=("Arial", 24, "bold"))

    return winner


# Set up the betting system
bet = screen.textinput("Turtle Race", "Which turtle will win the race? (red, blue, green, purple, orange)")

# Check if the bet is valid
if bet not in colors:
    screen.textinput("Turtle Race", "Invalid bet! Please enter a valid turtle color.")
else:
    screen.textinput("Turtle Race", "Get ready to race!")
    winner = race()
    if bet == winner.color()[0]:
        screen.textinput("Turtle Race", "Congratulations! You won the bet!")
    else:
        screen.textinput("Turtle Race", "Sorry, you lost the bet.")

# Close the window when the user clicks on it
screen.exitonclick()
