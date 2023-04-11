'''
2023-04-06
@HuiyuanZheng02
'''
import random

def main():
    print("Welcome to the guessing game!")
    while True:
        # generate a random number between 1 and 100
        num = random.randint(1, 100)
        print("I'm thinking of a number between 1 and 100.")
        print("You have 4 chances to guess the number.")
        cheat_mode = False
        count = 1
        while count <= 4:
            guess = input(f"[{count}]：您猜的数是？")
            # check if the user wants to cheat
            if guess == "help" or guess == "8888":
                print(f"[作弊模式]您要猜的数字是 {num}")
                cheat_mode = True
                continue
            try:
                guess = int(guess)
                if guess < 1 or guess > 100:
                    print("请输入一个[1,100]范围内的整数")
                    continue
            except:
                print(f"请输入一个[1,100]范围内的整数 invalid literal for int() with base 10: '{guess}'")
                continue
            if guess == num:
                print("您猜对了！")
                break
            elif guess < num:
                print("您猜的数太小了！")
            else:
                print("您猜的数太大了！")
            count += 1
        print(f"您已经猜了{count-1}次，要猜的数是 {num}")
        play_again = input("继续游戏(Y/N)?...")
        if play_again.lower() != "y":
            break
    print("Thanks for playing!")

    

if __name__ == '__main__':
    main()