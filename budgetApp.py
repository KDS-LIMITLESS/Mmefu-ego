import json
from os import error


class Budget:
    naira = u'\u20A6'
    db = {}


    def deposit_funds(self, category: str):
        amount = int(input(f"How much do you want to assing for {category} \n >>>"))
        if category == 'food'.lower():
            self.db['FoodBudget'] = {'amount': amount, 'balance': 0}
            try:
                with open('zuriPurse.txt') as file:
                    data = json.load(file)
            except error:
                with open('zuriPurse.txt', 'w') as dbdata:
                    data = {}
                    data['FoodBudget'] = {'amount': amount, 'balance': 0}
                    json.dump(data, dbdata)

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
                        end=f'Your {category} budget balance is {self.naira}' + str(data['FoodBudget']['balance'])
                    )

                    

    def withdraw_funds(self):
        pass

    def compute_balance(self):
        pass

    def transfer_balance(self):
        pass

food = Budget()
food.deposit_funds("food")
