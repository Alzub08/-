def ask_number1():
  num1 = ''
  sign = ''
  num2 = ''
  while num1 == '' and sign == '' and num2 == '':
    try:
      num1 = int(input('Input your first number: '))
      num2 = int(input('Input your sekond number: '))	
      sign = input('Input your sing: ')
      if sign == '+' or sign == '-' or sign == '*' or sign == '/':
        print(num1,sign,num2)
      else:
        sign = ''
        raise ValueError
    except ValueError:
      print('You need to write normal evaluation')

    if sign == '+':
      print(num1,sign,num2,'=',num1+num2)
    elif sign == '/':
      try:
        print(num1,sign,num2,'=',num1/num2)
      except:
        print('This is division by zero!!!')
        print('The end of program')
    elif sign == '-':
      print(num1,sign,num2,'=',num1-num2)
    if sign == '*':
      print(num1,sign,num2,'=',num1*num2)
  
def ask_number12():
	age = int(input('Input your age: '))
	print('Your age is', age)
	print('The end of program')

ask_number1()