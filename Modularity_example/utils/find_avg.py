from utils.marks_input import get_marks
from utils.find_min import get_lowest

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
