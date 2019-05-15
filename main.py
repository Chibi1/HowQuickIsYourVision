from microbit import *
import music
import random

def main():
  #initialising values
  isGameStartUp = True
  isDisplayingNumber = False
  isWaitingForUser = False
  isGameOver = False
  level = 1
  displayDuration = 1000
  isCountingDown = False
  displayDuration = 250

  #run game
  while True:
    if isGameStartUp == True:
      music.play(music.CHASE, wait=False, loop=True)
    #displays start up text and begins game if b was pressed
    while isGameStartUp == True:
      display.scroll("Press B to play")
      if button_b.was_pressed():
        music.stop()
        display.clear()
        isGameStartUp = False
        isDisplayingNumber = True
        isCountingDown = True

    #displays countdown before showing random digit for a set amount of time
    while isDisplayingNumber == True:
      answer = 0
      countDown = 3
      numberDisplayed = 0
      sleep(1000)
      music.play(music.POWER_UP, wait=False, loop=True)
      display.scroll("Level " + str(level))
      music.stop()
      #display countdown
      while isCountingDown == True:
        if countDown == 0:
          music.play('C6:3')
          display.clear()
          isCountingDown = False
        else:
          music.play('C5:1')
          display.show(str(countDown))
          sleep(1000)
          countDown-= 1
      #display integer for set amount of time
      sleep(random.randint(2,6)*1000)
      numberDisplayed = random.randint(0,9)
      display.show(str(numberDisplayed))
      sleep(displayDuration / level)
      display.clear()
      sleep(1000)
      display.scroll("What is your answer?")
      isDisplayingNumber = False
      isWaitingForUser = True  

    #take in the users answer and compares it to previously displayed number
    #to determine whether the users answer is correct
    while isWaitingForUser == True:
      if button_b.was_pressed():
        if answer == numberDisplayed:
          level += 1
          isWaitingForUser = False
          isDisplayingNumber = True
          isCountingDown = True
          music.play(music.BA_DING, wait=False)
          flashCorrectAnswer(answer)
        else:
          music.play(music.WAWAWAWAA)
          isWaitingForUser = False
          isGameOver = True
      elif button_a.was_pressed():
        music.play('B5:1')
        answer += 1
        answer %= 10
      display.show(str(answer))

    while isGameOver == True:
      if level == 1:
        display.scroll("You need to get your eyes checked")  
      else:
        display.scroll("You can see " + str(displayDuration / (level - 1)) + "ms")
        isGameOver = False
        isGameStartUp = True

#flashes the passed answer on the display
def flashCorrectAnswer(answer):
  for i in range(0,5):
    display.clear()
    sleep(100)
    display.show(str(answer))
    sleep(100)
    
if __name__ == "__main__":
  main()
    