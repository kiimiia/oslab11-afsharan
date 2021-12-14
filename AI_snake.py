import random
import arcade
import math

SCREEN_WIDTH=500
SECREEN_HEIGHT=500
DEFAULT_FONT_SIZE =4 

class snake(arcade.Sprite) : 

    def __init__(self,w,h) -> None:
        super().__init__()  

        self.width=16
        self.height=16
        self.color=arcade.color.BLACK
        self.body_size=0
        self.center_x=SCREEN_WIDTH//2  
        self.center_y=SECREEN_HEIGHT//2
        self.speed=2
        self.r=10
        self.change_x = 0  
        self.change_y = 0 
        self.score = 1
        self.body = [] 


    def draw(self):
        
        for index, item in enumerate(self.body):  
            arcade.draw_circle_filled(item[0], item[1], self.r, self.color) 
                

    def move(self):

        for i in range(len(self.body)-1, 0, -1):
            self.body[i][0] = self.body[i-1][0]
            self.body[i][1] = self.body[i-1][1]


        self.center_x += self.speed * self.change_x
        self.center_y += self.speed * self.change_y  


        if self.body:
            self.body[0][0] += self.speed * self.change_x
            self.body[0][1] += self.speed * self.change_y  
        
            

    def eat(self):

        self.body.append([self.center_x,self.center_y])
        self.score += 1  


class Apple(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__("apple.png")
        self.width = 35
        self.height = 35
        self.center_x = random.randint(20, w-20)  
        self.center_y = random.randint(20, h-20)      


class Pear(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__("pear.png")
        self.width = 35
        self.height = 35       
        self.center_x = random.randint(20, w-20)  
        self.center_y = random.randint(20, h-20)


class Shit(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__("shit.png")
        self.width = 35
        self.height = 35
        self.center_x = random.randint(20, w-20)  
        self.center_y = random.randint(20, h-20)


class game(arcade.Window) :

    def __init__(self):
        arcade.Window.__init__(self, SCREEN_WIDTH, SECREEN_HEIGHT, title='snake game') 
        arcade.set_background_color(arcade.color.RICH_LAVENDER)
        
        #object az hame classha
        self.snake = snake(SCREEN_WIDTH, SECREEN_HEIGHT)  
        self.apple = Apple(SCREEN_WIDTH, SECREEN_HEIGHT)  
        self.pear = Pear(SCREEN_WIDTH, SECREEN_HEIGHT)
        self.shit = Shit(SCREEN_WIDTH, SECREEN_HEIGHT)


    #rasm #graphic output
    def on_draw(self): 
        arcade.start_render()  

        if self.snake.score >= 0 :  
            self.snake.draw()
            self.apple.draw()
            self.pear.draw()
            self.shit.draw()

            #position score
            start_x = 10 
            start_y = SCREEN_WIDTH - 30 
        
            arcade.draw_text('Score : %i'%self.snake.score, start_x , start_y ,arcade.color.BLACK , DEFAULT_FONT_SIZE * 3, width=SCREEN_WIDTH, align='left')
            
        
        else: 
        
            arcade.draw_text('Game Over',SCREEN_WIDTH//2, SECREEN_HEIGHT//2,arcade.color.BLACK, DEFAULT_FONT_SIZE * 3, width=SCREEN_WIDTH, align='left')
        

    #mantegh bazi
    def on_update(self, delta_time: float): 

        # hooshe masnooie baraye harkate snake
        X=0  
        Y=0

        # peyda kardane positione apple & pear 
        if math.sqrt((self.snake.center_x-self.apple.center_x)**2+(self.snake.center_y-self.apple.center_y)**2) < math.sqrt((self.snake.center_x-self.pear.center_x)**2+(self.snake.center_y-self.pear.center_y)**2):
            X=self.apple.center_x
            Y=self.apple.center_y

        else :
            X=self.pear.center_x   
            Y=self.pear.center_y

        key_right=True
        key_left=True
        key_up=True
        key_down=True

        #shart position snake baraye AI game

        #x> & y==
        if self.snake.center_x>self.shit.center_x and self.snake.center_y==self.shit.center_y:
            key_left=False

        #x< & y==
        if self.snake.center_x<self.shit.center_x and self.snake.center_y==self.shit.center_y:
            key_right=False

        #x== & y>
        if self.snake.center_x==self.shit.center_x and self.snake.center_y>self.shit.center_y:
            key_down=False

        #x== & y<
        if self.snake.center_x==self.shit.center_x and self.snake.center_y<self.shit.center_y:
            key_up=False

        #4 sharte lazem barasase 4 kelide bazi baraye move
        if  key_left and self.snake.center_x > X:
            self.snake.change_x = -1
            self.snake.change_y = 0
            self.snake.move()
            

        elif key_right and  self.snake.center_x < X:

            self.snake.change_x = 1
            self.snake.change_y = 0
            self.snake.move()


        elif key_down and self.snake.center_y > Y:

            self.snake.change_x = 0
            self.snake.change_y = -1
            self.snake.move()


        elif key_up and self.snake.center_y < Y:

            self.snake.change_x = 0
            self.snake.change_y = 1      
            self.snake.move()

        # +1 => APPLE  
        if arcade.check_for_collision(self.snake,self.apple):
            self.apple = Apple(SCREEN_WIDTH, SECREEN_HEIGHT)
            self.snake.eat() 

        #+2 => PEAR
        if arcade.check_for_collision(self.snake,self.pear):
            self.pear = Pear(SCREEN_WIDTH, SECREEN_HEIGHT)    
            self.snake.eat() 
            self.snake.eat()  
    

play_game=game()
#loop infinty
arcade.run() 