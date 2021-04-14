import json
from os import error


class Budget:
    naira = u'\u20A6'
    db = {}


    def deposit_funds(self, category: str):
        amount = int(input(f"How much do you want to assing for {category} \n >>> {self.naira}"))
        if category == 'food'.lower() or category == 'clothing'.lower() or category == 'entertainment'.lower():
            self.db[category] = {'amount': amount, 'balance': 0}
            try:
                with open('zuriPurse.txt') as file:
                    data = json.load(file)
                    if not data[category]:
                        pass
            except (error, json.decoder.JSONDecodeError, FileNotFoundError, KeyError):
                with open('zuriPurse.txt', 'w') as dbdata:
                    data = {}
                    data[category] = {'amount': amount, 'balance': 0}
                    json.dump(data, dbdata)

            with open('zuriPurse.txt', 'w') as dbFile:
                if data[category]['balance'] == 0:
                    data[category]['balance'] += amount
                    data[category]['amount'] = self.db[category]['amount']
                    print(self.db)
                    json.dump(data, dbFile)
                else:
                    data[category]['balance'] += self.db[category]['amount']
                    data[category]['amount'] = self.db[category]['amount']
                    json.dump(data, dbFile)
                print(
                    f"{self.naira}{amount} added to {category} budget. \n",\
                        end=f'Your {category} budget balance is {self.naira}' + str(data[category]['balance'])
                    )
       

    def withdraw_funds(self):
        pass

    def compute_balance(self):
        pass

    def transfer_balance(self):
        pass

food = Budget()
food.deposit_funds("clothing")
