
#Dominators
#Rezaul Hoque,Shouliang Wang
#The running man
#



from gamelib import*

game=Game(1000,800,"The running man")
bk = Image("street.jpg",game)
game.setBackground(bk)
bk.resizeTo(1000,800)
f1=Font(red,36,black,"Impact")
f2=Font(blue,30,red,"Impact")
play=Image("play.png",game)
play.resizeTo(400,200)
coins=Animation("coins.png",64,game,512/8,512/8)
coins.resizeTo(50,50)
coins.moveTo(1600,700)
coins.setSpeed(1,270)
car=Image("car.png",game)
car.resizeTo(330,150)
car.moveTo(2000,720)
car.setSpeed(20,270)
rm = Animation("rm.png",6,game,594/3,667/2,4)
rm.resizeTo(100,175)
rm.moveTo(75,700)
jumping = False
landed = False
factor = 1
gameover=Image("gameover.jpg",game)
gameover.resizeTo(1000,800)
robber=Animation("robber.png",6,game,1000/6,313,3)
robber.resizeTo(100,175)
robber.moveTo(950,700)
robber.setSpeed(5,270)




while not game.over:
    game.processInput()
    game.scrollBackground("left",10)
    game.drawText("How to play: Press SPACE to JUMP",40,40,f1)

    car.x-=20
    bk.draw()
    rm.draw()
    play.draw()
    robber.draw()
  
    
    
    
    


    if mouse.collidedWith(play) and mouse.LeftClick:
        game.over=True
    game.update(30)
game.over=False


    
 
while not game.over:
    game.processInput()
    game.scrollBackground("left",10)
    

    
  
    

    rm.draw()
    coins.draw()
    coins.x-=20
    car.draw()
    car.x-=30
    
    robber.move()
   
    
    
    
   

    if car.isOffScreen("left"):
        car.moveTo(1500,720)
        coins.visible=True
        
        
        
        
    if coins.isOffScreen("left"):
          x = randint(1800,2000)
          y = randint(600,720)
          coins.moveTo(x,y)
          car.visible=True

   


    if rm.collidedWith(car):
        game.score-=5
        car.visible=False
        
          

        
        
        

    if rm.collidedWith(coins):
        game.score+=10
        coins.visible=False
        
    


    if rm.y< 700:
        landed = False

    else:
        landed = True

   
            
    if keys.Pressed[K_SPACE] and landed and not jumping:
        jumping = True

    if jumping:
   
        rm.y -=27*factor
        
        factor*=.95
        
        landed = False
        
        if factor < .40:
            jumping = False
            
            factor = 1
            
    if not landed: 
        rm.y +=6

    if rm.collidedWith(car) or game.score<0:
        game.over=True
        gameover.draw()
        game.drawText("You LOST:(",700,700,f1)
        

        
        
 
         
        
    game.displayScore(0,0,f2)
    game.update(30)






