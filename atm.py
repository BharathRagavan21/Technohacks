import tkinter as tk
from tkinter import messagebox


class ATMSimulator:
    def __init__(self):
        self.account_balance = 0
        self.pin = "1234"  # Replace with your desired PIN
        self.logged_in = False

    def login(self, entered_pin):
        if entered_pin == self.pin:
            self.logged_in = True
            messagebox.showinfo("Login Successful", "You have successfully logged in.")
        else:
            self.logged_in = False
            messagebox.showerror("Invalid PIN", "Please enter a valid PIN.")

    def logout(self):
        self.logged_in = False
        messagebox.showinfo("Logout", "You have been logged out.")

    def check_balance(self):
        if self.logged_in:
            messagebox.showinfo("Account Balance", f"Your current balance is ${self.account_balance}")
        else:
            messagebox.showerror("Access Denied", "Please log in to access your account.")

    def deposit(self, amount):
        if self.logged_in:
            self.account_balance += amount
            messagebox.showinfo("Deposit", f"${amount} successfully deposited. Your current balance is ${self.account_balance}")
        else:
            messagebox.showerror("Access Denied", "Please log in to access your account.")

    def withdraw(self, amount):
        if self.logged_in:
            if amount <= self.account_balance:
                self.account_balance -= amount
                messagebox.showinfo("Withdrawal", f"${amount} successfully withdrawn. Your current balance is ${self.account_balance}")
            else:
                messagebox.showerror("Withdrawal", "Insufficient funds. Please try again with a lower amount.")
        else:
            messagebox.showerror("Access Denied", "Please log in to access your account.")


class ATMGUI:
    def __init__(self, atm):
        self.atm = atm

        self.window = tk.Tk()
        self.window.title("ATM Simulator")

        self.login_frame = tk.Frame(self.window)
        self.login_frame.pack(pady=10)

        self.pin_label = tk.Label(self.login_frame, text="Enter PIN:")
        self.pin_label.pack(side=tk.LEFT)

        self.pin_entry = tk.Entry(self.login_frame, show="*")
        self.pin_entry.pack(side=tk.LEFT)

        self.login_button = tk.Button(self.window, text="Login", command=self.login)
        self.login_button.pack(pady=10)

        self.balance_button = tk.Button(self.window, text="Check Balance", command=self.check_balance)
        self.balance_button.pack(pady=10)

        self.deposit_frame = tk.Frame(self.window)
        self.deposit_frame.pack(pady=10)

        self.deposit_label = tk.Label(self.deposit_frame, text="Deposit Amount:")
        self.deposit_label.pack(side=tk.LEFT)

        self.deposit_entry = tk.Entry(self.deposit_frame)
        self.deposit_entry.pack(side=tk.LEFT)

        self.deposit_button = tk.Button(self.window, text="Deposit", command=self.deposit)
        self.deposit_button.pack(pady=5)

        self.withdraw_frame = tk.Frame(self.window)
        self.withdraw_frame.pack(pady=10)

        self.withdraw_label = tk.Label(self.withdraw_frame, text="Withdraw Amount:")
        self.withdraw_label.pack(side=tk.LEFT)

        self.withdraw_entry = tk.Entry(self.withdraw_frame)
        self.withdraw_entry.pack(side=tk.LEFT)

        self.withdraw_button = tk.Button(self.window, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack(pady=5)

        self.logout_button = tk.Button(self.window, text="Logout", command=self.logout)
        self.logout_button.pack(pady=10)

    def login(self):
        entered_pin = self.pin_entry.get()
        if entered_pin:
            self.atm.login(entered_pin)
        else:
            messagebox.showerror("Invalid PIN", "Please enter a valid PIN.")

    def check_balance(self):
        self.atm.check_balance()

    def deposit(self):
        amount = float(self.deposit_entry.get())
        self.atm.deposit(amount)
        self.deposit_entry.delete(0, tk.END)

    def withdraw(self):
        amount = float(self.withdraw_entry.get())
        self.atm.withdraw(amount)
        self.withdraw_entry.delete(0, tk.END)

    def logout(self):
        self.atm.logout()

    def run(self):
        self.window.mainloop()


atm_simulator = ATMSimulator()
atm_gui = ATMGUI(atm_simulator)
atm_gui.run()