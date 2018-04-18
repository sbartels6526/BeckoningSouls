from gamelib import *
game = Game(995,604,"Beckoning Souls")
title = Image("title.jpg",game)
play= Image("play1.jpg",game,use_alpha= False)
play.resizeBy (-90)
play.moveTo (320,428)
game.setBackground(title)
b1= Image("b1.jpg",game)
b2= Image("b2.Jpg",game)
b3= Image("b3.Jpg",game) 
b4= Image("b4.Jpg",game)
b5= Image("b5.Jpg",game)
b6= Image("b6.jpg",game)
b7= Image("b7.jpg",game)
b8= Image("b8.Jpg",game)
b9= Image("b9.Jpg",game) 
b10= Image("b10.Jpg",game)
b11= Image("b11.Jpg",game)
b12= Image("b12.jpg",game)
b13= Image("b13.jpg",game)
b14= Image("b14.Jpg",game)
b15= Image("b15.Jpg",game)
level1s= Image("level1s.jpg",game)
level2s= Image("level2s.jpg",game)
level3s= Image("level3s.jpg",game)
go1 = Image("go1.jpg",game)
go2 = Image("go2.jpg",game)
go3 = Image("go3.jpg",game)
go4 = Image("go4.jpg",game)


death = Sound("death.ogg", 2)
lg= Sound ("lg.ogg",3)
ba= Sound ("ba.ogg",4)
wa= Sound ("wa.ogg",5)
win=Image ("win.png",game)
win.resizeBy (80)

control= Image ("control.jpg",game)
att = (Animation("att.png", 25, game, 960/5, 960/5))
att2 = (Animation("att2.png", 20, game, 960/5, 768/4))
att3 = (Animation("att3.png", 15, game, 960/5, 576/3))
att = []
for index in range (30):
    att.append(Animation("att.png", 25, game, 960/5, 960/5))
for index in range(30):
    x = randint(100,800)
    y = randint(100,4000)
    att[index].moveTo(x, -y)
    att[index].setSpeed (6,180)

att2 = []
for index in range (20):
    att2.append(Animation("att2.png", 20, game, 960/5, 768/4))
for index in range(20):
    x = randint(100,800)
    y = randint(100,4000)
    att2[index].moveTo(x, -y)
    att2[index].setSpeed (6,180)

att3 = []
for index in range (30):
    att3.append(Animation("att3.png", 15, game, 960/5, 576/3))
for index in range(30):
    x = randint(100,800)
    y = randint(100,4000)
    att3[index].moveTo(x, -y)
    att3[index].setSpeed (6,180)

controls = Image("controls.jpg",game,use_alpha= False)
controls.resizeBy(-85)
controls.moveTo(320,500)
zen = Animation("zenn.jpg",3,game,2048/3,2048,use_alpha= False)
zen.stop()
zen.resizeBy(-92)
zen.moveTo (320,465)
forest=Image("forest.jpg",game)
forest.resizeTo(game.width, game.height)
bow=Image ("bow.jpg",game, use_alpha= False)
arrow1= Image ("arrow1.jpg",game, use_alpha=False)
arrow1.resizeBy (-95)
bow.resizeBy (-90)
control = Image("control.jpg", game)
arrow2 = Image("arrow2.jpg", game, use_alpha = False)
#arrow Setup/LIST

arrow = Image("arrow.png",game)
arrow.resizeBy (-98)
arrow.moveTo (zen.x,zen.y)
bow.moveTo(zen.x+3,zen.y+7)
bow.resizeBy (-78)
for index in range(20):
    x = randint(100,700)
    y = randint(100,4000)
demons1 = []
for index in range(10):
    demons1.append(Animation("demons1.jpg",3,game,2048/3,2048,use_alpha= False))
for index in range(10):
    x = randint(100,800)
    y = randint(100,2000)
    demons1[index].moveTo(x, -y)
    demons1[index].resizeBy(-80)
    s = randint(2,3)
    demons1[index].setSpeed(s,180)


demons2 = []
for index in range(10):
    demons2.append(Animation("demons2.jpg",3,game,2048/3,2048,use_alpha= False))
for index in range(10):
    x = randint(100,800)
    y = randint(100,2000)
    demons2[index].moveTo(x, -y)
    demons2[index].resizeBy(-80)
    s = randint(2,3)
    demons2[index].setSpeed(s,180)
demons3 = []
for index in range(10):
    demons3.append(Animation("demons3.jpg",3,game,2048/3,2048,use_alpha= False))
for index in range(10):
    x = randint(100,800)
    y = randint(100,2000)
    demons3[index].moveTo(x, -y)
    demons3[index].resizeBy(-80)
    s = randint(2,3)
    demons3[index].setSpeed(s,180)
    
    

 
