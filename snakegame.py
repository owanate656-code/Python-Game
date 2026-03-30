import tkinter as tk
import random
import json


#-----------Variables and Constants---------------
TILE_SIZE = 25
GAME_WIDTH = 500
GAME_HEIGHT = 500
SNAKE_COLOR = 'green'
FOOD_COLOR = 'red'
BACKGROUND_COLOR='#05a5f0'
BODY_PARTS =1
SPEED = 100
score = 0
pause = False
direction ='right'
dir_bef_none = direction
gameover = False
file_name ='snake.json'




#---------------Game Classes and Functions----------------
class Snake:
    def __init__(self):
        self.size = BODY_PARTS
        self.coordinates = []
        
        for i in range( BODY_PARTS):
            self.coordinates.append([0,0])
        for x , y in self.coordinates:
            self.squares =canvas.create_rectangle(x,y , x+TILE_SIZE,y+TILE_SIZE, fill= SNAKE_COLOR, tags='snake')

class Food:
    def __init__(self):
        
        self.x = random.randint(0,19)*TILE_SIZE
        self.y = random.randint(0,19)*TILE_SIZE   
        canvas.create_oval(self.x,self.y , self.x+TILE_SIZE, self.y+TILE_SIZE, fill=FOOD_COLOR, tags='food') 
    

def turn():
    global direction, food, score , gameover , highscore , pause , dir_bef_none
    x,y = snake.coordinates[0]
    if direction =='right':
         x += TILE_SIZE
         dir_bef_none ='right'
    elif direction =='left':
         x -= TILE_SIZE
         dir_bef_none ='left'
    elif direction =='up':
        y-= TILE_SIZE
        dir_bef_none ='up' 
        print(dir_bef_none)
    elif direction =='down':
         y+= TILE_SIZE
         dir_bef_none ='down'
    elif direction =='none':
        x+=0
        y+=0
    new_head = [x,y]
    snake.coordinates.insert(0, new_head)
    # print(snake.coordinates)
    
    
    
    
        

    if snake.coordinates[0][0] == food.x and snake.coordinates[0][1] == food.y:
        score+=1
        label.config(text=f'Score: {score} Highscore: {highscore}')
        canvas.delete('food')
        canvas.delete('snake')
        for body_x, body_y in snake.coordinates:
            canvas.create_rectangle(body_x, body_y, body_x+TILE_SIZE, body_y+TILE_SIZE, fill=SNAKE_COLOR, tags='snake')
        food = Food()

    else:
        snake.coordinates.pop()  
        canvas.delete('snake')
        for body_x, body_y in snake.coordinates:
            canvas.create_rectangle(body_x, body_y, body_x+TILE_SIZE, body_y+TILE_SIZE, fill=SNAKE_COLOR, tags='snake')

    head = snake.coordinates[0]
    body = snake.coordinates[1:]
    if head in body:
        gameover= True
        


def change_direction(e):
    global direction
    
    if e.keysym == 'Down':
        if direction != 'up':
            direction='down'
            
    elif e.keysym =='Up':
        if direction != 'down':
            direction='up'
    elif e.keysym =='Right':
        if direction != 'left':
            direction='right'
    elif e.keysym =='Left':
        if direction != 'right':
            direction='left'
    elif direction =='none':
        direction=='none'

def collision():
    global gameover
    x_head , y_head = snake.coordinates[0]
    
    if x_head >= GAME_WIDTH or x_head <0 or y_head>= GAME_HEIGHT or y_head<0:
         gameover=True
   
def game_loop():
    global gameover , highscore , direction , pause
    turn()
    collision()
    
    if gameover == False:
        window.after(SPEED, game_loop)
    elif gameover == True:
        
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER ", fill="red", tags='gameover')
        if score >= highscore:
                
                highscore = score
                label.config(text=f'Score: {score} Highscore: {highscore}')
                save_score(highscore)

def load_score():
    with open(file_name,'r') as file:
        return json.load(file)

def save_score(score):
    with open(file_name,'w') as file:
        json.dump({'highscore': score}, file)


def restart():
    global snake , score , gameover , food , direction ,highscore
    gameover = False
    score = 0
    label.config(text=f'Score: {score} Highscore: {highscore}')
    canvas.delete('snake')
    canvas.delete('food')
    canvas.delete('gameover')
    direction = 'right'
    snake = Snake()
    
    food = Food()
    game_loop()
    

def pause_game(e):
    global pause
    pause = True

def resume(e):
    global pause
    pause = False

#------------Game Window and Setup------------
snake_user = load_score()
highscore = snake_user['highscore']

window = tk.Tk()
window.title('Snake Game')

label = tk.Label(window, text=F'Score: {score} Highscore: {highscore}', font=('Consolas', 20))
label.grid(row=0 , column= 0)



canvas = tk.Canvas(window , bg= BACKGROUND_COLOR, width= GAME_WIDTH, height= GAME_HEIGHT)
canvas.grid()

frame = tk.Frame(window, )
frame.grid(sticky='ew')
frame.grid_columnconfigure(0, weight=1)


restart_btn = tk.Button(frame,text='Restart', font=('Consolas', 15),bg='#d4e704',fg='white', width=33, command=restart,)
restart_btn.grid(row=0, column=0 , sticky='ew')


# resume_btn = tk.Button(frame , text='R',font=('Consolas', 15),fg='yellow', command= resume)
# resume_btn.grid(row= 0 , column=2)

# pause_btn = tk.Button(window,text = 'P',font=('Consolas', 15), fg='yellow', command= pause_game)
# pause_btn.grid(row= 0 , column=1)

food = Food()
snake = Snake()

game_loop()


window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2)-(window_width/2))
y = int((screen_height/4)- (window_height/4))

window.geometry(f'{ window_width}x{window_height}+{x}+{y}')


#---------------------Keyboard Functions------------------
window.bind('W', pause_game)
window.bind('w', pause_game)
window.bind('q', resume)
window.bind('Q', resume)
window.bind('<KeyPress>',change_direction)
window.mainloop()