# -*- coding: utf-8 -*-
"""
Created on Wed May 23 11:50:41 2018

@author: Peeyush Goyal
"""

from pymongo import MongoClient

client=MongoClient("localhost",27017)
mydb=client.db_University

def add_client(Student_Name, Student_Age, Student_Roll_no, Student_Branch):
    unique_client=mydb.student.find_one({"Student Roll No":Student_Roll_no},{"_id":0})
    if unique_client:
        print "client already exists"
    else:
        mydb.student.insert(
                {
                  "Student Name":Student_Name,
                  "Student Age":Student_Age,
                  "Student Roll No":Student_Roll_no,
                  "Student Branch":Student_Branch 
                 })
        return "client added successfully"
def view_client(Student_Roll_no):
    student=mydb.student.find_one({"Student Roll No":Student_Roll_no},{"_id":0})
    if student:
        Name=student["Student Name"]
        Age=student["Student Age"]
        Roll_No=student["Student Roll No"]
        Branch=student["Student Branch"]
        return {
                  "Student Name":Name,
                  "Student Age":Age,
                  "Student Roll No":Roll_No,
                  "Student Branch":Branch 
                 }
    else:
        return "Sorry, No such student exists"


Name=raw_input("enter name")
Age=raw_input("enter Age")
Roll_No=raw_input("enter rollno")
Branch=raw_input("enter branch")

print add_client(Name,Age,Roll_No,Branch)

user = raw_input("Enter Roll_no to find: ")
user_data = view_client(user)

print user_data
