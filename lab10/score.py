from os import scandir
from select import select
import pygame
import random
import psycopg2
from psycopg2 import Error
finished=True
print('Enter your name')
name=input()
finished=False
pygame.init()
BLACK = (0, 0, 0)
LINE_COLOR = (50, 50, 50)
HEIGHT = 400
WIDTH = 400

BLOCK_SIZE = 20
path='C:\\Users\\apal0\OneDrive\Desktop\pp2\lab8,9\snake'
class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y


class Wall:
    def __init__(self, level):
        self.body = []
        f = open(path+"\levels\level{}.txt".format(level), "r")

        #lines = content.split('\n')
        #print(len(lines[0]))
        
        for y in range(0, HEIGHT//BLOCK_SIZE + 1):
            for x in range(0, WIDTH//BLOCK_SIZE + 1):
                if f.read(1) == '#':
                    self.body.append(Point(x, y))

    def draw(self):
        for point in self.body:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (226,135,67), rect)
class Food:
    def __init__(self,wall,snake):
        self.location=Point(random.randint(0, 19), random.randint(0, 19))
        i,j=0,0
        while (self.location.x!=wall.body[i].x and self.location.y!=wall.body[i].y) and (self.location.x==snake.body[j].x and self.location.y==snake.body[j].y):
            if i!=len(wall.body):
                i+=1
            else:
                i=0
            if j!=len(wall.body):
                j+=1
            else:
                j=0
            self.location=Point(random.randint(0, 19), random.randint(0, 19))
    def gen(self,wall,snake):
        self.location=Point(random.randint(0, 19), random.randint(0, 19))
        i,j=0,0
        while (self.location.x!=wall.body[i].x and self.location.y!=wall.body[i].y) and (self.location.x==snake.body[j].x and self.location.y==snake.body[j].y):
            if i!=len(wall.body):
                i+=1
            else:
                i=0
            if j!=len(wall.body):
                j+=1
            else:
                j=0
            self.location=Point(random.randint(0, 19), random.randint(0, 19))
    def draw(self):
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (0, 255, 0), rect)
class SuperFood():
    def __init__(self,wall,snake):
        self.location=Point(random.randint(0, 19), random.randint(0, 19))
        i,j=0,0
        while (self.location.x!=wall.body[i].x and self.location.y!=wall.body[i].y) and (self.location.x==snake.body[j].x and self.location.y==snake.body[j].y):
            if i!=len(wall.body):
                i+=1
            else:
                i=0
            if j!=len(wall.body):
                j+=1
            else:
                j=0
            self.location=Point(random.randint(0, 19), random.randint(0, 19))
    def gen(self,wall,snake):
        self.location=Point(random.randint(0, 19), random.randint(0, 19))
        i,j=0,0
        while (self.location.x!=wall.body[i].x and self.location.y!=wall.body[i].y) and (self.location.x==snake.body[j].x and self.location.y==snake.body[j].y):
            if i!=len(wall.body):
                i+=1
            else:
                i=0
            if j!=len(wall.body):
                j+=1
            else:
                j=0
            self.location=Point(random.randint(0, 19), random.randint(0, 19))
    def draw(self):
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (255,0 , 0), rect)
    def disappear(self):
        self.location=Point(0,0)


