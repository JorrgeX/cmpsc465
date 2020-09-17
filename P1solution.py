def convertToList(line):

    #Convert the input to list of ints and retrun
    converted = str.split(line)
    converted = [int(i) for i in converted]

    return converted

def convertToString(array):

    #Create and emptry string and iterate through the given array, converting
    #and adding each one to the string
    string = ""
    for i in array:
        string = string + str(i) + " "
    
    return string


def mergeTwo(array1, array2):

    #Define variable to keep track of each array length and the index being compared in each iteration
    firstLength = len(array1)
    secondLength = len(array2)
    firstCounter = 0
    secondCounter = 0
    solution = []

    #While each array still has unchecked indexes, go through each array and compare the indexes,
    #adding the lower one to the solution array and moving to that arrays next index
    if(firstLength >= 0 and secondLength >= 0):
        while((firstCounter) < firstLength and (secondCounter) < secondLength):
            if((firstCounter) < firstLength):
                if(array1[firstCounter] < array2[secondCounter]):
                    solution.append(array1[firstCounter])
                    firstCounter += 1
                else:
                    solution.append(array2[secondCounter])
                    secondCounter += 1

        #Add the rest of the indexes of an array if the end of the other is reached
        if((firstCounter) < firstLength):
            while((firstCounter) < firstLength):
                solution.append(array1[firstCounter])
                firstCounter += 1 
        elif((secondCounter) < secondLength):
            while((secondCounter) < secondLength):
                solution.append(array2[secondCounter])
                secondCounter += 1 

    #Return the sorted array
    return solution

def mergeSort(nums, start, end):

    #Base case of an array of length 1, return it
    if start >= end:
      return [nums[start]]
 
    #Split the input array into two seperate ones from the middle, then recursively
    #call mergeSort function
    left = mergeSort(nums, start, (start + end)//2)
    right = mergeSort(nums, ((start+end)//2+1), end)
    out = mergeTwo(left,right)
 
    return out


#Get the length of the array in line 1 and the values in line 2, then call mergeSort
#to sort this array
line1 = input()
line2 = input()
nums = convertToList(line2)
answer = mergeSort(nums, 0, len(nums)-1)
#print(convertToString(mergeSort(convertToList(line1)[0], convertToList(line2))))
print(convertToString(answer))