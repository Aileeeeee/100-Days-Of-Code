'''
Write a script that does the following:

- Print numbers from 1 to 10 using a for loop.
- the script to print the square of each number from 1 to 10.
'''
print('First problem')
# Iterate through a range of number and print each number 
for num in range(1,11):
    print(num)

print('\nSecond problem')
# Iterate through a range of numbers and print the square of each number from 1 - 10
for num in range(1,11):
    print(num ** 2)


'''
Write a script that does the following:

Repeatedly ask the user to guess a secret number (e.g., 7).
Stop the loop when the user guesses the correct number and display a success message.
Bonus: Add a counter to track how many attempts the user needed to guess the correct number.

'''
# Import random module
import random

# Print welcome message to user
print("Welcome to the 'Guess the secret number game'")

# Generate a number using the randrange() function
secret_number = random.randrange(1,20)

while True:
    # Getting user input
    user_input = input('\nDo you want to continue? (yes/no): ')
    if user_input == 'no':
        print('Goodbye! See you in your next login.')
        break

    elif user_input == 'yes':
        counter = 0
        user_entry = int(input('\nEnter a number (Hint: The number is between the range of 1 - 20): '))

        while user_entry != secret_number:
            print('Try again! You guessed wrongly!')
            user_entry = int(input('\nEnter a number (Hint: The number is between the range of 1 - 20): '))
         
            counter += 1
        if user_entry == secret_number:
            print("You've guessed correctly!")
            print(f'\nThe secret number is {secret_number}.')
            break
    else:
        print("Enter a valid output! 'yes or no'")
                             
  
print(f'You guessed {counter} times !')


'''
1. Track Patient Weight
Write a Python script to evaluate whether each patient’s weight meets or exceeds a specified standard weight. The program should:

- Take a list of patient weights (in kg) as input.
- Compare each patient's weight to a standard weight (e.g., 75 kg).
- For each patient, display whether they meet, exceed, or fall short of the standard.

At the end, summarize the total number of patients who are:
- Below the standard weight.
- At or above the standard weight.

'''
weights = [70, 80, 75, 68, 90, 74,45,85,90,78]
standard_weight = 75

# Define a function `track_weight` to compare patient weight to standard weight
def track_weight(weight_list,standard_weight):

    # Declare the variables `below_standard_count` and `equal_above_standard_count`
    below_standard_count = 0
    equal_above_standard_count = 0
    # Iterate over weight list
    for i ,weight in enumerate(weight_list,1):
        
        # Check if patient's weight meet, exceed, or fall short of the standard. 
        if weight == standard_weight:
            print(f'patient {i}: Meets the standard weight')
            equal_above_standard_count += 1
        elif weight < standard_weight:
            print(f'patient {i}: Falls short the standard weight')
            below_standard_count += 1
        else: 
            print(f'patient {i}: Exceeds the standard weight')
            equal_above_standard_count += 1

    return equal_above_standard_count,below_standard_count

# Unpack variables 
equal_above_standard_count,below_standard_count = track_weight(weights,standard_weight)

print('\nSummary: ')
print(f'Below standard weight: {below_standard_count} patients.')
print(f'At or Above standard weight: {equal_above_standard_count} patients.')
