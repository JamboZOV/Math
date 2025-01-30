from src.core import random_primer as rp, check_answer, calculate as calc

def concol_app():
    #create_points = Points()

    while True:

        primer = rp()
        print(primer)

        correct_answer = calc(example=primer)
        #print(correct_answer)
        try:
            answer = float(input('введите ответ - '))
        except ValueError:
            print("вы ввели не число")
        else:    
            result = check_answer(user_answer=answer, correct_answer=correct_answer)

            if result == True:
                print("правильно")
        #create_points.plus_points()

            else:
                print("неправильно")
        #    create_points.minus_points()

        #print(f' у вас  {create_points.get_points()} очков')