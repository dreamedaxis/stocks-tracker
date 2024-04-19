import tkinter as tk
import yfinance as yf

class StockReaderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Stock Reader")

        self.master.geometry("400x200")

        self.master.configure(bg="Lightblue")

        self.symbol_label = tk.Label(self.master, text="Enter Stock Symbol:", bg="lightgray")
        self.symbol_label.pack()

        self.symbol_var = tk.StringVar(self.master)
        self.symbol_entry = tk.Entry(self.master, textvariable=self.symbol_var)
        self.symbol_entry.pack()

        self.price_label = tk.Label(self.master, text="", bg="lightgray", font=("Helvetica", 14))
        self.price_label.pack()

        self.fetch_button = tk.Button(self.master, text="Fetch Price", command=self.fetch_stock_price, bg="blue", fg="white")
        self.fetch_button.pack()

    def fetch_stock_price(self):
        symbol = self.symbol_var.get().strip().upper()
        if symbol:
            try:
                stock = yf.Ticker(symbol)
                current_price = stock.history(period="1d")["Close"].iloc[-1]
                self.price_label.config(text=f"Current Price for {symbol}: ${current_price:.2f}")
            except Exception as e:
                self.price_label.config(text=f"Error fetching price for {symbol}", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    stock_reader_app = StockReaderApp(root)
    root.mainloop()



#PART 2 setstock notis
import yfinance as yf
from plyer import notification
import tkinter as tk


def get_stock_price(ticker):


    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    current_price = data['Close'].iloc[-1]
    return current_price


def check_price(ticker, target_price):

    current_price = get_stock_price(ticker)

    if current_price < target_price:
        notification_title = f"{ticker} Price Alert!"
        notification_message = f"Current Price: ${current_price:.2f}\nTarget Price: ${target_price:.2f}\nPrice dropped below the target."
        notification.notify(
            title=notification_title,
            message=notification_message,
            app_icon=None,
            timeout=10
        )


def track_stock():

    ticker = ticker_entry.get()
    target_price = float(price_entry.get())

    check_price(ticker, target_price)

root = tk.Tk()
root.title("Stock Price Tracker")

root.geometry("400x300")  # Width x Height
root.configure(bg="lightblue")  # Background color

tk.Label(root, text="Enter Stock Ticker:", font=("Helvetica", 12), bg="lightblue").pack(pady=10)
ticker_entry = tk.Entry(root, font=("Helvetica", 12))
ticker_entry.pack(pady=5, padx=20, ipadx=50, ipady=5)

tk.Label(root, text="Enter Target Price ($):", font=("Helvetica", 12), bg="lightblue").pack(pady=10)
price_entry = tk.Entry(root, font=("Helvetica", 12))
price_entry.pack(pady=5, padx=20, ipadx=50, ipady=5)

track_button = tk.Button(root, text="Track", command=track_stock, font=("Helvetica", 14), bg="green", fg="white")
track_button.pack(pady=20, ipadx=20, ipady=8)

root.mainloop()
