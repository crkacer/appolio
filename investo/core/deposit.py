from investo.core.transaction import Transaction
class Deposit(Transaction):

    def __init__(self, amount, date_time, transaction_name, transaction_type) -> None:
        super().__init__(amount, date_time, transaction_name, transaction_type)
