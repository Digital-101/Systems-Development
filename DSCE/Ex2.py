try:
    age = int(input("Enter your age: "))
    gender = input('Enter your gender: ').lower()
    marital_status = input('Enter your marital status: ').lower()

    if gender == 'male' and age < 30:
        print('You are a bachelor!')
    elif gender == 'male' and age >= 30 and age <65:
        if marital_status == 'married':
            print('You are a settled man!')
        else:
            print('You are a bachelor looking for love!')
    elif gender == 'female' and age < 30 and age <65:
        print('You are a young lady!')
    elif gender == 'female' and age >= 30 and age <65:
        if marital_status == 'married':
            print('You are a happy homemaker!')
        else:
            print('You are a single lady looking for love!')
    elif age >= 65:
        print("You are a golden ager!")
        
except ValueError:
    print('Error! Invalid Input')