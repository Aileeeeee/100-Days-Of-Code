'''
Sum of Numbers
Write a function that takes any number of integers as arguments and returns their sum.

'''

def return_sum(*num):
    'A function that takes any number of integers as arguments and returns their sum.'
    total_number = 0
    for number in num:
        if not isinstance(number,(int,float)) or number < 0:
            return f"Invalid input. '{number}' not a valid positive numerical value"
        total_number += number
    return int(total_number) 


'''
Student Grades
Create a function that takes the name of a student as a regular argument, and then any number of grades as arbitrary positional arguments. The function should return the student’s name and their average grade.
'''
def student_grades(name,*grades):
    'A function that takes the name of a student their grades and return the student’s name and their average grade.'
    
    if not grades:
        return f'{name} has no grades entered to calculate average grade.'

    # Calculate student average grade
    average_grade = round(sum(grades) / len(grades),2)

    return f"{name}'s average grade: {average_grade}"



# Collect student_name from user input
name = input("Enter a student's name: ").strip().capitalize()


'''
 User Profile
Write a function that accepts a user’s first and last name as regular arguments, followed by arbitrary keyword 
arguments for extra details like age, country, etc. 
The function should return a string displaying the user’s full name and any extra details provided.
'''

def user_profile(first_name,last_name,**extra_details):
    print('\nUser Profile ')
    # Display full name
    print(f'Full name: {first_name} {last_name}')

    # Iterate through the dictionary
    for keyword,detail in extra_details.items():
        # Replace underscores with whitespace and capitalize each word
        formatted_keyword = keyword.replace('_',' ').title()
        print(f'{formatted_keyword} : {detail}')

# Collect user profile details from user inpu
first_name = input('Enter your first name: ').strip().capitalize()
last_name = input('Enter your last name: ').strip().capitalize()
gender = input('Enter your gender: ').strip().capitalize()
state_of_origin = input('Enter your state of origin: ').strip().capitalize()
local_govt = input('Enter your local government area: ').strip().capitalize()


user_profile(first_name,last_name,gender = gender,state_of_origin = state_of_origin ,local_govt= local_govt)
        
        
'''
Maximum Value
Write a function that accepts any number of numerical values and returns the largest one.

'''
def max_value(*nums):
    ' A function that accepts any number of numerical values and returns the largest one.'

    # Check if at least one value is entered .
    if not nums:
        return f'No values entered! Enter at least one numerical value.'

    # Validate all values entered are numerical values
    for number in nums:
        if not isinstance(number,(int,float)):
            return f'Invalid input! {number} is not  a numerical value.Enter a valid numeric value.'

    # Obtain the highest value from the numerical value provided
    largest = max(nums)
    return largest