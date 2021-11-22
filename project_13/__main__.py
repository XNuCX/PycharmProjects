import abc
class Account(abc.ABC):
    def __init__(self, owner:str, amount=0):
        super(Account, self).__init__()
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount):

        if type(amount) is not int:
            raise ValueError("please use int for amount")
        else:
            # self.validate_transaction(self, amount)
            self._transactions.append(amount)
    @property
    def balance(self):
        return self.amount + sum(self._transactions)
    @staticmethod
    def validate_transaction(account, amount_to_add):
        if account.amount + amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!")
        else:
            account.amount = account.amount + amount_to_add
            return f"New balance: {account.balance}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"
    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"
    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, item):
        return self._transactions[item]
    # def __next__(self):
    def __reversed__(self):

        return reversed(self._transactions)

    def __gt__(self, value):
        if self.amount < value.amount:
            return True
        else:
            return False
    def __lt__(self, value):
        if self.amount > value.amount:
            return True
        else:
            return False
    def __ge__(self, value):
        if self.amount <= value.amount:
            return True
        else:
            return False
    def __le__(self, value):
        if self.amount >= value.amount:
            return True
        else:
            return False
    def __eq__(self, value):
        if self.amount == value.amount:
            return True
        else:
            return False
    def __ne__(self, value):
        if self.amount != value.amount:
            return True
        else:
            return False
    def __add__(self, other):
        name = f"{self.owner}&{other.owner}"
        amount = self.amount + other.amount
        transactions = self._transactions + other._transactions
        new_acc = Account(name, amount)
        new_acc._transactions = transactions
        return new_acc
acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)



