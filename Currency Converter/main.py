import tkinter as tk
from tkinter import ttk, messagebox

# Fixed exchange rates relative to USD
exchange_rates = {
    "USD": 1.0,
    "EUR": 0.93,
    "INR": 83.5,
    "JPY": 145.0,
    "GBP": 0.81,
    "AUD": 1.5,
    "CAD": 1.35
}

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_cb.get()
        to_currency = to_currency_cb.get()

        if from_currency == "" or to_currency == "":
            messagebox.showwarning("Warning", "Please select both currencies.")
            return

        # Convert amount to USD first, then to target currency
        amount_in_usd = amount / exchange_rates[from_currency]
        converted_amount = amount_in_usd * exchange_rates[to_currency]

        result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI setup
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")
root.resizable(False, False)

title_label = tk.Label(root, text="💱 Currency Converter", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Input Frame
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
amount_entry = tk.Entry(frame)
amount_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="From:").grid(row=1, column=0, padx=5, pady=5)
from_currency_cb = ttk.Combobox(frame, values=list(exchange_rates.keys()), state="readonly")
from_currency_cb.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="To:").grid(row=2, column=0, padx=5, pady=5)
to_currency_cb = ttk.Combobox(frame, values=list(exchange_rates.keys()), state="readonly")
to_currency_cb.grid(row=2, column=1, padx=5, pady=5)

convert_button = tk.Button(root, text="Convert", command=convert_currency, bg="#4CAF50", fg="white", font=("Arial", 12))
convert_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

root.mainloop()
