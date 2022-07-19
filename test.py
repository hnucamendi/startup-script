import random

def createRands(counter, stop):
  rand1 = random.randint(1,100)
  rand2 = random.randint(1,100)
  rand3 = random.randint(1,100)
  rand4 = random.randint(1,100)
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
    print(str(counter) + " Sucess took " + str(counter) + " tries")
    return
  while counter < stop:
    counter += 1
    createRands(counter,stop)
    break
  exit

createRands(0, 1000)
