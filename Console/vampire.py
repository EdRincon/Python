print('Hi')
print('What´s your name?')  #Ask for thename
name = input()
print('What´s your age?')
age = int(input())
if name == 'Alice':
    print('Hi, Alice')
elif age < 12:
    print('You are not Alice kiddo')
elif age > 2000:
    print('unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie')
