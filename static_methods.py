import random

class StateUtils:
    
    @staticmethod
    def check_login_state():
        number = random.randint(1,3)
        if number == 1:
            print("Authenticated")
        elif number == 2:
            print("Unauthenticated")
        else:
            print("Login Error!")

    
    @staticmethod
    def check_sale_state():
        number = random.randint(1,3)
        if number == 1:
            print("Success")
        elif number == 2:
            print("Pending")
        else:
            print("Closed")
    