def get_lowest(num_arr):

    lowest = num_arr[0]

    # i as a variable takes value of a number present
    # in the array "num_arr" starting from 1 since
    # the starting value was already determined 
    # then comparisons take below between elements and 
    # the lowest number is found out from all

    for i in range(1,len(num_arr)):
        if(num_arr[i] < lowest):
            lowest = num_arr[i]

    return lowest