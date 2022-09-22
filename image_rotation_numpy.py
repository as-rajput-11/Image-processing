import numpy as np
from PIL import Image


img = Image.open("3.jpg")
m = np.array(img) 
l1 = m


##############################90*degree###################


# l1 = [[1,2,3],[4,5,6],[7,8,9]]
l2 = []
def transpose(l1, l2):


 for i in range(len(l1[1])):
  # print(i)
  row =[]
  for item in l1:

   row.append(item[i])
  l2.append(row)
 return l2
transpose(l1, l2)

l2.reverse()
# print(l2) 

im = Image.fromarray(np.uint8(l2)).convert('RGB')
im.save("l90.png")



##############################180*degree###################

l3= l2
l4 = []
def transpose(l3, l4):

 for i in range(len(l3[1])):
  # print(i)
  row =[]
  for item in l3:

   row.append(item[i])
  l4.append(row)
 return l4
transpose(l3, l4)

l4.reverse()
# print(l4)   
 
im = Image.fromarray(np.uint8(l4)).convert('RGB')
im.save("l180.png")



#######################270*degree##################################


l5= l4
l6 = []
def transpose(l5, l6):


 for i in range(len(l5[1])):
  # print(i)
  row =[]
  for item in l5:

   row.append(item[i])
  l6.append(row)
 return l6
transpose(l5, l6)

l6.reverse()
# print(l6)   
 
im = Image.fromarray(np.uint8(l6)).convert('RGB')
im.save("l270.png")


#################################360*degree####################################

l7= l6
l8 = []
def transpose(l7, l8):


 for i in range(len(l7[1])):
  # print(i)
  row =[]
  for item in l7:

   row.append(item[i])
  l8.append(row)
 return l8
transpose(l7, l8)

l8.reverse()
# print(l6)   
 
im = Image.fromarray(np.uint8(l8)).convert('RGB')
im.save("l360.png")



