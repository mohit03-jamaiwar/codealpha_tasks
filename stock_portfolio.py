stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "AMZN": 120,
    "MSFT": 310
}
ch="yes"
u_portfolio=[]
while ch=="yes":
    stock=[]
    in_stock=input("Enter stock name:\t").upper()
    no_share=int(input("Enter no of shares owned:\t"))
    if in_stock in stock_prices:
        stock=[in_stock,no_share,stock_prices[in_stock],stock_prices[in_stock]*no_share]
        u_portfolio.append(stock)
        print(f"The price of {in_stock} is {stock_prices[in_stock]*no_share}.\n")
    else:
        print("Stock not found")
        exit()
    ch=input("Want to enter more stock?(yes/no):\t").lower()

print(u_portfolio)
for _ in range(len(u_portfolio)):
    print(f'''Stock: {u_portfolio[_][0]}, 
Shares: {u_portfolio[_][1]}, 
Price: {u_portfolio[_][2]}, 
Total Value: {u_portfolio[_][3]}\n''')

s=input("want to save portfolio in text file?(y/n)").lower()
if s=="y":
    res_file=open("portfolio_summary.txt","w+")
    res_file.write("Stock Portfolio Summary\n")
    i=1
    for i in range(len(u_portfolio)):
        res_file.write(f"Stock: {u_portfolio[_][0]}\nShares: {u_portfolio[_][1]}\nPrice: {u_portfolio[_][2]}\nTotal Value: {u_portfolio[_][3]}\n\n")
    print("Portfolio saved in file \"portfolio_summary.txt\"")
