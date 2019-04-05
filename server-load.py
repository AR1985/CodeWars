#!"/usr/bin/env python"

import time     #Optional, only used to measure performance of code

#Problem Statement: To support a website, there are 4x VMs running on a server, which have recorded the sessions occuring during the first 10 minutes of the hour.
#The times have been rounded to the nearest minute, and recorded in the tuples below, labelled 'sessions_1' ... 'sessions_4'.  For example 'sessions_1' are recorded from
#the first VM, sessions_2 from the second VM, etc. The time format used to record the sessions is hh:mm, and (6, 8) represents a session which uses started at 00:06
#(6 minutes into the hour), and ended at 00:08 (8 minutes into the hour), and lasted 2 minutes.  Keep in mind the session is inclusive of the start time, and exclusive of the finish time.
#For example, the tuple (6, 8) includes minutes 6 and 7, but does not include any time in minute 8.
#During which minute of the hour was the server most heavily loaded?

#Defining the datasets manually
sessions_1 = (
    (8,9),
    (1,4),
    (2,3),
    (5,6),
    (6,8))

sessions_2 = (
    (1,4),
    (2,3),
    (5,7),
    (6,9),
    (6,10))

sessions_3 = (
    (1,4),
    (2,3),
    (5,7),
    (6,9),
    (6,10),
    (4,5),
    (4,6))

sessions_4 = ((3,5),)*1000000


timeStart = time.time()  #Optional, only used to measure performance of code - take the initial start time


#*** Function buildOut takes a sessionList tuple, and re-creates it as a list, filling in the time elapsed during the session.***#
def buildOut(tuple):
    results = []    #Actual list of results to return

    for i in range(len(tuple)): #Iterate through items in tuple
        tempResults = [] #Temporary list to build up, and pass to results list
        for j in range(0, (tuple[i][1]-tuple[i][0])):
            tempResults.append(tuple[i][0] + j)    #Loop through values of sessions start to end, to build  out the temporary list for one set of values
        results.append(tempResults) #Add the temporary list to the results list, for one set of values at a time
        
    return(results) #Return the list of lists, with each all the values built out


#*** Function aggregate takes the list data generated in the function buildOut as 'list' and aggregates the results in a dictionary called 'results'  The dictionary with the new values added gets returned. ***#
def aggregate(list, results):
    for i in range(len(list)):      #Find session in list of sessions
        for j in range(len(list[i])):       #Find item within session in list
            if list[i][j] in results.keys():      #If item is in list
                results[list[i][j]] += 1       #Increment count representing item

            else:
                results[list[i][j]] = 1      #If items is not in list, create it.

    return(results) #Return the results at the end


#*** Main function***#
#1. Call buildOut function, to turn all 'sessions_X' tuples into lists, which will be built out with all the minutes the sessions were running
sessionList_1 = buildOut(sessions_1)
sessionList_2 = buildOut(sessions_2)
sessionList_3 = buildOut(sessions_3)
sessionList_4 = buildOut(sessions_4)

#2. (Optional) Debug values for troubleshooting
#print(sessionList_1)       #These are debug values, uncomment to see results of function calls to buildOut, if required
#print(sessionList_2)       #These are debug values, uncomment to see results of function calls to buildOut, if required
#print(sessionList_3)       #These are debug values, uncomment to see results of function calls to buildOut, if required
#print(sessionList_4)       #These are debug values, uncomment to see results of function calls to buildOut, if required (This has 1000000 values, don't uncomment)


#3. Take all the 'sessionList_X' variables and aggregate all results in a dictionary called totalDict, which will count the occurance of each number              
totalDict = {}
totalList = aggregate(sessionList_1, totalDict)
totalList = aggregate(sessionList_2, totalDict)        
totalList = aggregate(sessionList_3, totalDict)
totalList = aggregate(sessionList_4, totalDict)


#4. Calculate the maximum number of occurances, so it doesn't have to be calculated twice when output
maxOccurance = max(totalDict, key=totalDict.get)

#5. Print the results
print('The server was most heavily loaded during minute {}, with {} sessions'.format(maxOccurance, totalList.get(maxOccurance)))

#6. #Optional, only used to measure performance of code - output the elapsed time to the user
elapsedTime = time.time() - timeStart
print('The runtime was: {} seconds'.format(round(elapsedTime,2)))
