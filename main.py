import testing
from sys import *
import time
import json
import replit
variables = []
class output:
  def log(output):
    try:
      print(output)
    except NameError:
      print("Error: Output is not defined")
    
  def clear():
    try:
      system("clear")
    except:
      system("cls")
  def sleep(seconds):
    time.sleep(seconds)
  def require(module):
    replit.clear()
    while True:
      print("Downloading " + module + ".")
      time.sleep(0.5)
      replit.clear()
      print("Downloading " + module + "..")
      replit.clear()
      time.sleep(0.5)
      print("Downloading " + module + "...")
      replit.clear()
      time.sleep(0.5)
  def write(filename,content):
    thefile = open(filename,"w")
    thefile.write(content)
    thefile.close()
  def append(filename,content):
    thefile = open(filename,"a")
    thefile.write(content)
    thefile.close()
  def read():
    return input()