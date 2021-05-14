import json
import sys


class Budget:
    naira = u'\u20A6'
    db = {}

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

    def deposit_funds(self):
        print()
        category = input('Deposit funds to::: ').lower()
        last_deposit_amount = int(input(f"How much do you want to assign to {category} \n ::: {self.naira}"))
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

    def withdraw_funds(self):
        print()
        category = input('Withdraw funds from::: ').lower()
        amount = int(input('Enter Amount::: '))
        print(f'Withdraw {self.naira}{amount} from {category} balance?')
        print("1. Yes, Continue \n", end='2. Cancel \n')
        confirm = int(input('::: '))

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

    def compute_balance(self):
        print()
        category = input('Compute balance for ::: ').lower()
        try:
            self.read_file(category)
            print(f"The remaining balance in your {category} purse is {self.naira}" + str(self.Purse[category]['balance']))
        except (AttributeError):
            print(f'Budget balance for {category} not found')

    def transfer_balance(self):
        print()
        category = input('From:::').lower()
        to = input('to:::').lower()
        transfer_amount = int(input(f"Amount::: {self.naira}"))
        self.read_file(category)

        print(
            f"transfer {transfer_amount} from {category} balance to {to}? \n ", \
                end="1. Yes, Proceed \n 2. Cancel \n"
            )

        confirm = int(input(">>> "))
        if confirm == 1:
            if self.Purse[category]['balance'] < transfer_amount:
                print(f"Insuficient balance in {category} budget.")
                sys.exit()
            self.Purse[category]['balance'] -= transfer_amount
            self.write_to_file(category)

            self.read_file(to)
            self.Purse[to]['balance'] += transfer_amount
            self.write_to_file(to)
            print("Transfer Successful!")

        elif confirm == 2:
            print('Have a nice day!')
            sys.exit()
        else:
            print('Invalid response')
            self.transfer_balance()


# Budget app for ***clothing***, ***food***, ***entertainment***

app = Budget()
# app.deposit_funds()
# app.withdraw_funds()
# app.compute_balance()
# app.transfer_balance()
