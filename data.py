class DataProgram:
    MAX_DIGITS = 6

    def __init__(self):
        self.storage_balance = 1000 * 100

    def operate(self, operation_type, balance=None):
        operation_type = operation_type.upper()

        if operation_type == 'READ':
            return self.storage_balance / 100

        elif operation_type == 'WRITE' and balance is not None:
            balance_cents = int(round(balance * 100))

            int_part = balance_cents // 100
            frac_part = balance_cents % 100

            if int_part >= 10**self.MAX_DIGITS:
                int_part = int_part % (10**self.MAX_DIGITS)

            self.storage_balance = int_part * 100 + frac_part
            return self.storage_balance / 100

        else:
            raise ValueError("Invalid operation or missing balance for WRITE.")
