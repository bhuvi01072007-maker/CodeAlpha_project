stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145
}

total_investment = 0

print("=== Stock Portfolio Tracker ===")

while True:
    stock = input("Enter Stock Name (AAPL, TSLA, GOOGL, MSFT, AMZN): ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter Quantity: "))
        investment = stock_prices[stock] * quantity
        total_investment += investment

        print(f"Investment in {stock}: ${investment}")
    else:
        print("Stock not found!")

    choice = input("Do you want to add another stock? (yes/no): ").lower()

    if choice != "yes":
        break

print("\n===== Portfolio Summary =====")
print(f"Total Investment Value: ${total_investment}")


with open("portfolio_summary.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write(f"Total Investment Value: ${total_investment}")

print("Portfolio summary saved to 'portfolio_summary.txt'")