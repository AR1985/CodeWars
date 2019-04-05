#!/python3

##Problem Statement:
##Monte Carlo Simulation to find the E(X) of the min within a subset
##
##This program defines a dataset, picks 6 random numbers, and then performs a Monte Carlo simulation to find the E(X) that it would return.
##This was used to validate a calculation, to answer the question of "Given a random subset, of a list of numbers, 
##what is the expected value of the minimum of that subset).

import random

#define the dataset
dataset = [12, 7, 5, 2, 7, 8, 3, 16, 12, 4, 13]


#Function to pick the value for the subset
def minOfSubset(dataset):

    subset=[]
    chosenList=[]    #List of array positions already chosen, to prevent duplicates

    #Randomly pick 6 numbers from the dataset list, to populate the subset list
    for i in range(0,5):
        numToPick=random.randint(0,len(dataset)-1)
        if(numToPick not in chosenList):   #Check that list entry has not already been entered into subset 
            subset.append(dataset[numToPick])
            chosenList.append(numToPick)

    "print('The lowest value in the subset is: ', min(subset))" #Commented out for now to save on processing speed.  Remove comments if you wish to display the minimum in the subset each time.

    return(min(subset))



#Main Program - Monte Carlo Simulation to find the E(X), of the minimum value within the subset.  This is done by performing a Monte Carlo simulation, to see the average.
valuesReturned=[]

for i in range(0,1000000):
    valuesReturned.append(minOfSubset(dataset))


print('After ', i+1,' loops, the E(X) of the minimum number found within the subset is: ', sum(valuesReturned)/len(valuesReturned))
