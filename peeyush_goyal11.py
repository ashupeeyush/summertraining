# -*- coding: utf-8 -*-
"""
Created on Tue May 15 11:20:39 2018

@author: Peeyuh goyal
"""

l1 = input("Enter comma saperated no.s")
l2=list(l1)

def f1(x,y):return x+y
def f2(x,y):return x*y
    
def add():return reduce(f1,l2)
print "sum= ",add()

def Multiply():return reduce(f2,l2)
print "Multiply= ",Multiply()

def Largest():return max(l2)
print "Largest= ",Largest()

def Smallest():return min(l2)
print "Smallest= ",Smallest()

def Sorting():
    l2.sort()
    return l2

print "Sorting =",Sorting()


def Remove_Duplicates():
    l3=list(set(l2))
    return l3

print "without duplicates= ",Remove_Duplicates()



