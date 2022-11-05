def ask_number1(deco):
  def wrapper():
    deco()
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
  return wrapper
def num3(deco):
  def wrapper():
    deco()
    num1 = ''
    num3 = ''
    num2 = ''
    sign = ''
    sign2 = ''
    while num1 == '' and sign == '' and sign2 == '' and num2 == '' and num3 == '':
      try:
        num1 = int(input('Input your first number: '))
        num2 = int(input('Input your sekond number: '))	
        num3 = int(input('Input your third number: '))	
        sign = input('Input your sing: ')
        sign2 = input('Input your sekond sing: ')
        if sign == '+' or sign == '-' or sign == '*' or sign == '/':
          print(num1,sign,num2,sign2,num3)
        else:
          sign = ''
          raise ValueError
      except ValueError:
        print('You need to write normal evaluation')
  
      if sign == '+' and sign2 == '/':
        print(num1,sign,num2,sign2,num3,'=',num1+num2-num3)
      elif sign == '+' and sign2 == '+':
        print(num1,sign,num2,sign2,num3,'=',num1+num2-num3)
      elif sign == '+' and sign2 == '*':
         print(num1,sign,num2,sign2,num3,'=',num1+num2-num3)
      elif sign == '+' and sign2 == '-':
        print(num1,sign,num2,sign2,num3,'=',num1+num2-num3)
      elif sign == '/' and sign2 == '/':
        try:
          print(num1,sign,num2,sign2,num3,'=',num1/num2-num3)
        except:
          print('This is division by zero!!!')
          print('The end of program')
      elif sign == '/' and sign2 == '+':
        try:
          print(num1,sign,num2,sign2,num3,'=',num1/num2-num3)
        except:
          print('This is division by zero!!!')
          print('The end of program')
      elif sign == '/' and sign2 == '*':
        try:
          print(num1,sign,num2,sign2,num3,'=',num1/num2-num3)
        except:
          print('This is division by zero!!!')
          print('The end of program')
      elif sign == '/' and sign2 == '-':
        try:
          print(num1,sign,num2,sign2,num3,'=',num1/num2-num3)
        except:
          print('This is division by zero!!!')
          print('The end of program')
      elif sign == '-' and sign2 == '/':
        print(num1,sign,num2,sign2,num3,'=',num1-num2-num3)
      elif sign == '-' and sign2 == '+':
        print(num1,sign,num2,sign2,num3,'=',num1-num2-num3)
      elif sign == '-' and sign2 == '*':
         print(num1,sign,num2,sign2,num3,'=',num1-num2-num3)
      elif sign == '-' and sign2 == '-':
        print(num1,sign,num2,sign2,num3,'=',num1-num2-num3)
      elif sign == '*' and sign2 == '/':
        print(num1,sign,num2,sign2,num3,'=',num1*num2-num3)
      elif sign == '*' and sign2 == '+':
        print(num1,sign,num2,sign2,num3,'=',num1*num2-num3)
      elif sign == '*' and sign2 == '*':
         print(num1,sign,num2,sign2,num3,'=',num1*num2-num3)
      elif sign == '*' and sign2 == '-':
        print(num1,sign,num2,sign2,num3,'=',num1*num2-num3)
  return wrapper

@num3
@ask_number1

def Calculator():
  print('This  is Calculator')
Calculator()