ring=[]
for index in range (20):
    ring.append(Image("ring.jpg",game,use_alpha=False))
for index in range(20):
    x = randint(100,800)
    y = randint(100,4000)
    ring[index].moveTo(x, -y)
    ring[index].setSpeed (3,180)

    ring[index].resizeBy(-95)

soul=[]
for index in range (20):
    soul.append(Animation("soul4.png",15,game,960/5,576/3 ))
for index in range(20):
    x = randint(100,800)
    y = randint(100,4000)
    soul[index].moveTo(x, -y)
    soul[index].setSpeed (3,180)

    soul[index].resizeBy(-70)
    
#Title Screen
arrow2.resizeBy(-95)
control.visible = False
arrow2.visible = False
game.setMusic ("titlescreen.ogg")
game.playMusic()
while not game.over:

    game.processInput()
    
    title.draw()
    play.draw()
    controls.draw()
    control.draw()
    arrow2.draw()

    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
        game.stopMusic()
    if controls.collidedWith(mouse) and mouse.LeftClick:
        control.visible = True
        arrow2.visible = True
        arrow2.moveTo (940,560)

    if arrow2.collidedWith(mouse) and mouse.LeftClick:
        arrow2.visible = False
        control.visible = False

    game.update(30)
game.over = False

#Story
game.setMusic ("background.ogg")
game.playMusic()
while not game.over:
    game.processInput()
    b1.draw ()
    arrow1.draw ()
    arrow1.moveTo (940,570)
    if arrow1.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    game.update(30)
game.over= False
while not game.over:
    game.processInput()
    b2.draw ()
    arrow1.draw ()
    arrow1.moveTo (940,570)
    if arrow1.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    game.update(30)
game.over= False
while not game.over:
    game.processInput()
    b3.draw ()
    arrow1.draw ()
    arrow1.moveTo (940,570)
    if arrow1.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    game.update(30)
game.over= False
while not game.over:
    game.processInput()
    b4.draw ()
    arrow1.draw ()
    arrow1.moveTo (940,570)
    if arrow1.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    game.update(30)
game.over= False
while not game.over:
    game.processInput()
    b5.draw ()
    arrow1.draw ()
    arrow1.moveTo (940,570)
    if arrow1.collidedWith(mouse) and mouse.LeftClick:
       game.over = True
    game.update(30)
game.over= False
while not game.over:
    game.processInput()
    b6.draw ()
    arrow1.draw ()
    arrow1.moveTo (940,570)
    if arrow1.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    game.update(30)
game.over= False
while not game.over:
    game.processInput()
    b7.draw ()
    arrow1.draw ()
    arrow1.moveTo (940,570)
    if arrow1.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    game.update(30)
game.over= False
while not game.over:
    game.processInput()
    level1s.draw ()
    arrow1.draw ()
    arrow1.moveTo (940,570)
    if arrow1.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    game.update(30)
game.over= False
game.stopMusic()
game.setMusic ("intown.ogg")
game.playMusic()
while not game.over:
    game.processInput()
    b8.draw ()
    arrow1.draw ()
    arrow1.moveTo (940,570)
    if arrow1.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    game.update(30)
game.over= False
while not game.over:
    game.processInput()
    b9.draw ()
    arrow1.draw ()
    arrow1.moveTo (940,570)
    if arrow1.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    game.update(30)
game.over= False
while not game.over:
    game.processInput()
    b10.draw ()
    arrow1.draw ()
    arrow1.moveTo (940,570)
    if arrow1.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    game.update(30)
game.over= False
while not game.over:
    game.processInput()
    b11.draw ()
    arrow1.draw ()
    arrow1.moveTo (940,570)
    if arrow1.collidedWith(mouse) and mouse.LeftClick:
       game.over = True
    game.update(30)
game.over= False
while not game.over:
    game.processInput()
    b12.draw ()
    arrow1.draw ()
    arrow1.moveTo (940,570)
    if arrow1.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    game.update(30)
game.over= False
while not game.over:
    game.processInput()
    b13.draw ()
    arrow1.draw ()
    arrow1.moveTo (940,570)
    if arrow1.collidedWith(mouse) and mouse.LeftClick:
       game.over = True
    game.update(30)
game.over= False
while not game.over:
    game.processInput()
    b14.draw ()
    arrow1.draw ()
    arrow1.moveTo (940,570)
    if arrow1.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    game.update(30)
game.over= False
while not game.over:
    game.processInput()
    b15.draw ()
    arrow1.draw ()
    arrow1.moveTo (940,570)
    if arrow1.collidedWith(mouse) and mouse.LeftClick:
       game.over = True
    game.update(30)
