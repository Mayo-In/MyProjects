import random
import string

class project:
    def password_Gen(self, user_choice):
        pass_list = []
        password = ''
        special_chars = ['@', '#', '$', '&']
        if user_choice.lower() in ["weak", "strong"]:
            if user_choice.lower() == "weak":
                for i in range(1,3):
                    pass_list.append(random.choice(string.ascii_letters))
                for i in range(1,3):
                    random_num = random.randrange(0,3)
                    pass_list.append(special_chars[random_num])
                for i in range(1,3):
                    pass_list.append(str(random.randint(0,9)))
                for j in pass_list:
                    password = password + j

            elif user_choice.lower() == "strong":
                for i in range(1,5):
                    pass_list.append(random.choice(string.ascii_letters))
                for i in range(1,3):
                    random_num = random.randrange(0,3)
                    pass_list.append(special_chars[random_num])
                for i in range(1, 5):
                    pass_list.append(str(random.randint(0,9)))
                for j in pass_list:
                    password = password + j
            print(password)
        else: print("Please check your choice again!!")

obj = project()
choice = input("How would you like your password - weak or strong ? ")
obj.password_Gen(choice)