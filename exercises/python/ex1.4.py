import sys

balance = 1000

if len(sys.argv) < 2:
    print('Incorrect function selected')
else:
    mode = sys.argv[1]

    if mode == 'Withdraw':
        w_value = int(input('Enter amount to withdraw: '))
        
        if w_value <= balance:
            new_balance = balance - w_value
            print(f'Your new balance is: {new_balance}')
        else:
            print('Withdrawn amount exceeds current balance')

    elif mode == 'Deposit':
        d_value = int(input('Enter amount to deposit: '))
        new_balance = balance + d_value
        print(f'Your new balance is: {new_balance}')

    else:
        print('Incorrect function selected')



