# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 13:06:07 2022

@author: jingy
"""

def repeater(string,length,repeat):
    new_string = string[0:(length)]
    return new_string*repeat

def isPalindrome(s):
    s = str(s)
    if (len(s))%2 != 0:
        splice = int(((len(s)+1)/2))
        first_half = s[:splice]
        second_half = s[-1:(-splice)-1:-1]
    else:
       splice = int(((len(s))/2))
       first_half = s[:splice]
       second_half = s[-1:(-splice)-1:-1]
    if first_half == second_half:
        return True
    else:
        return False
    
def draw_grid(n):
    for i in range(1,n+1):
        for i in range(1,n+1):
            print(f'+ {"- "*4}',end='')
        print('+')
        for i in range(4):
            for i in range(1,n+1):
                print(f'{"|":10}',end='')
            print('|')
    for i in range(1,n+1):
        print(f'+ {"- "*4}',end='')
    print('+')
        
    
if __name__ == '__main__':
    print(repeater('jing',4,5))
    
    palindrome_odometer = []
    for i in range(100000,1000000):
        i = str(i)
        last_four = i[-1:-5:-1]
        if not isPalindrome(last_four):
            continue
        elif isPalindrome(last_four):
            i = int(i)
            i+=1
            i = str(i)
            last_five = i[-1:-6:-1]
            if isPalindrome(last_five):
                i = int(i)
                i+=1
                i = str(i)
                middle_four = i[1:5]
                if isPalindrome(middle_four):
                    i = int(i)
                    i+=1
                    i = str(i)
                    if isPalindrome(i):
                        i = int(i)
                        i-=3
                        palindrome_odometer.append(i)
    
    draw_grid(3)
    
    
                    

    
                
                
    