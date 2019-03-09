#! /usr/bin/python3.6
#Codewars Link: https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
#Problem Statement:
#A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.
#Here's how it works:
#
#digital_root(16)
#=> 1 + 6
#=> 7
#
#digital_root(942)
#=> 9 + 4 + 2
#=> 15 ...
#=> 1 + 5
#=> 6


def digital_root(n):

   #Create a function calcTotal to calculate the sum of the numbers, since it may have to be done multiple times
    def calcTotal(num):
        iTempNum=0                      #iTempNum will add up the sum of the numbers within the function, and be returned at the end
        
        for element in str(num):        #Create a string of the elements in the numbers, to loop through them
            iTempNum += int(element)    #Add each one to the iTempNum as we go through, converting back to int first
        
        return(iTempNum)                #Return the sum at the end

        
    while n > 10:                       #Continually call the function calcTotal until the number is less than 2 digits long
        n = calcTotal(n)
        
    return(n)                           
