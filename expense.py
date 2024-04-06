def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)
    

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        
        choice = input('Enter your choice: ')

        match choice:
            case '1':
                amount = float(input('Enter amount: '))
                category = input('Enter category: ')
                add_expense(expenses, amount, category)

            case '2':
                print('\nAll Expenses:')
                print_expenses(expenses)

            case '3':
                print('\nTotal Expenses: ', total_expenses(expenses))

            case '4':
                category = input('Enter category to filter: ')
                print(f'\nExpenses for {category}:')
                expenses_from_category = filter_expenses_by_category(expenses, category)
                print_expenses(expenses_from_category)

            case '5':
                print('Exiting the program.')
                break

            case _ :
                print("Choice is doesn't exist. Try again")

if __name__ == "__main__":
    main()