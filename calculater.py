
user_input = input('what you want to do:')
if user_input == 'quit':
    print('calculator is closed')
elif user_input == 'add':
    num1 = eval(input('enter a number:'))
    num2 = eval(input('enter a number:'))
    result =str(num1 + num2)
    print('the answer is' ' ' + result)
elif user_input == 'subtract':
    num1 = eval(input('enter a number:'))
    num2 = eval(input('enter a number:'))
    result = str(num1 - num2)
    print('the answer is' ' ' + result)
elif user_input == 'multiply':
    num1 = eval(input('enter a number:'))
    num2 = eval(input('enter a number:'))
    result = str(num1 * num2)
    print('the answer is' ' ' + result)
elif user_input == 'divide':
    num1 = eval(input('enter a number:'))
    num2 = eval(input('enter a number:'))
    result = str(num1 / num2)
    print('the answer is' ' ' + result)
else:
    print('unkown input')             
  
