'''
Exercise 1: Are You Rich?
Write a program that asks the user how much money they have in their wallet. The program
should output “You're rich!” if the user inputs $20 or more and “You're broke!” if the input is
less than $20.
'''

''' First Method using Functions '''
def get_wallet_amount():
    while True:
        user_input = input('How much money do you have in your wallet: ')
        if user_input.replace('.','',1).isdigit():
            wallet = float(user_input)

            if wallet >= 0:
                break
            else:
                print('Enter a positive numeric value.')

        else:
            print('Invalid output!Enter a valid numeric currency value.')
    return wallet

   
            
# Initialize `get_wallet_amount()` function            
wallet = get_wallet_amount()

# Validate if user is ``Rich` or `Broke`
if wallet >= 20:
    print(f"\nWallet cash balance: ${wallet}\nYou're rich!")
else:
    print(f"\nWallet cash balance: ${wallet}\nYou're broke!")
    

    
''' Second method without functions '''
while True:
    user_input = input('How much money do you have in your wallet: ')
    if user_input.replace('.','',1).isdigit():
        wallet = float(user_input)

        if wallet >= 0:
            break
        else:
            print('Enter a positive numeric value.')

    else:
        print('Invalid output!Enter a valid numeric currency value.')

# Validate if user is ``Rich` or `Broke`
if wallet >= 20:
    print(f"\nWallet cash balance: ${wallet:.2f}\nYou're rich!")
else:
    print(f"\nWallet cash balance: ${wallet:.2f}\nYou're broke!")

    

''' Exercise 2: Cats or Dogs
Write a program that performs the following steps:
1. Ask the user if they own any cats. (Yes/No answer)
2. Ask the user if they own any dogs. (Yes/No answer)
3. If the user's responses indicate that they have both cats and dogs, output “You must
really love pets!”
4. Otherwise, the output should be “Maybe you need more pets.”
The last step will apply if the user has cats but not dogs, dogs but not cats, or neither cats nor
dogs.
Write two different versions of this program: one that uses only if statements and another
that uses if-else statements
'''

def get_response(prompt):
    user_input = input(prompt).strip().lower()
    return user_input

''' IF statements only '''
cat_response = get_response('Do you own any cats? (yes/no):')
dog_response = get_response('Do you own any dogs? (yes/no):')

if cat_response == 'yes':
    if dog_response == 'yes':
        print('You must really love pets!')
    if dog_response == 'no':
        print('Maybe you need more pets.')


if cat_response == 'no':
    if dog_response == 'yes':
        print('Maybe you need more pets.')
    if dog_response == 'no':
        print('Maybe you need more pets.')



''' IF Else statement'''
cat_response = get_response('Do you own any cats? (yes/no):')
dog_response = get_response('Do you own any dogs? (yes/no):')

if cat_response == 'yes' and dog_response == 'yes' :
    print('You must really love pets!')
else:
    print('Maybe you need more pets.')




''' 
Exercise 3: True or False Quiz
Create a program that asks the user a few questions to which the user will respond either True
or False. Display all the questions with the correct answer and the user's answers at the end of
the program, along with the user's correct response rate (number of questions answered
correctly/number of questions).

'''
# Predefined questions and correct answers
question_prompts = [
    "Python is a case-sensitive programming language? (True or False): ",
    "In Python, a list is immutable? (True or False): ",
    "The elif keyword in Python is used for multiple conditional checks? (True or False): ",
    "Comments in Python start with a double forward slash (//)? (True or False): ",
    "The print() function in Python is used to display output to the console? (True or False): ",
    "In Python, the == operator is used for assignment? (True or False): ",
    "A tuple in Python can contain duplicate values? (True or False): ",
    "Indentation is optional in Python code? (True or False): ",
    "The break statement is used to exit a loop in Python? (True or False): ",
    "Python can be used for both scripting and object-oriented programming? (True or False): "]

correct_responses = [True, False, True, False, True, False, True, False, True, True]
user_responses = []
no_of_questions = len(question_prompts)
count = 0


def get_response(prompt):
    """
    Prompt the user for a True/False input.
    Validates input and returns a boolean value.
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ['true','false']:
            return user_input == 'true'
            break
        else:
            print("Please enter 'True' and 'False'")
    

# Display welcome message to user
print('Welcome to the Python Beginners assessment test.')
print('Provide True/False responses to the questions.\n')

for i,question in enumerate(question_prompts,1):
    response = get_response(f'{i}. {question}')
    user_responses.append(response)

for i in range(no_of_questions):
    if user_responses[i] == correct_responses[i]:
        count += 1

response_rate = (count / no_of_questions) * 100

print('\nCORRECT RESPONSES AND USER RESPONSES')
for i,(question,user_response,correct_response) in enumerate(zip(question_prompts,correct_responses,user_responses),1):
    print(f'Question {i}: {question}')
    print(f'Your answer: {user_response}')
    print(f'Correct answer: {correct_response}\n')
    
print(f'You answered {count} questions out of {no_of_questions} correctly!')
print(f'Your Score: {response_rate:.2f}%')