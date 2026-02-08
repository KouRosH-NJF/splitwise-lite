from domain.person import Person


class Transaction:
    def __init__(
        self,
        title: str,
        amount: float,
        paid_by: Person
    ) -> None:
        if amount <= 0:
            raise ValueError("Transaction amount must be positive")

        self.title: str = title
        self.amount: float = amount
        self.paid_by: Person = paid_by

    def __repr__(self) -> str:
        return (
            f"Transaction(title='{self.title}', "
            f"amount={self.amount}, "
            f"paid_by={self.paid_by.name})"
        )
