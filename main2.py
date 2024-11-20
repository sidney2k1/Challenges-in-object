class flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word+"("+self.meaning+") "
flash=[]
print("Welcome to flashcard application:")
while(True):
    word=input("enter the word you want to add a flashcard for:")
    meaning=input("Enter the meaning of the word:")
    flash.append(flashcard(word,meaning))
    option=int(input("Input 0 if you want to add a flashcard or else input 1:"))
    if option:
        break
print("\nYour flashcard:")
for i in flash:
    print(">",i)