game.over= False
while not game.over:
    game.processInput()
    level2s.draw ()
    arrow1.draw ()
    arrow1.moveTo (940,570)
    if arrow1.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    game.update(30)
game.over= False
game.stopMusic()
#Transition

forest.draw ()
game.setBackground (forest)


#Level 1

demons1complete = 0
	
soulsCollected = 0
game.setMusic("mbl.ogg")
game.playMusic()
while not game.over:
    game.processInput ()



    if keys.Pressed[K_RIGHT]:
        game.scrollBackground ("left",0)
        
        zen.x += 4
        zen.prevFrame()
        wa.play ()


    elif keys.Pressed[K_LEFT]:
        game.scrollBackground ("right",0)
        zen.x -= 4
        zen.nextFrame()
        wa.play ()
    
    else:
        game.scrollBackground ("right",0)

        zen.draw()

    for index in range(10):
        demons1[index].health==100
        demons1[index].move()
        v = randint(1,2)
        demons1[index].moveTowards (zen,v)
 
        if demons1[index].collidedWith(zen):
            zen.health -= 50
            demons1[index].visible = False
  
            demons1complete += 1

    game.drawText("Health: " + str(zen.health),zen.x - 20,zen.y + 50)

    if zen.health<=0:
        game.over=True

    for index in range (10):
        if demons1[index].collidedWith (arrow):
            demons1[index].health -= 50
            arrow.visible = False
        
        if demons1[index].health <=0 and demons1[index].visible == True:
            demons1[index].visible=False
            demons1complete +=1
            soulsCollected += 1
    arrow.move()
    bow.draw()
    bow.moveTo (zen.x+15, zen.y+10)
    if keys.Pressed[K_SPACE]:
        arrow.visible = True
        arrow.moveTo(zen.x+15,zen.y+8)
        arrow.rotateTo(arrow.angleTo(mouse))
        arrow.setSpeed(24,arrow.angleTo(mouse))
        bow.rotateTo(bow.angleTo(mouse))
        bow.setSpeed(24,bow.angleTo(mouse))
        ba.play ()
    #soul (Making it WORK)
    for index in range(20):
        soul[index].move()
        if soul[index].collidedWith(zen):
 
            soul[index].visible = False
            zen.health += 5
    for index in range(20):
        ring[index].move()
        if ring[index].collidedWith(zen):
            ring[index].visible = False
            zen.health -= 10


            
    game.drawText("souls: " + str(soulsCollected),zen.x-10,zen.y + 80)
        

    if demons1complete==10:
        game.drawText("Level 1 Complete: ",400,80)
        game.over=True
          
    game.update (30)
game.over = False
game.stopMusic()
game.setBackground (forest)
#Level 2

demons2complete = 0
	
soulsCollected =0
game.setMusic("mbl.ogg")
game.playMusic()
for index in range (20):
    ring[index].moveTo(x, -y)

while not game.over and zen.health>0:
    game.processInput ()

    
    if keys.Pressed[K_RIGHT]: 
        game.scrollBackground ("left",0)
        zen.x += 4
        zen.prevFrame()
        wa.play ()

    elif keys.Pressed[K_LEFT]:
        game.scrollBackground ("right",0)
        zen.x -= 4
        zen.nextFrame()
        wa.play ()
    
    else:
        game.scrollBackground ("left",0)

        zen.draw()

    for index in range (10):
        demons2[index].move()
        v = randint(1,2)
        demons2[index].moveTowards (zen,v)

        if demons2[index].collidedWith(zen):
            zen.health -= 10
            demons2[index].visible = False

            demons2complete += 1

    game.drawText("Health: " + str(zen.health),zen.x - 20,zen.y + 50)

    if zen.health<=0:
        game.over=True
    for index in range (10):
        ring[index].move()
        if demons2[index].collidedWith (arrow):
            demons2[index].health -= 25
            arrow.visible = False
        if demons2[index].health <=0 and demons2[index].visible == True:
            demons2[index].visible=False
            demons2complete +=1
            soulsCollected += 1
        if demons2[index].visible == True and ring[index].y < 50:
            ring[index].visible = True
            ring[index].moveTo(demons2[index].x+15,demons2[index].y+15)
            ring[index].setSpeed(24,ring[index].angleTo(zen))
            

        if ring[index].collidedWith (zen):
            zen.health -=10
            ring[index].visible = False

    arrow.move()
    bow.draw()
    bow.moveTo(zen.x+15, zen.y+10)

    if keys.Pressed[K_SPACE]:

        arrow.visible = True
        arrow.moveTo(zen.x+15,zen.y+8)
        arrow.rotateTo(arrow.angleTo(mouse))
        arrow.setSpeed(24,arrow.angleTo(mouse))
        bow.rotateTo(bow.angleTo(mouse))
        bow.setSpeed(24,bow.angleTo(mouse))
        ba.play ()


    game.drawText("souls: " + str(soulsCollected),zen.x-10,zen.y + 80)
        


    if demons2complete==10:
        game.drawText("Level 2 Complete: ",400,80)
        game.over=True
        
    game.update (30)
