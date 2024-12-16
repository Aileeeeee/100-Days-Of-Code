'''
Fix the following code:
Print("Hello, welcome to the banking portal.")print("In this portal, you can
handle all of your banking needs.")
print("Please enter a selection from the following menu.")
Print("Type Login to log in")
print("Type Quit to quit")

'''
# Display a welcome message to the user
print("Hello, welcome to the banking portal.\n")

# Inform the user of the function of the program
print("In this portal, you can handle all of your banking needs.\n")

# A clear user friendly message
print("Please enter a selection from the following menu.\n")

# Print a message to tell the user how to begin and end the program
print("Type Login to log in\n")
print("Type Quit to quit\n")


'''
Fixing the Code: 
Each of the following code blocks includes at least one error that will prevent it from
running. Fix the errors and test to make sure the code runs as expected. Comments at the top
of each block will tell you what the code should do.

# display the text in quotation marks to an output block
Print("Python is fun!")

# Display the text in quotation marks to an output block
# without moving any of the existing code to a different line
print("Python is fun!") print("Python is also easy.")

# Display the text in quotation marks to an output block
# without moving any of the existing code to a different line
print
("Python is fun!")

# Change each variable name to an appropriate name for Python.
# Do not use the same variable name more than one time.
1-name = "Rebecca" # first name
&_name = "Roberts" # last name

# After changing the variable names, update the code below
# to print out each name.
print(1-name)
print(&_name)
'''

# Display the text in quotation marks to an output block
print("Python is fun!\n")

# Display the text in quotation marks to an output block
# without moving any of the existing code to a different line
print("Python is fun!") ; print("Python is also easy.\n")

# Display the text in quotation marks to an output block
# without moving any of the existing code to a different line
print("'Python is fun!'\n")

# Change each variable name to an appropriate name for Python.
# Do not use the same variable name more than one time.
first_name = "Rebecca" # first name
last_name = "Roberts" # last name

# After changing the variable names, update the code below
# to print out each name.
print(first_name)
print(last_name)


'''Broken Variables: 
Fix the following code to create three valid variable names. Add print() statements to
display the values associated with each variable and run the code to verify that there are no
errors.
-name="Alex"
__age = 35
2_list_of_states = ["Kentucky", "New Jersey"]
'''
# Declaring Variables
name="Alex"
age = 35
list_of_states = ["Kentucky", "New Jersey"]




'''
Broken Names
Fix the following code to create valid variable names:
thisisavalidvariablenamealthoughitisverylong=5
thisIsASecondVariableNmeThatIsVeryLong = "help"
print(thisisavalidvariablenamealthoughitislong)
print(thisIsASecondVariableNameThatIsVeryLong)
'''
num = 5
word_string = "help"

print(num)
print(word_string)
print('\n')





'''
Where Are You?
Create a script that prompts the user for the name of the state where they were born and the
name of the state where they live now. Save each value in its own variable and display the
input values to the user
'''
# Prompting user's input
place_of_birth = input('Enter the name of the state you were born: ').strip().capitalize()
current_location = input('Enter where you currently live: ').strip().capitalize()

print('Location Details:')
print('Place of Birth: ', place_of_birth)
print('Current Location: ', current_location)



'''
Simple Risk Assessment
Design a program that assesses basic health risks based on user input:

Smokers and those with a BMI ≥ 30 are at "High Risk."
Others are at "Low Risk."
'''

# Define a function that collects user input and checks if they are numeric
def get_user_input(prompt, data_type = int):
    # Collect user input 
    user_input = input(prompt)

    # Optimize user input to ensure user input is a positive numeric value
    while not user_input.replace('.','',).isdigit():
        print('Enter  a valid positive numeric value')
        user_input = input(prompt)
    return data_type(user_input)

# Obtain patient weight from user input
weight = get_user_input("Enter patient's weight(in kg): ", data_type = float )
# Check if user input is a positive value
while weight <= 0:
    print('Enter a valid positive numeric value')
    weight = get_user_input("Enter patient's weight(in kg): ", data_type = float )


# Obtain patient height from user input
height = get_user_input("Enter patient's height(in cm): ", data_type = float )
height = height / 100
# Check if user input is a positive value
while height <= 0:
    print('Enter a valid positive numeric value')
    height = get_user_input("Enter patient's height(in cm): ", data_type = float )
    height = height / 100

# Calculate patient bmi
bmi = weight / (height ** 2)

# Obtain patient's smoking status from user output
is_smoker = input('Is the patient a smoker? (yes/no): ').strip().capitalize()

# Check patient's health risk level
if bmi >= 30 or is_smoker.lower() == 'yes':
    risk_level = 'High risk'
else:
    risk_level = 'Low risk'
    
# Display output
print('\nPatient Summary:')
print("Patient's BMI: ", round(bmi,2))
print("Patient's Smoking Status: ", is_smoker)
print("Patient's Health Risk Level: ", risk_level)
