import time
import os
import subprocess
from os import system, name
import sys
def getData(fullData, dataType):
  '''Parses data from String, and returns substring just after given data header.
  How to use:
  Input: getData(";DESCRIPTION;This is a table;END;", ";DESCRIPTION;")
  Output:
  This is a table'''
  returnSubstringStart = 0
  returnSubstringEnd = 5
  for x in range(0, len(fullData)):
    if fullData[x:x + len(dataType)] == dataType:
      returnSubstringStart = x + len(dataType)
  for x in range(int(returnSubstringStart - 1), len(fullData)):
    if fullData[x:x + 5] == ";END;":
      returnSubstringEnd = x
      break
  return fullData[returnSubstringStart:returnSubstringEnd]



def drawLoading(intro, mode):
  


  ''' 
  Prints big 'ol letters, in a graphical way
  credit to https://www.geeksforgeeks.org/clear-screen-python/
  '''
  if mode == "fowards":
    for x in range(0, len(intro)):
      print(intro[x])
      time.sleep(0.1)
      if x < len(intro)-1:
        clear()
  if mode == "backwards":
    x = (len(intro)-1)
    while x >=0:
      print(intro[x])
      time.sleep(0.1) 
      if x < 0:
        clear()
      x = x-1

            
          
def slowlyText(text, mode):
  #if period, waiter is 1, if next line marker, ignore and print next line
  placeCounter = 0
  if mode == "serious":
    while placeCounter <= len(text):
      waiter = 0.1
      if placeCounter <= len(text)-1:
        if text[placeCounter] == ".":
          waiter=1
      if placeCounter <= len(text)-4:
        if text[placeCounter:int(placeCounter+4)] == ";/n;":
          print()
          placeCounter+=4
      if placeCounter <= len(text)-1:
        sys.stdout.write(text[placeCounter])
        sys.stdout.flush()
        time.sleep(waiter)
      if placeCounter <= len(text)+1:
        if not text[placeCounter:int(placeCounter+3)] == ";/n;":
          placeCounter+=1
  if mode == "CyberKnight":
    while placeCounter <= len(text):
      waiter = 0.01
      if placeCounter <= len(text)-1:
        if text[placeCounter] == ".":
          waiter=0.1
      if placeCounter <= len(text)-4:
        if text[placeCounter:int(placeCounter+4)] == ";/n;":
          print()
          placeCounter+=4
      if placeCounter <= len(text)-1:
        sys.stdout.write(text[placeCounter])
        sys.stdout.flush()
        time.sleep(waiter)
      if placeCounter <= len(text)+1:
        if not text[placeCounter:int(placeCounter+3)] == ";/n;":
          placeCounter+=1
        
def logoPrinter(brandName):
    print("logohere")

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def scrollingText(arrayToScroll):
  starter = 0
  while starter < len(arrayToScroll)-5:
    time.sleep(1)
    clear()
    for x in range(starter,starter+5):
      print(arrayToScroll[x])
    starter = starter+1
