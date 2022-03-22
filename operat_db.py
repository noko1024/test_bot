#coding UTF-8

import json

def Help():
    print("mode:add")
    print("add new data to database\n")

def Add_db():
    print("cominng soon")

def Main():
    print("\nDataBaseOperat")
    str = input("select mode:")
    if str == "help":
        Help()
    elif str == "add":
        Add_db()
    else :
        print("try again")

if __name__ == "__main__":
    while True:
        Main()