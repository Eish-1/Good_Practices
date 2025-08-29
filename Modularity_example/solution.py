def get_marks():
    try: 
        marks = int(input("Enter marks: "))

        while(marks<0 or marks>100):
            print("Invalid input! retry")
            marks = int(input("Enter marks: "))

    except Exception as e:
        print("Error: ",e,"has occured most likey " \
        "invalid input! Need an integer dear")

        return None
    
    return marks

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
    


def get_average():
    num = 5  
    num_arr = []
    while(num):
        num -= 1                    # decrementing num variable
        mark  = get_marks()         # calling in function to take in input
        num_arr.append(mark)

    sum_of_marks = 0
    for number in num_arr:
        sum_of_marks += number      # incrementing

    sum_of_marks -= get_lowest(num_arr)   # removing the lowest marks from the total 
    return sum_of_marks/4


'''The main function where every defined step will
   excute.
'''
def main():
    print(get_average())

main()