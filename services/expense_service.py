# services/expense_service.py
from typing import Dict, List, Tuple


class ExpenseService:
    @staticmethod
    def settle_debts(
        balances: Dict[str, float]
    ) -> List[Tuple[str, str, float]]:
        """
        Returns:
            List of (debtor, creditor, amount)
        """
        debtors = []
        creditors = []

        for person, balance in balances.items():
            if balance < 0:
                debtors.append([person, -balance])
            elif balance > 0:
                creditors.append([person, balance])

        settlements: List[Tuple[str, str, float]] = []

        i = j = 0
        while i < len(debtors) and j < len(creditors):
            debtor, debt = debtors[i]
            creditor, credit = creditors[j]

            amount = min(debt, credit)
            settlements.append((debtor, creditor, amount))

            debtors[i][1] -= amount
            creditors[j][1] -= amount

            if debtors[i][1] == 0:
                i += 1
            if creditors[j][1] == 0:
                j += 1

        return settlements
