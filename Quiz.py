print("------Wellcome to the QUIZ ---")
score = 0
question_no = 0

#start---
playing = input('Do you want to start \n (yes/no) ?').lower()
if playing == 'yes':
    question_no += 1
    #------1st question
    ques = input(f'\n{question_no}. what does CPU stand for? \na. computer processing unit\nb. central printing unit\nc. central processing unit\n ').lower()
    if ques == 'c':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is -->c. central processing unit')

# ------2nd question
    question_no += 1
    ques = input(f'\n{question_no}. What is a correct syntax to output "Hello World" in Python? \na.echo("Hello World"); \nb. p("Hello World") \nc. print("Hello World")\nd. echo "Hello World"\n').lower()
    
    if ques == 'c':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is -->c. print("Hello World")')

# -----3rd question
    question_no += 1
    ques = input(f'\n{question_no}. what does RAM stand for? \na.random access memory\nb. random access machine\nc. reallocating memory\n').lower()
    
    if ques == 'a':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is -->a.random access memory')

# -----4th question
    question_no += 1
    ques = input(f'\n{question_no}. How do you insert COMMENTS in Python code? \na. //comments \nb. /comments\nc. #comments\n').lower()
    
    if ques == 'c':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is -->  c. #comments')


# -----5th question
    question_no += 1
    ques = input(f'\n{question_no}. what does ROM stand for?\na. read on memory\nb. read only memory\nc. rewrite on memory\n ').lower()
    
    if ques == 'b':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is -->b. read only memory')
    # -----6th question
    question_no += 1
    ques = input(f'\n{question_no}.total number of predefined keywords present in python____(numerical answer type)\n').lower()
    
    if ques == '36':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is -->36 keywords')
    print(f'\nnumber of question is {question_no}')
    print(f'your score is {score}')
    try:
        percentage = (score *100)/question_no
    except ZeroDivisionError:
        print('0% quetions are correct')
    print(f'{percentage}% questions are correct.')


else:
    print('thankyou you are out of a game.')

