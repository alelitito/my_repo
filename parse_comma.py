#!/usr/bin/env python

f = open('C:/Users/ptito/Desktop/bsit3b.txt','r')

name_list = []

for i in f:
   name_list.append(str(i))

i = 0
while i < len(name_list):
   #name = (((name_list[i]).split()[1]) + ' ' + ((name_list[i]).split()[2])).replace(',','')
   name=((name_list[i]).split()[0]).replace(',','')
   print name
   i += 1



#(((name_list[i]).split()[1]) + ((name_list[i]).split()[2]))
