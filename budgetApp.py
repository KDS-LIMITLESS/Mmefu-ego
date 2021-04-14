import json
import os


class Budget:
    naira = u'\u20A6'
    db = {}


    def __init__(self):
        pass

    def deposit_funds(self, category: str):
        print(os.getcwd())
        amount = int(input(f"How much do you want to assing for {category} \n >>>"))
        if category == 'food'.lower():
            self.db['FoodBudget'] = {'amount': amount, 'balance': 0}
            with open('zuriPurse.txt') as file:
                data = json.load(file)
                
                with open('zuriPurse.txt', 'w') as dbFile:
                    if data['FoodBudget']['balance'] == 0:
                        data['FoodBudget']['balance'] += amount
                        data['FoodBudget']['amount'] = self.db['FoodBudget']['amount']
                        print(self.db)
                        json.dump(data, dbFile)

                    else:
                        data['FoodBudget']['balance'] += self.db['FoodBudget']['amount']
                        data['FoodBudget']['amount'] = self.db['FoodBudget']['amount']
                        print(self.db)
                        json.dump(data, dbFile)
                    
        print(
            f"{self.naira}{amount} added to {category} budget. \n",\
                end=f'Your {category} budget balance is ' + str(data['FoodBudget']['balance'])
            )

                    

    def withdraw_funds(self):
        pass

    def compute_balance(self):
        pass

    def transfer_balance(self):
        pass

food = Budget()
food.deposit_funds("food")
