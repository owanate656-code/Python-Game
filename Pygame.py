import pygame
import sys

pygame.init()

#Variables
width = 500
height = 500
ball_speed = 0
elasticity =1
window = pygame.display.set_mode((width,height))
rect = pygame.Rect((150,200,30,30))
clock = pygame.time.Clock()
tiles =[pygame.Rect(400,400, 40,40) , pygame.Rect(450,400, 40,40) ,]
floor= pygame.Rect(0 , 300 , 500,40)
ball = pygame.Rect(60-20, 60-20, 40, 40)  # x, y, width, height

def draw():
    window.fill('red')
    pygame.draw.rect(window, 'blue', rect)
    pygame.draw.rect(window, 'yellow', floor)
    pygame.draw.circle(window, '#26d9d0', (ball.x + 20, ball.y + 20), 20)
    for tile in tiles:
        pygame.draw.rect(window, 'green', tile)


def check_collision(rect, tiles):
    collisions = []
    for tile in tiles:
        if rect.colliderect(tile):
            collisions.append(tile)
           
    return collisions
def border_check(rect):
    if rect.x < 0: rect.x = 0
    elif rect.x > width - rect.width: rect.x = width - rect.width
    if rect.y < 0: rect.y = 0
    elif rect.y > height - rect.height: rect.y = height - rect.height


def simulatingGravity(circle , floor , ):
    global ball_speed , elasticity
    gravity = 0.5
    ball_speed+= gravity 
    circle.y += ball_speed
    if circle.colliderect(floor):
        circle.bottom = floor.top
        ball_speed = -ball_speed * elasticity
        elasticity -= 0.1
        circle.y += ball_speed


        


while True:
    
    dx = 0
    dy = 0
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        dx -= 5
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        dx += 5
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        dy -= 5
    if keys[pygame.K_DOWN]  or keys[pygame.K_s]:
        dy += 5
    
    rect.x += dx
    collisions = check_collision(rect, tiles)
    
    for tile in collisions:
        future_tile = pygame.Rect(tile.x + dx, tile.y, tile.width, tile.height)
        can_move = True
        for other_tile in tiles:
            if other_tile is tile:
                continue
            if future_tile.colliderect(other_tile):
                can_move = False
                break
        if can_move:
            tile.x += dx
            can_move = False
        if tile.x < 0: 
            tile.x = 0
            
        elif tile.x > width - tile.width:
            tile.x = width - tile.width
            
        if not can_move:
            rect.x -= dx
            break

            
        
    rect.y += dy 
    collisions = check_collision(rect, tiles)      
    for tile in collisions:
        future_tile = pygame.Rect(tile.x, tile.y + dy, tile.width, tile.height)
        can_move = True
        for other_tile in tiles:
            if other_tile is tile:
                continue
            if future_tile.colliderect(other_tile):
                can_move = False
                break
        if can_move:
            tile.y += dy
        if tile.y < 0: 
            tile.y = 0
            can_move = False

        elif tile.y > height - tile.height: 
            tile.y = height - tile.height
            can_move = False
        if not can_move:
            rect.y -= dy
            break
    draw()
    border_check(rect)
    simulatingGravity(ball , floor )
    pygame.display.update()
    clock.tick(60) 
 