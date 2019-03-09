#! /usr/bin/python3.6
#Codewars Link: https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

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
