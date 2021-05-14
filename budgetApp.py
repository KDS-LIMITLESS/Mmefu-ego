import json
import sys


class Budget:
    naira = u'\u20A6'
    db = {}

    def __init__(self) -> None:
        self.deposit_funds(category="clothing")
        self.deposit_funds(category="entertainment")
        self.deposit_funds(category="food")

    def read_file(self, category):
        if category == 'food':
            with open('FoodPurse.txt') as file:
                self.Purse = json.load(file)
                return self.Purse
        if category == 'clothing':
            with open('clothingPurse.txt') as file:
                self.Purse = json.load(file)
                return self.Purse
        if category == 'entertainment':
            with open('entertainmentPurse.txt') as file:
                self.Purse = json.load(file)
                return self.Purse

    def write_to_file(self, category):
        if category == 'food':
            with open('FoodPurse.txt', 'w') as file:
                json.dump(self.Purse, file, indent=2)

        if category == 'clothing':
            with open('clothingPurse.txt', 'w') as file:
                json.dump(self.Purse, file, indent=2)

        if category == 'entertainment':
            with open('entertainmentPurse.txt', 'w') as file:
                json.dump(self.Purse, file, indent=2)

    def deposit_funds(self, category=""):
        last_deposit_amount = int(input(f"\n \n How much do you want to assign for {category} \n >>> {self.naira}"))
        self.db[category] = {'last_deposit_amount': last_deposit_amount, 'balance': 0}

        try:
            self.read_file(category)
          
        except (json.decoder.JSONDecodeError, FileNotFoundError, KeyError):
            self.Purse = {}
            self.Purse[category] = {'last_deposit_amount': last_deposit_amount, 'balance': 0}
            self.write_to_file(category)

        if self.Purse[category]['balance'] == 0:
            self.Purse[category]['balance'] += last_deposit_amount
            self.Purse[category]['last_deposit_amount'] = self.db[category]['last_deposit_amount']
            self.write_to_file(category)

            print(
                f"{self.naira}{last_deposit_amount} added to {category} budget. \n",\
                    end=f'Your {category} budget balance is {self.naira}' + str(self.Purse[category]['balance'])
                )
        else:
            self.Purse[category]['balance'] += self.db[category]['last_deposit_amount']
            self.Purse[category]['last_deposit_amount'] = last_deposit_amount
            self.write_to_file(category)

            print(
                f"{self.naira}{last_deposit_amount} added to {category} budget. \n",\
                    end=f'Your {category} budget balance is {self.naira}' + str(self.Purse[category]['balance'])
                )

    def withdraw_funds(self, category="", amount=0):
        print()
        print(f'\n Withdraw {self.naira}{amount} from {category} balance?')
        print("1. Yes, Continue \n", end='2. Cancel \n')
        confirm = int(input('>>> '))

        if confirm == 1:
            self.read_file(category)
            if self.Purse[category]['balance'] < amount:
                print(f"Insuficient balance in {category} budget")
                sys.exit()
            self.Purse[category]['balance'] -= amount
            self.write_to_file(category)
            print(f"{amount} dedducted from your {category} budget balance. \n")

        elif confirm == 2:
            print("Have a nice day!")
            sys.exit()
        else:
            print("invalid Command!")
            self.withdraw_funds(category=category, amount=amount)

    def compute_balance(self, category=""):
        if category == "food":
            with open("FoodPurse.txt") as file:
                balance = json.load(file)
                print(f"The remaining balance in your {category} purse is {self.naira}" + str(balance[category]['balance']))
        elif category == "clothing":
            with open("clothingPurse.txt") as file:
                balance = json.load(file)
                print(f"The remaining balance in your {category} purse is {self.naira}" + str(balance[category]['balance']))
        elif category == "entertainment":
            with open("entertainmentPurse.txt") as file:
                balance = json.load(file)
                print(f"The remaining balance in your {category} purse is {self.naira}" + str(balance[category]['balance']))
        else:
            print(f"Budget for {category} not found in database!")

    def transfer_balance(self, category="", to=""):

        with open("FoodPurse.txt") as file:
            foodFile = json.load(file)
        with open("clothingPurse.txt") as file:
            clothingFile = json.load(file)
        with open("entertainmentPurse.txt") as file:
            entertainmentFile = json.load(file)

        if (category == "food" and to == "clothing"):
            transfer_amount = int(input(f"Enter Amount \n >>> {self.naira}"))
            print(
                f"transfer {transfer_amount} from {category} balance to {to}? \n ", \
                    end="1. Yes, Proceed \n 2. Cancel \n"
                )
            confirm = int(input(">>> "))
            if confirm == 1:
                if foodFile[category]['balance'] < transfer_amount:
                    print(f"Insuficient balance in {category} budget.")
                    sys.exit()
                with open("FoodPurse.txt", 'w') as Ffile:
                    foodFile[category]['balance'] -= transfer_amount
                    json.dump(foodFile, Ffile, indent=2)
                with open("clothingPurse.txt", 'w') as Cfile:
                    clothingFile['clothing']['balance'] += transfer_amount
                    json.dump(clothingFile, Cfile, indent=2)
                    print(f"Transfer Successful!")
            else:
                sys.exit()

        if (category == "food" and to == "entertainment"):
            transfer_amount = int(input(f"Enter Amount \n >>> {self.naira}"))
            print(
                f"transfer {transfer_amount} from {category} balance to {to}? \n ", \
                    end="1. Yes, Proceed \n 2. Cancel \n"
                )
            confirm = int(input(">>> "))
            if confirm == 1:
                if foodFile[category]['balance'] < transfer_amount:
                    print(f"Insuficient balance in {category} budget.")
                    sys.exit()
                with open("FoodPurse.txt", 'w') as Ffile:
                    foodFile[category]['balance'] -= transfer_amount
                    json.dump(foodFile, Ffile, indent=2)
                    print(f"Transfer Successful! Your new balance is {self.naira}" + foodFile[category]['balance'])
                with open("entertainmentPurse.txt", 'w') as Efile:
                    entertainmentFile['entertainment']['balance'] += transfer_amount
                    json.dump(entertainmentFile, Efile, indent=2)
                    print(f"Transfer Successful!")
            else:
                sys.exit()

        if (category == "clothing" and to == "food"):
            transfer_amount = int(input(f"Enter Amount \n >>> {self.naira}"))
            print(
                f"transfer {transfer_amount} from {category} balance to {to}? \n ", \
                    end="1. Yes, Proceed \n 2. Cancel \n"
                )
            confirm = int(input(">>> "))
            if confirm == 1:
                if clothingFile[category]['balance'] < transfer_amount:
                    print(f"Insuficient balance in {category} budget.")
                    sys.exit()
                with open("clothingPurse.txt", 'w') as Cfile:
                    clothingFile[category]['balance'] -= transfer_amount
                    json.dump(clothingFile, Cfile, indent=2)
                with open("FoodPurse.txt", 'w') as Ffile:
                    foodFile['food']['balance'] += transfer_amount
                    json.dump(foodFile, Ffile, indent=2)
                    print(f"Transfer Successful!")
            else:
                sys.exit()

        if (category == "clothing" and to == "entertainment"):
            transfer_amount = int(input(f"Enter Amount \n >>> {self.naira}"))
            print(
                f"transfer {transfer_amount} from {category} balance to {to}? \n ", \
                    end="1. Yes, Proceed \n 2. Cancel \n"
                )
            confirm = int(input(">>> "))
            if confirm == 1:
                if clothingFile[category]['balance'] < transfer_amount:
                    print(f"Insuficient balance in {category} budget.")
                    sys.exit()
                with open("clothingPurse.txt", 'w') as Cfile:
                    clothingFile[category]['balance'] -= transfer_amount
                    json.dump(clothingFile, Cfile, indent=2)
                with open("entertainmentPurse.txt", 'w') as Efile:
                    entertainmentFile['entertainment']['balance'] += transfer_amount
                    json.dump(entertainmentFile, Efile, indent=2)
                    print(f"Transfer Successful!")
            else:
                sys.exit()
        if (category == "entertainment" and to == "food"):
            transfer_amount = int(input(f"Enter Amount \n >>> {self.naira}"))
            print(
                f"transfer {transfer_amount} from {category} balance to {to}? \n ", \
                    end="1. Yes, Proceed \n 2. Cancel \n"
                )
            confirm = int(input(">>> "))
            if confirm == 1:
                if entertainmentFile[category]['balance'] < transfer_amount:
                    print(f"Insuficient balance in {category} budget.")
                    sys.exit()
                with open("entertainmentPurse.txt", 'w') as Efile:
                    entertainmentFile[category]['balance'] -= transfer_amount
                    json.dump(entertainmentFile, Efile, indent=2)
                with open("FoodPurse.txt", 'w') as Ffile:
                    foodFile['food']['balance'] += transfer_amount
                    json.dump(foodFile, Ffile, indent=2)
                    print(f"Transfer Successful!")
            else:
                sys.exit()

        if (category == "entertainment" and to == "clothing"):
            transfer_amount = int(input(f"Enter Amount \n >>> {self.naira}"))
            print(
                f"transfer {transfer_amount} from {category} balance to {to}? \n ", \
                    end="1. Yes, Proceed \n 2. Cancel \n"
                )
            confirm = int(input(">>> "))
            if confirm == 1:
                if entertainmentFile[category]['balance'] < transfer_amount:
                    print(f"Insuficient balance in {category} budget.")
                    sys.exit()
                with open("entertainmentPurse.txt", 'w') as Efile:
                    entertainmentFile[category]['balance'] -= transfer_amount
                    json.dump(entertainmentFile, Efile, indent=2)
                with open("clothingPurse.txt", 'w') as Cfile:
                    clothingFile['clothing']['balance'] += transfer_amount
                    json.dump(clothingFile, Cfile, indent=2)
                    print('Transfer Successful!')
            else:
                sys.exit()

# Budget app for ***clothing***, ***food***, ***entertainment***


app = Budget()
app.deposit_funds('food')
#app.withdraw_funds(category="food", amount=100000)
# app.compute_balance(category='entertainment')
# app.transfer_balance(category="clothing", to="food")
