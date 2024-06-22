import numpy as np
from math import cos
import datetime
from reclinks import *
from selfemail import *

def sigmoid(x):

  return 1 / (1 + np.exp(-x))

def invsigmoid(x):
  return 1-(1/ (3 + np.exp(-x)))
dataset = []
docfile = open("history.txt", 'r')
lineset  = docfile.readlines()
for i in lineset:
    dataset.append(i.strip().split('\t'))
# print(dataset)
temp = {}
for i in dataset:
    if  i[0] in temp.keys():
      temp[i[0]][1] +=1
      d = datetime.datetime.today() -  (datetime.datetime.strptime(i[1][:10], r"%Y-%m-%d") ) 
      temp[i[0]][0] +=int(str(d.days))
    else:
      temp.update({i[0]:[0,0]})
max_v = 0 
tgt = ''
for key in temp.keys():
   a_l = temp[key]
   cu_v = sigmoid(a_l[1])+invsigmoid(a_l[0])
  #  print(cu_v)
   if cu_v>max_v:
      max_v = cu_v
      tgt = key

urls = rec(tgt)
send_email("recomendations", urls,"eirprimeconsole@outlook.com")