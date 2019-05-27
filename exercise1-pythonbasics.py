# -*- coding: utf-8 -*-
"""
Jacqueline Xu
iXperience Data Science
26 May 2019
Introduction to Python Assignment
"""

#%%

# FIZZBUZZ
# print numbers 1-100; if multiple of 3: print FIZZ,
# multiple of 5: print BUZZ, multiple of 15: FIZZBUZZ

for n in range(1, 101):
    if n % 15 == 0:
        print("FIZZBUZZ")
    elif n % 3 == 0:
        print("FIZZ")
    elif n % 5 == 0:
        print("BUZZ")
    else:
        print(str(n))
    
#%%
    
# ROMAN NUMERALS       
# assuming numbers won't be that much greater than 1000

dictionary = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
              90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}

def roman_numeral(n):
    ans = ""
    current = n
    while current != 0:
        for i in dictionary:
            if i <= current:
                divis = i
        num_times = current // divis
        ans += (dictionary[divis] * num_times)
        current = current % divis
    return ans

# testing
for n in range(1, 101):
    print(str(n) + ": " + roman_numeral(n))
for n in range(1, 101):
    print(str(n * 10) + ": " + roman_numeral(n * 10))

#%%
    
# ROT_13
# rotation of alphabet by 13

def rot_13(s):
    ans = ""
    for each in s:
        if each == " ":
            ans += each
        elif each.islower():
            i = (ord(each) - ord('a') + 13) % 26
            ans += chr(i + ord('a'))
        else:
            i = (ord(each) - ord('A') + 13) % 26
            ans += chr(i + ord('A'))
    return ans

# testing
print(rot_13("hello world"))

# ROT_N
# rotation of alphabet by n characters

def rot_n(s, n):
    ans = ""
    for each in s:
        if each == " ":
            ans += each
        elif each.islower():
            i = (ord(each) - ord('a') + n) % 26
            ans += chr(i + ord('a'))
        else:
            i = (ord(each) - ord('A') + n) % 26
            ans += chr(i + ord('A'))
    return ans

# testing
print(rot_n("Hello World", 14))
