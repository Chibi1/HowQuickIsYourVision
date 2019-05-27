from microbit import *
import music
import random

def main():
  #initialising values
  currentTemp = 0
  isGameStartUp = True
  isDisplayingNumber = False
  isWaitingForUser = False
  isGameOver = False
  level = 1
  displayDuration = 500
  isCountingDown = False
  
  GO = Image('99999:'
              '99999:'
              '99999:'
              '99999:'
              '99999:')

  #run game
  while True:
    if isGameStartUp == True:
      music.play(music.CHASE, wait=False, loop=True)
      display.scroll("Press B", wait=False, loop=True)
    while isGameStartUp == True:
      if button_b.was_pressed():
        currentTemp = temperature()
        music.stop()
        display.scroll("Temp: " + str(currentTemp))
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
      music.play(music.POWER_UP, wait=False)
      display.scroll("Level " + str(level))
      music.stop()
      #display countdown
      while isCountingDown == True:
        if countDown == 0:
          display.show(GO)
          music.play('C6:3')
          display.clear()
          isCountingDown = False
        else:
          music.play('C5:1')
          display.show(str(countDown))
          sleep(1000)
          countDown-= 1
      #display integer for set amount of time
      sleep(random.randint(2,5)*1000)
      numberDisplayed = random.randint(0,9)
      display.show(str(numberDisplayed))
      sleep(displayDuration / (2**level))
      display.clear()
      sleep(1000)
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
      music.play(music.PYTHON, wait=False, loop=True)
      if level == 1:
        display.scroll("You need to get your eyes checked")  
        isGameOver = False
        isGameStartUp = True
      else:
        display.scroll("You can see " + str(round(displayDuration / 2**(level - 1))) + "ms")
        level = 0
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
    