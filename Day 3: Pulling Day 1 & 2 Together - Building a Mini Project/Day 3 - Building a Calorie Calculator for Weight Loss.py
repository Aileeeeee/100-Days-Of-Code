'''
Calorie Calculator for Weight Loss
Objective: Write a program that calculates the number of calories a person should consume to lose weight based on their Basal Metabolic Rate (BMR) and activity level.

Formula:
BMR for men = 10 × weight (kg) + 6.25 × height (cm) - 5 × age (years) + 5
BMR for women = 10 × weight (kg) + 6.25 × height (cm) - 5 × age (years) - 161
Calculate Total Daily Energy Expenditure (TDEE) based on activity level (e.g., Sedentary, Lightly active, Moderately active, Very active).
The program should:
Ask the user for their gender, age, weight, height, and activity level.
Calculate the BMR and TDEE.
Calculate the number of calories needed for weight loss (e.g., 500 calories less than TDEE for weight loss).
'''

activity_levels = [
    "Sedentary: little or no exercise, desk job",
    "Lightly active: light exercise/sports 1-3 days/week",
    "Moderately active: moderate exercise/sports 6-7 days/week",
    "Very active: hard exercise every day, or exercising 2 xs/day",
    "Extra active: hard exercise 2 or more times per day, or training for marathon, or triathlon, etc."
]
activity_multipliers = [1.2, 1.375, 1.55, 1.725, 1.9]
gender_options = ['male','female']
moderate_weight_loss = 500
aggressive_weight_loss = 1000


# Define function `get_user_input` to obtain user input
def get_user_input(prompt,data_type = float,positive = True):
    
    """
    Prompt the user for input and validate it.

    Args:
        prompt (str): The input prompt to display to the user.
        data_type (type): The type to convert the input into (default: float).
        positive (bool): Whether to validate for positive values (default: True).

    Returns:
        data_type: The validated user input.
    """
   
    if data_type == str:
        user_input = input(prompt).strip().lower()
        return user_input
    else:
        while True:
            user_input = input(prompt)
            # Validate user input to check if it is a numeric value
            if user_input.replace('.','',1).isdigit():
                value = data_type(user_input)

                if positive and value <= 0:
                    print('Please enter a valid positive value')
                else:
                    return value
                
            else:
                print('Invalid output! Please enter a valid numeric output')
       

# Define function `bmr` to calculate Basal Metabolic Rate 
def bmr(gender,age,weight,height):

    """
    Calculate the Basal Metabolic Rate (BMR) for a person.

    Args:
        gender (str): The gender ('male' or 'female').
        age (int): The age in years.
        weight (float): The weight in kilograms.
        height (float): The height in centimeters.

    Returns:
        float: The BMR in calories/day.
    """
    
    if gender == 'male':
        bmr = ((10 * weight) + (6.25 * height)) - (5 * age) + 5
    else:
        bmr = ((10 * weight) + (6.25 * height)) - (5 * age) - 161
    return bmr


# Define function `tdee` to calculate Total Daily Energy Expenditure
def tdee(patient_bmr, activity_level):
    
    """
    Calculate Total Daily Energy Expenditure (TDEE).

    Args:
        patient_bmr (float): The patient's Basal Metabolic Rate.
        activity_level (float): The multiplier based on activity level.

    Returns:
        float: Total Daily Energy Expenditure.
    """
    
    tdee = patient_bmr * activity_level
    return tdee


# Define function `calories_calculator` to calculate the number of calories required for patient to loss weight
def calories_calculator(patient_tdee):
    print('\nTo calculate the calorie intake for weight loss,please select your goal:')
    print("1. Moderate weight loss (0.5 kg or ~1 lb per week, ~500 calorie deficit/day)")
    print("2. Aggressive weight loss (1 kg or ~2 lbs per week, ~1000 calorie deficit/day)")

    goal = get_user_input("\nEnter 1 for moderate or 2 for aggressive weight loss: ", data_type=str)

    if goal == '1':
        calories = patient_tdee - moderate_weight_loss
    elif goal == '2':
        calories = patient_tdee - aggressive_weight_loss
    return calories
            
        
# Obtain patient's gender from user input
while True:
    gender = get_user_input('\nGender (male or female): ',data_type = str)
    if gender in gender_options:
        break
    else:
        print('Invalid output! Enter male or female')

# Obtain patient's age from user input
age = get_user_input('\nAge (in years): ',data_type = int)

# Obtain patient's weight from user input
weight = get_user_input('\nWeight (in kg): ',data_type = float)
    
# Obtain patient's height from user input
height = get_user_input('\nHeight (in cm): ',data_type = float)

# Obtain patient's activity level from user input
print('\nActivity Levels:')
for i,level in enumerate(activity_levels,1):
    print(f'{i}. {level}')

while True:
    activity_choice = get_user_input('\nEnter a number to pick an activity level: ',data_type = int)

    # Validate if `choice is within limit
    if 0 < activity_choice and activity_choice <= len(activity_levels):
        activity_level = activity_multipliers[activity_choice - 1]
        break
    else:
        print('Invalid choice ! The number selected is not within limit.')
    

# Calculate patient's Basal Metabolic Rate 
patient_bmr = bmr(gender,age,weight,height)

# Calculate patient' Total Daily Energy Expenditure
patient_tdee = tdee(patient_bmr, activity_level)

# Calculate calories needed for weight loss
calories_for_weight_loss = calories_calculator(patient_tdee)

print(f'Your daily calorie requirement for weight loss is {calories_for_weight_loss:,.2f} calories per day.')