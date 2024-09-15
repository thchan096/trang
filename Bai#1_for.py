# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 09:38:40 2024

@author: Student
"""

n = int(input("Nhập một số nguyên dương: "))
giaithua = 1
for n in range(1, n+1):
    giaithua *= n
print(f"Tính giai thừa của {n} =", giaithua)
