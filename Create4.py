#This is your starter file for the Creating a Quiz project
#The lines that start with a # are comments and will not show up in your code
#You should utilize this feature to leave notes about what variables are for
#And what operations your code is performing

#Try to have your program be inutitive for the user to interact with
#To help you get started, here are the first two lines of your program (feel free to edit these)

favoriteThing = 'Valorant' #fill this string with your quiz subject
print(f'Welcome to the {favoriteThing} quiz!')
print('Enter the corresponding number and press enter to submit your answer.')
input('Are you ready? Press enter to continue.')

# First Question
print('Question 1/3:')
ques1 = '1. Who does not belong in this group?'
print(ques1)
print('1 - Reyna \n2 - Raze\n3 - Vyse\n4 - Jett')
answer1 = int(input('Your Answer: '))

# Used dictionary to store choices per question (only for the sake of printing out later)
# Used question numbers as keys
first_choices = {
    1 : 'Reyna',
    2 : 'Raze',
    3 : 'Vyse',
    4 : 'Jett'
}

# Second Question
print('Question 2/3:')
ques2 = '2. What does Raze launch in her ultimate?'
print(ques2)
print('1 - Bazooka \n2 - Rocket\n3 - Boom Bot\n4 - Grenade')
answer2 = int(input('Your Answer: '))

# Used dictionary to store choices per question (only for the sake of printing out later)
second_choices = {
    1 : 'Bazooka',
    2 : 'Rocket',
    3 : 'Boom Bot',
    4 : 'Grenade'
}

# Third Question
print('Question 3/3:')
ques3 = '3. What does Reyna say when casting her blind?'
print(ques3)
print('1 - Steel of sight! \n2 - Stealing sight! \n3 - Parting their vision. \n4 - Blinded fools!')
answer3 = int(input('Your Answer: '))

# Used dictionary to store choices per question (only for the sake of printing out later)
third_choices = {
    1 : 'Steel of sight!',
    2 : 'Stealing sight!',
    3 : 'Parting their vision.',
    4 : 'Blinded fools!'
}

# Used dictionary to store correct answers
# Used question numbers as keys
correct_answers = {
    1: 3,
    2: 1,
    3: 2
}

# Messages to user if they got correct answers
correct1 = 'That\'s correct! Vyse is a sentinel.'
correct2 = 'Bingo! Here comes the party!'
correct3 = 'Way to go! Time to steal their souls as well.'

# Messages to user if they got incorrect answers
wrong1 = 'NT. This is a group of duelists. Vyse is a sentinel!'
wrong2 = 'Stop throwing! Lucky tho, you got Roza ulted.'
wrong3 = 'Wrong. Now you\'re blind and dead. (Definitely not an Omen blind reference)'

input('Getting your answers...')

# Used if-else condition in the string showing the answer
# Question 1
print(f'{ques1}\nYou Answered: {answer1} - {first_choices[answer1] if 1 <= answer1 <= 4 else "Please uninstall, bruh. THE CHOICES ARE 1 TO 4 ONLY!"}')
print(f'Correct Answer: {correct_answers[1]} - {first_choices[3]}')
if answer1 == correct_answers[1]:
    print(f'✅ {correct1}')
    score1 = 1
else:
    print(f'❌ {wrong1}')
    score1 = 0

# Question 2
print(f'\n{ques2}\nYou Answered: {answer2} - {second_choices[answer2] if 1 <= answer2 <= 4 else "Please uninstall, bruh. THE CHOICES ARE 1 TO 4 ONLY!"}')
print(f'Correct Answer: {correct_answers[2]} - {second_choices[1]}')
if answer2 == correct_answers[2]:
    print(f'✅ {correct2}')
    score2 = 1
else:
    print(f'❌ {wrong2}')
    score2 = 0

# Question 3
print(f'\n{ques3}\nYou Answered: {answer3} - {third_choices[answer3] if 1 <= answer3 <= 4 else "Please uninstall, bruh. THE CHOICES ARE 1 TO 4 ONLY!"}')
print(f'Correct Answer: {correct_answers[3]} - {third_choices[2]}')
if answer3 == correct_answers[3]:
    print(f'✅ {correct3}')
    score3 = 1
else:
    print(f'❌ {wrong3}')
    score3 = 0

# Gets the percentage of the scores per quiz item
percentage = ((score1 + score2 + score3)/3)*100
print(f'\nYour quiz percentage is {percentage:.2f}%')

