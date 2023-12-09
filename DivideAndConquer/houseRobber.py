#Problem: Given N number of houses along the street with some amount of money. Adjacent houses cannot be stolen. Find max amount that can be stolen.
#Solution: MAX(Rob 1st house and got to third house, Dont rob anything and got to 2st house).

def houseRober(houses, currentIndex):
  if currentIndex>=len(houses):
    return 0
  else:
    stealFirstHouse = houses[currentIndex] + houseRober(houses, currentIndex+2)
    skipFirstHouse = houseRober(houses, currentIndex+1)
    return max(stealFirstHouse, skipFirstHouse)
  
houses = [6,7,1,30,8,2,4]
print(houseRober(houses, 0))

