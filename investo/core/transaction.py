class Transaction:

    def __init__(self, amount, date_time, transaction_name, transaction_type) -> None:
        self._amount = amount
        self._datetime = date_time
        self._transaction_type = transaction_type
        self._transaction_name = transaction_name