import json
import sys


class Budget:
    naira = u'\u20A6'
    db = {}


    def deposit_funds(self, category: str):
        last_deposit_amount = int(input(f"\n How much do you want to assing for {category} \n >>> {self.naira}"))
        if category == 'food'.lower():
            self.db['food'] = {'last_deposit_amount': last_deposit_amount, 'balance': 0}
            try: 
                with open('FoodPurse.txt') as file: # read file
                    data = json.load(file)
                    if not data['food']:
                        pass
            except (json.decoder.JSONDecodeError, FileNotFoundError, KeyError):
                with open('FoodPurse.txt', 'w') as dbdata: # create data if not exists 
                    data = {}
                    data['food'] = {'last_deposit_amount': last_deposit_amount, 'balance': 0}
                    json.dump(data, dbdata, indent=2)

            with open('FoodPurse.txt', 'w') as dbFile: # Save balance to file 
                if data['food']['balance'] == 0:
                    data['food']['balance'] += last_deposit_amount
                    data['food']['last_deposit_amount'] = self.db['food']['last_deposit_amount']
                    json.dump(data, dbFile, indent=2)
                else:
                    data['food']['balance'] += self.db['food']['last_deposit_amount']
                    data['food']['last_deposit_amount'] = self.db['food']['last_deposit_amount']
                    json.dump(data, dbFile, indent=2)
                print(
                    f"{self.naira}{last_deposit_amount} added to {category} budget. \n",\
                        end=f'Your {category} budget balance is {self.naira}' + str(data[category]['balance'])
                    )
        
        elif category == 'clothing'.lower():
            self.db['clothing'] = {'last_deposit_amount': last_deposit_amount, 'balance': 0}
            try: 
                with open('clothingPurse.txt') as file: # read file
                    data = json.load(file)
                    if not data['clothing']:
                        pass
            except (json.decoder.JSONDecodeError, FileNotFoundError, KeyError):
                with open('clothingPurse.txt', 'w') as dbdata: # create data if not exists 
                    data = {}
                    data['clothing'] = {'last_deposit_amount': last_deposit_amount, 'balance': 0}
                    json.dump(data, dbdata, indent=2)

            with open('clothingPurse.txt', 'w') as dbFile: # Save balance to file 
                if data['clothing']['balance'] == 0:
                    data['clothing']['balance'] += last_deposit_amount
                    data['clothing']['last_deposit_amount'] = self.db['clothing']['last_deposit_amount']
                    json.dump(data, dbFile, indent=2)
                else:
                    data['clothing']['balance'] += self.db['clothing']['last_deposit_amount']
                    data['clothing']['last_deposit_amount'] = self.db['clothing']['last_deposit_amount']
                    json.dump(data, dbFile, indent=2)
                print(
                    f"{self.naira}{last_deposit_amount} added to {category} budget. \n",\
                        end=f'Your {category} budget balance is {self.naira}' + str(data[category]['balance'])
                    )
        elif category == category == 'entertainment'.lower():
            self.db['entertainment'] = {'last_deposit_amount': last_deposit_amount, 'balance': 0}
            try: 
                with open('entertainmentPurse.txt') as file: # read file
                    data = json.load(file)
                    if not data['entertainment']:
                        pass
            except (json.decoder.JSONDecodeError, FileNotFoundError, KeyError):
                with open('entertainmentPurse.txt', 'w') as dbdata: # create data if not exists 
                    data = {}
                    data['entertainment'] = {'last_deposit_amount': last_deposit_amount, 'balance': 0}
                    json.dump(data, dbdata, indent=2)

            with open('entertainmentPurse.txt', 'w') as dbFile: # Save balance to file 
                if data['entertainment']['balance'] == 0:
                    data['entertainment']['balance'] += last_deposit_amount
                    data['entertainment']['last_deposit_amount'] = self.db['entertainment']['last_deposit_amount']
                    json.dump(data, dbFile, indent=2)
                else:
                    data['entertainment']['balance'] += self.db['entertainment']['last_deposit_amount']
                    data['entertainment']['last_deposit_amount'] = self.db['entertainment']['last_deposit_amount']
                    json.dump(data, dbFile, indent=2)
                print(
                    f"{self.naira}{last_deposit_amount} added to {category} budget. \n",\
                        end=f'Your {category} budget balance is {self.naira}' + str(data[category]['balance'])
                    )

    def withdraw_funds(self, category = "", amount = 0):
        print()
        print(f'\n Withdraw {self.naira}{amount} from {category} balance?')
        print("1. Yes, Continue \n", end='2. Cancel \n')
        confirm = int(input('>>> '))
        if confirm == 1 and category == 'food':
            with open('FoodPurse.txt') as file:
                foodPurse = json.load(file)
                if foodPurse[category]['balance'] < amount:
                    print(f"Insuficient balance in {category} budget")
                    sys.exit()
                with open('FoodPurse.txt', "w") as file:
                    foodPurse[category]['balance'] -= amount
                    json.dump(foodPurse, file, indent=2)
                    print(f"{amount} dedducted from your {category} budget balance. \n")
        
        elif confirm == 1 and category == 'clothing':
            with open('clothingPurse.txt') as file:
                clothingPurse = json.load(file)
                if clothingPurse[category]['balance'] < amount:
                    print(f"Insuficient balance in {category} budget")
                    sys.exit()
                with open('clothingPurse.txt', "w") as file:
                    clothingPurse[category]['balance'] -= amount
                    json.dump(clothingPurse, file, indent=2)
                    print(f"{amount} dedducted from your {category} budget balance. \n")

        elif confirm == 1 and category == 'entertainment':
            with open('entertainmentPurse.txt') as file:
                entertainmentPurse = json.load(file)
                if entertainmentPurse[category]['balance'] < amount:
                    print(f"Insuficient balance in {category} budget")
                    sys.exit()
                with open('entertainmentPurse.txt', "w") as file:
                    entertainmentPurse[category]['balance'] -= amount
                    json.dump(entertainmentPurse, file, indent=2)
                    print(f"{amount} dedducted from your {category} budget balance. \n")

        elif confirm == 2:
            print("Have a nice day!")
            sys.exit()
        else:
            print("invalid Command!")
        


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
app.deposit_funds('clothing')
app.withdraw_funds(category="food", amount=200)
app.compute_balance(category='entertainment')
app.transfer_balance(category="clothing", to="food")
