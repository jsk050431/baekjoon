for i in range(3):

    a = input()

    if not('z' in a):
        
        for j in range(2-i):
            input()

        b = int(a)+3-i

        if b%3 == 0 and b%5 == 0:
            print('FizzBuzz')
        elif b%3 == 0:
            print('Fizz')
        elif b%5 == 0:
            print('Buzz')
        else:
            print(b)

        break