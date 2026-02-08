from typing import List, Dict
from domain.person import Person
from domain.transaction import Transaction


class Group:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.people: List[Person] = []
        self.transactions: List[Transaction] = []

    def add_person(self, person: Person) -> None:
        self.people.append(person)

    def add_transaction(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)

    def total_expense(self) -> float:
        return sum(t.amount for t in self.transactions)

    def split_per_person(self) -> float:
        if not self.people:
            return 0.0
        return self.total_expense() / len(self.people)

    def balances(self) -> Dict[str, float]:
        """
        Returns:
            Dict[name, balance]
            positive  -> person should receive money
            negative  -> person owes money
        """
        split = self.split_per_person()
        balance: Dict[str, float] = {p.name: -split for p in self.people}

        for t in self.transactions:
            balance[t.paid_by.name] += t.amount

        return balance
