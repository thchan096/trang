# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:49:45 2024

@author: Student
"""

x = float(input("Nhập x = "))
while x < -99 or x > 99:
    x = float(input("Nhập lại x = "))
print("Gia tri da nhap:", x)