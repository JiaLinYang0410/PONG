#turtle module for basic graphic
import turtle

window = turtle.Screen()
window.title("PONG")
window.bgcolor("black")
window.setup(width=800, height=600)

# Start page
start_page = turtle.Turtle()
start_page.speed(0)
start_page.color("white")
start_page.penup()
start_page.hideturtle()

start_page.goto(0, 100)
start_page.write("PONG!", align="center", font=("Press Start 2P", 48, "normal"))
start_page.goto(0, 20)
start_page.write("Player 1 use 'W' and 'S' keys.", align="center", font=("Press Start 2P", 10, "normal"))
start_page.goto(0, -20)
start_page.write("Player 2 use 'Up' and 'Down' keys.", align="center", font=("Press Start 2P", 10, "normal"))
start_page.goto(0, -100)
start_page.write("Press 'Enter' to start", align="center", font=("Press Start 2P", 18, "normal"))

game_in_progress = False

def start_game():
    #clear start page
    global game_in_progress  
    #prevent game from resetting when pressing 'Enter' when there is game in process
    if not game_in_progress:
        game_in_progress = True  # Set the flag to True
        start_page.clear()  

        #create new window
        window = turtle.Screen()
        #give it a name
        window.title("Pong Game")
        #background color
        window.bgcolor("black")
        #set size of window
        window.setup(width = 800, height = 600)
        #stops window from updating/game runs faster
        window.tracer(0)


        #Paddle A 
        #create a turtle object, turtle -> module name, Turtle -> class name
        paddle_A = turtle.Turtle()
        #speed of animation, set it to maximum speed
        paddle_A.speed(0)
        paddle_A.shape("square")
        paddle_A.color("white")
        #adjust size of paddle
        paddle_A.shapesize(stretch_wid = 5, stretch_len = 0.5)
        #move cursor without leaving mark/ink/lines
        paddle_A.penup()
        #position(coordinate) where paddle A starts, where (0,0) is the middle of the screen
        paddle_A.goto(-350, 0)

        #Paddle B
        #create a turtle object, turtle -> module name, Turtle -> class name
        paddle_B = turtle.Turtle()
        #speed of animation, set it to maximum speed
        paddle_B.speed(0)
        paddle_B.shape("square")
        paddle_B.color("white")
        #adjust size of paddle
        paddle_B.shapesize(stretch_wid = 5, stretch_len = 0.5)
        #move cursor without leaving mark/ink/lines
        paddle_B.penup()
        #position(coordinate) where paddle B starts, where (0,0) is the middle of the screen
        paddle_B.goto(350,0)

        #Ball
        #create a turtle object, turtle -> module name, Turtle -> class name
        ball = turtle.Turtle()
        #speed of animation, set it to maximum speed
        ball.speed(0)
        ball.shape("circle")
        ball.color("white")
        #move cursor without leaving mark/ink/lines
        ball.penup()
        #position(coordinate) where ball starts, where (0,0) is the middle of the screen
        ball.goto(0,0)

        #ball movement
        #everytime ball moves, moves by 0.15 pixels
        ball.dx = 0.15
        ball.dy = -0.15

        #scoring
        pen = turtle.Turtle()
        pen.speed()
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 260)
        pen.write("Player A: 0          Player B: 0", align = "center", font = ("Press Start 2P", 18, "normal"))

        score_a = 0
        score_b = 0
        winning_score = 5
        #moving the paddles using functions
        def paddle_A_up():
            #assigns y coordinate of paddle A to variable y
            y = paddle_A.ycor()
            y += 20
            #set y coordinate of y to new y coordinate
            paddle_A.sety(y)

        def paddle_A_down():
            #assigns y coordinate of paddle A to variable y
            y = paddle_A.ycor()
            y -= 20
            #set y coordinate of y to new y coordinate
            paddle_A.sety(y)

        def paddle_B_up():
            #assigns y coordinate of paddle A to variable y
            y = paddle_B.ycor()
            y += 20
            #set y coordinate of y to new y coordinate
            paddle_B.sety(y)

        def paddle_B_down():
            #assigns y coordinate of paddle A to variable y
            y = paddle_B.ycor()
            y -= 20
            #set y coordinate of y to new y coordinate
            paddle_B.sety(y)    

        def display_winner(player):
            window.clear()
            winner_display = turtle.Screen()
            winner_display.bgcolor("black")
            winner_display = turtle.Turtle()
            winner_display.speed(0)
            winner_display.color("white")
            winner_display.penup()
            winner_display.hideturtle()
            winner_display.goto(0, 0)
            winner_text = "Player {} Wins!".format(player)
            winner_display.write(winner_text, align="center", font=("Press Start 2P", 30, "normal"))

        #keyboard binding
        #listens to keyboard input
        window.listen()
        #when user presses the key w, calls function paddle_A_up
        window.onkeypress(paddle_A_up, "w")
        #when user presses the key s, calls function paddle_A_down
        window.onkeypress(paddle_A_down, "s")
        #press up arrow key, calls function paddle_B_up
        window.onkeypress(paddle_B_up, "Up")
        #press down arrow key, calls function paddle_B_down
        window.onkeypress(paddle_B_down, "Down")
        
        #main game loop
        while True:
            if game_in_progress: 
            #everytime loop runs -> updates screen
                window.update()

                #move the ball
                ball.setx(ball.xcor() + ball.dx)
                ball.sety(ball.ycor() + ball.dy)

            #border check, make sure ball doesn't fly out the screen
            #top border
            if ball.ycor() > 290:
                ball.sety(290)
                #reverses direction of the ball
                ball.dy *= -1
            #bottom border
            if ball.ycor() < -290:
                ball.sety(-290)
                #reverses direction of the ball
                ball.dy *= -1  
            #left border
            if ball.xcor() < -390:
                #updates score
                score_b += 1
                #clear previous score
                pen.clear()
                #print new score
                pen.write("Player A: {}          Player B: {}".format(score_a, score_b), align = "center", font = ("Press Start 2P", 18, "normal"))
                #set balls position back to center
                ball.goto(0, 0)
                ball.dx *= -1
            #right border
            if ball.xcor() > 390:
                score_a += 1
                pen.clear()
                pen.write("Player A: {}          Player B: {}".format(score_a, score_b), align = "center", font = ("Press Start 2P", 18, "normal"))
                ball.goto(0, 0)
                ball.dx *= -1

            #paddle & ball collision
            if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_B.ycor() + 40 and ball.ycor() > paddle_B.ycor() - 40):
                ball.setx(340)
                ball.dx *= -1
            
            if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_A.ycor() + 40 and ball.ycor() > paddle_A.ycor() - 40):
                ball.setx(-340)
                ball.dx *= -1

            #winning player display
            if score_a >= winning_score:
                display_winner(1)
                game_in_progress = False
                break
            elif score_b >= winning_score:
                display_winner(2)
                game_in_progress = False
                break

#listen for enter key press to start game           
window.listen()
window.onkeypress(start_game, "Return")

#keep window opened
window.mainloop()