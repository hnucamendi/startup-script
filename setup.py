import random
import pywhatkit

## To run:
# pip install pywhatkit || pip3 install pywhatkit
# pip install random
# Python must be installed

def createRands(counter=1, stop=100):
  rand1 = random.randint(1,1000)
  rand2 = random.randint(1,1000)
  rand3 = random.randint(1,1000)
  rand4 = random.randint(1,1000)
  if counter < stop:
    exit
  twoArrayAdder([rand1,rand2], [rand3,rand4],counter, stop)

def arraySum(arr):
  for i in (0,len(arr)-1):
    sum = arr[i]
    return sum

def twoArrayAdder(arr1, arr2, counter, stop):
  sum1 = arraySum(arr1)
  sum2 = arraySum(arr2)
  if sum1 == sum2:
    print(str(counter) + " Success took " + str(counter) + " tries...Enjoy!")
    pywhatkit.playonyt("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    pywhatkit.take_screenshot("Pranked")
    return
  while counter < stop:
    counter += 1
    createRands(counter,stop)
    break
  exit

createRands()

