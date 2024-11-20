import random
class fruitquiz:
    def __init__(self):
        self.fruits={"apple":"red","watermelon":"green","banana":"yellow","cranberry":"red"}
    def quiz(self):
        while(True):
            fruit,color=random.choice(list(self.fruits.items()))
            print("What is the color of {}".format(fruit))
            useranswer=input()
            if useranswer.lower()==color:
                print("Correct answer")
            else:
                print("Wrong answer")
            option=int(input("If u want to play again enter 0 else enter 1:"))
            if option:
                break
print("welcome to fruit quiz:")
fq=fruitquiz()
fq.quiz()
