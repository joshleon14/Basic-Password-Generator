# password Generator
import random

class passwordCreator:
    password = ""
    chars = "abcdefghijklmnopqrstuvwxyz.,/\|[]{}""::`~<>!@#$%^&*()-=_+1234567890"

    def numberGenerator(self):
        return random.randint(1,50)

    def passwordGenerator(self):
        length = self.numberGenerator()
        for i in range(length):
            self.password += random.choice(self.chars)
        self.showPassword(length)

    def showPassword(self, length):
        print("The predefined Length is: {}".format(length))
        print("This is your new password: \n{} ".format(self.password))


passwordCreator().passwordGenerator()
