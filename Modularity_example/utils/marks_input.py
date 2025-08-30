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