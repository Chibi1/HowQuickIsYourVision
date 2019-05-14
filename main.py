from microbit import *
import music
import random

gameStartUp = True
isDisplayingNumber = False
isWaitingForUser = False
level = 0
displayDuration = 1000
isCountingDown = False
countDown = 3
numberDisplayed = 0
count = 0

while True:
  if gameStartUp == True:
    music.play(music.CHASE, wait=False, loop=True)
    
  while gameStartUp == True:
    display.scroll("Press B to play")
    if button_b.was_pressed():
      music.stop()
      display.clear()
      gameStartUp = False
      isDisplayingNumber = True
      isCountingDown = True
      
  while isDisplayingNumber == True:
    sleep(2000)
    while isCountingDown == True:
      if countDown == 0:
        display.clear()
        isCountingDown = False
      else:
        display.show(str(countDown))
        sleep(1000)
        countDown-= 1
    sleep(random.randint(1,5)*1000)
    numberDisplayed = random.randint(0,9)
    display.show(str(numberDisplayed))
    sleep(100)
    display.clear()
    sleep(1000)
    isDisplayingNumber = False
    isWaitingForUser = True  
    
  while isWaitingForUser == True:
    if button_a.was_pressed() and button_b.was_pressed():
      if count == numberDisplayed:
        level += 1
        isWaitingForUser = False
        music.play(music.BA_DING)
    elif button_a.was_pressed() and count > 0:
      music.play('B5:1')
      count -= 1
    elif button_b.was_pressed() and count < 9:
      music.play('B5:1')
      count += 1
    display.show(str(count))
    
    
    
    
    