game.over= False
game.stopMusic()

#Level 3
forest.draw ()
game.setBackground (forest)
soulsCollected = 0
demons3complete = 0
game.setMusic("rbl.ogg")
game.playMusic()
while not game.over and zen.health>0:
    game.processInput ()

    if keys.Pressed[K_RIGHT]:
        game.scrollBackground ("left",0)
        
        zen.x += 4
        zen.prevFrame()

 
    elif keys.Pressed[K_LEFT]:
        game.scrollBackground ("right",0)
        zen.x -= 4
        zen.nextFrame()
    
    else:
        game.scrollBackground ("right",0)
        zen.draw()

    for index in range (30):
        att[index].move()

        if att[index].collidedWith(zen):
            att[index].visible = False
            zen.health -= 15
            lg.play ()
    for index in range (20):
        att2[index].move()

        if att2[index].collidedWith(zen):
            att2[index].visible = False
            zen.health -= 15
            lg.play ()

    for index in range (30):
        att3[index].move()

        if att3[index].collidedWith(zen):
            att3[index].visible = False
            zen.health -= 20
            lg.play ()

        if zen.health <= 0:
            game.over = True
    for index in range (10):
        demons3[index].move()
        v = randint(1,2)
        demons3[index].moveTowards (zen,v)

        if demons3[index].collidedWith(zen):
            zen.health -= 10
            demons3[index].visible = False
            demons3complete += 1

    game.drawText("Health: " + str(zen.health),zen.x - 20,zen.y + 50)

    for index in range (10):
       
        if demons3[index].collidedWith (arrow):
            demons3[index].health -= 25
            arrow.visible = False
        if demons3[index].health <=0 and demons3[index].visible == True:
            demons3[index].visible=False
            demons3complete +=1
            soulsCollected += 1


    arrow.move()
    bow.draw()
    bow.moveTo(zen.x+15, zen.y+10)

    if keys.Pressed[K_SPACE]:
        arrow.visible = True
        arrow.moveTo(zen.x+15,zen.y+8)
        arrow.rotateTo(arrow.angleTo(mouse))
        arrow.setSpeed(24,arrow.angleTo(mouse))
        bow.rotateTo(bow.angleTo(mouse))
        bow.setSpeed(24,bow.angleTo(mouse))
        ba.play ()




    game.drawText("Health: " + str(zen.health),zen.x - 20,zen.y + 50)
    game.drawText("souls: " + str(soulsCollected),zen.x-10,zen.y + 80)

    if demons3complete==10:
        game.drawText("Level 3  Complete: ",400,80)
        game.over=True
              
    game.update (30)
game.over = False
game.stopMusic()
#GameOver

if zen.health <= 0:
    game.setMusic ("gameover.ogg")
    game.playMusic()
    zen.visible=False
    go1.draw ()
    game.update (30)
    game.wait (K_RETURN)

else:
    game.setMusic ("gametheme.ogg")
    game.playMusic()
    while not game.over  and demons3complete==10 and zen.health>0:
        game.processInput()
        level3s.draw ()
        arrow1.draw ()
        arrow1.moveTo (940,570)
        if arrow1.collidedWith(mouse) and mouse.LeftClick:
            game.over = True
        game.update(30)
    game.over= False
    while not game.over:
        game.processInput()
        zen.visible=False
        game.processInput()
        go2.draw ()
        arrow1.draw ()
        arrow1.moveTo (940,570)
        if arrow1.collidedWith(mouse) and mouse.LeftClick:
            game.over = True
        game.update(30)
    game.over= False
    while not game.over:
        game.processInput()
        go3.draw ()
        arrow1.draw ()
        arrow1.moveTo (940,570)
        if arrow1.collidedWith(mouse) and mouse.LeftClick:
            game.over = True
        game.update(30)
    game.over= False
    while not game.over:
        game.processInput()
        go4.draw ()
        arrow1.draw ()
        arrow1.moveTo (940,570)
        if arrow1.collidedWith(mouse) and mouse.LeftClick:
            game.over = True
        game.update(30)
    game.over= False
    game.stopMusic()
    game.update (30)
game.quit()