class Snake:
    def __init__(self):
        self.body = [Point(10, 11)]
        self.dx = 0
        self.dy = 0

    def move(self):    
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y

        self.body[0].x += self.dx 
        self.body[0].y += self.dy 

        if self.body[0].x * BLOCK_SIZE > WIDTH:
            self.body[0].x = 0
        
        if self.body[0].y * BLOCK_SIZE > HEIGHT:
            self.body[0].y = 0

        if self.body[0].x < 0:
            self.body[0].x = WIDTH / BLOCK_SIZE
        
        if self.body[0].y < 0:
            self.body[0].y = HEIGHT / BLOCK_SIZE

    def draw(self):
        point = self.body[0]
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (255, 0, 0), rect)


        for point in self.body[1:]:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (0, 255, 0), rect)

    def check_collision(self, food,wall,super_food):
        global score
        for i in range(1,len(self.body)):
            if self.body[0].x==self.body[i].x:
                if self.body[0].y==self.body[i].y:
                    exit()
        if self.body[0].x == food.location.x:
            if self.body[0].y == food.location.y:
                self.body.append(Point(food.location.x, food.location.y))
                food.gen(wall,self)
                score+=1
        if self.body[0].x == super_food.location.x:
            if self.body[0].y == super_food.location.y:
                self.body.append(Point(super_food.location.x, super_food.location.y))
                super_food.gen(wall,self)
                score+=5
        for i in range(0,len(wall.body)):
            if self.body[0].x==wall.body[i].x:
                if self.body[0].y==wall.body[i].y:
                    exit()
        if self.body[0].x>=20 or self.body[0].x<0:
            exit()
        if self.body[0].y>=20 or self.body[0].y<0:
            exit()
        
        

dirs={'UP':True,'DOWN':True,'RIGHT':True,'LEFT':True}
level=1
speed=5
def record_to_db(name,score):
    try:
        connection=psycopg2.connect(user='postgres',password='postgres',host='localhost',port='5432',database='postgres')
        cursor=connection.cursor()
        cursor.execute('SELECT EXISTS(select from SCORE where name=%s)',(name,))
        if cursor.fetchone()[0]:
            cursor.execute('UPDATE score SET score=%s where name=%s',(score,name))
            connection.commit()
        else:
            cursor.execute('INSERT INTO score VALUES(%s,%s)',(name,score))
            connection.commit()
    except (Exception,Error) as error:
        print(error)
    finally:
        if connection:
            cursor.close()
            connection.close()
score=0
def main(level,speed):
    global score
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, 440))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    snake = Snake()
    wall=Wall(level)
    food = Food(snake,wall)
    super_food=SuperFood(wall, snake)
    font=pygame.font.SysFont('Verdana', 30)
    SUPERFOOD=pygame.USEREVENT+1
    time=10000
    pygame.time.set_timer(SUPERFOOD, time)
    finished=False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished=True
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and dirs['RIGHT']:
                    snake.dx = 1
                    snake.dy = 0
                    dirs.update(LEFT=False,RIGHT=True,UP=True,DOWN=True)
                if event.key == pygame.K_LEFT and dirs['LEFT']:
                    snake.dx = -1
                    snake.dy = 0
                    dirs.update(LEFT=True,RIGHT=False,UP=True,DOWN=True)
                if event.key == pygame.K_UP and dirs['UP']:
                    snake.dx = 0
                    snake.dy = -1
                    dirs.update(LEFT=True,RIGHT=True,UP=True,DOWN=False)
                if event.key == pygame.K_DOWN and dirs['DOWN']:
                    snake.dx = 0
                    snake.dy = 1
                    dirs.update(LEFT=True,RIGHT=True,UP=False,DOWN=True)
        snake.move()

        snake.check_collision(food,wall,super_food)
        if len(snake.body) > 10 and len(snake.body) % 2 == 1:
            main(level+1,speed+1)
            wall = Wall(snake.level)
            dirs.update(LEFT=True,RIGHT=True,UP=True,DOWN=True)

        SCREEN.fill(BLACK)

        
        snake.draw()
        wall.draw()
        food.draw()
        if event.type==SUPERFOOD:
            super_food.draw()
        drawGrid()
        level_show=font.render(f'LEVEL-{level}', True, (255,255,255))
        score_show=font.render(f'SCORE-{score}', True, (255,255,255))
        SCREEN.blit(score_show, (215,400))
        SCREEN.blit(level_show,(50,400))
        pygame.display.update()
        CLOCK.tick(speed)
        record_to_db(name,score)


def drawGrid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, LINE_COLOR, rect, 1)
main(level,speed)

            