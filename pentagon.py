#!/usr/bin/env python3

# Created by: Khang Le
# Created on: Oct 2019
# This program uses user defined functions

def pentagon_perimeter(length1, length2, length3, length4, length5):
    perimeter = length1 + length2 + length3 + length4 + length5
    print('The perimeter of the pentagon is: {} '.format(perimeter))

def main():
    length1 = input("Enter a length of the pentagon: ")
    length2 = input("Enter a length of the pentagon: ")
    length3 = input("Enter a length of the pentagon: ")
    length4 = input("Enter a length of the pentagon: ")
    length5 = input("Enter a length of the pentagon: ")
    try:
        user_length1 = int(length1)
        user_length2 = int(length2)
        user_length3 = int(length3)
        user_length4 = int(length4)
        user_length5 = int(length5)
        if user_length1 > 0 and user_length2 > 0 and user_length3 > 0 and user_length4 > 0 and user_length5 > 0:
            pentagon_perimeter(user_length1, user_length2, user_length3, user_length4, user_length5)
        else:
            print("Numbers were < 0")
    except Exception:
        print("These are not integer")
        

if __name__ == "__main__":
    main()
