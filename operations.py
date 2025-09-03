from data import DataProgram

data_program = DataProgram()

def run_operation(operation_type):
    operation_type = operation_type.upper().strip()

    if operation_type == 'TOTAL':
        balance = data_program.operate('READ')
        print(f"Current balance: {balance:09.2f}")

    elif operation_type == 'CREDIT':
        try:
            amount = float(input("Enter credit amount: ").strip())
        except ValueError:
            print("Please enter a valid number (digits with an optional decimal point).")
            return

        if amount <= 0:
            print("Please enter a positive number greater than zero.")
            return

        balance = data_program.operate('READ')
        if balance + amount > 999999.99:
            print("Operation cancelled: balance cannot exceed 999 999.99")
            return

        new_balance = data_program.operate('WRITE', balance + amount)
        print(f"Amount credited. New balance: {new_balance:09.2f}")

    elif operation_type == 'DEBIT':
        try:
            amount = float(input("Enter debit amount: ").strip())
        except ValueError:
            print("Please enter a valid number (digits with an optional decimal point).")
            return

        if amount <= 0:
            print("Please enter a positive number greater than zero.")
            return

        balance = data_program.operate('READ')
        if balance >= amount:
            new_balance = data_program.operate('WRITE', balance - amount)
            print(f"Amount debited. New balance: {new_balance:09.2f}")
        else:
            print("Insufficient funds for this debit.")

    else:
        print("Unknown operation.")
