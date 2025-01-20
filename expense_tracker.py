import customtkinter as ctk

# ctk.set_appearance_mode("light")
# ctk.set_default_color_theme("green")


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("550x650")

        self.transaction_list = [
            ("Food", 0, 200),
            ("Transport", 10.0, 0),
            ("Groceries", 300.0, 0),
            ("Entertainment", 0, 150.0),
            ("Food", 0, 200.0),
            ("Transport", 0, 150.0),
            ("Utilities", 400.0, 0),
            ("Food", 0, 200.0),
            ("Transport", 10.0, 0),
            ("Groceries", 300.0, 0),
            ("Entertainment", 0, 150.0),
            ("Food", 0, 200.0),
            ("Transport", 0, 150.0),
            ("Utilities", 400.0, 0),]


        self.main_frame = ctk.CTkFrame(root, corner_radius=15)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.status()

        self.balance()


    def clear(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def status(self):
        self.status_bar=ctk.CTkLabel(self.root,text='',text_color='red')
        self.status_bar.pack(padx=20, pady=10)

    def calculation(self):
        total_income = sum(item[1] for item in self.transaction_list)  #list comprehension
        total_expense = sum(item[2] for item in self.transaction_list)

        # total_expense=0
        # for item in self.transaction_list:
        #     total_expense+=item[2]

        balance = total_income - total_expense
        return total_income, total_expense, balance

    def balance(self):
        self.clear()
        self.status_bar.configure(text='')

        total_income, total_expense, balance = self.calculation()

        heading = ctk.CTkLabel(self.main_frame, text="Expense Tracker", font=ctk.CTkFont(size=40, weight="bold"))
        heading.grid(row=0,padx=10,pady=40)


        summary_frame = ctk.CTkFrame(self.main_frame, corner_radius=10)
        summary_frame.grid(row=1, column=0, padx=40, pady=20)

        balance_label = ctk.CTkLabel(summary_frame, text=f"Balance:\n ₹{balance}", font=ctk.CTkFont(size=30, weight="bold"))
        balance_label.grid(row=0, column=1, padx=20, pady=10)

        income_label = ctk.CTkLabel(summary_frame, text=f"Income:\n ₹{total_income}", font=ctk.CTkFont(size=25),text_color='#32cd32')
        income_label.grid(row=1, column=0, padx=20, pady=10)

        expense_label = ctk.CTkLabel(summary_frame, text=f"Expense:\n ₹{total_expense}", font=ctk.CTkFont(size=25),text_color='red')
        expense_label.grid(row=1, column=2, padx=20, pady=10)

        add_exp_btn=ctk.CTkButton(self.main_frame,text='Add Expense', font=ctk.CTkFont(size=25),command=self.add_expense, width=200, height=50)
        add_exp_btn.grid(row=2,padx=10, pady=10)

        transaction_btn=ctk.CTkButton(self.main_frame,text='Transactions', font=ctk.CTkFont(size=25),command=self.transaction, width=200, height=50)
        transaction_btn.grid(row=3,padx=10, pady=20)

        quit_btn=ctk.CTkButton(self.main_frame,text='Quit', font=ctk.CTkFont(size=25),command=self.root.quit, width=200, height=50)
        quit_btn.grid(row=4,padx=10, pady=10)

    def transaction(self):
        self.clear()

        transaction_label = ctk.CTkLabel(self.main_frame, text='Transactions', font=ctk.CTkFont(size=24, weight='bold'))
        transaction_label.pack(pady=20)

        transaction_frame = ctk.CTkScrollableFrame(self.main_frame, width=500, height=300, corner_radius=10)
        transaction_frame.pack(padx=20, pady=20)

        ctk.CTkLabel(transaction_frame, text="Category", font=ctk.CTkFont(size=14, weight="bold")).grid(row=0, column=0, padx=10, pady=5)
        ctk.CTkLabel(transaction_frame, text="Amount", font=ctk.CTkFont(size=14, weight="bold")).grid(row=0, column=1, padx=10, pady=5)
        ctk.CTkLabel(transaction_frame, text="Action", font=ctk.CTkFont(size=14, weight="bold")).grid(row=0, column=2, padx=10, pady=5)

        for i, (category, income, expense) in enumerate(self.transaction_list, start=1):
            ctk.CTkLabel(transaction_frame, text=category, font=ctk.CTkFont(size=14)).grid(row=i, column=0, padx=10, pady=5, sticky="w")

            if income > 0:
                ctk.CTkLabel(transaction_frame, text=f"+₹{income}", font=ctk.CTkFont(size=14), text_color="green").grid(row=i, column=1, padx=10, pady=5)

            elif expense > 0:
                ctk.CTkLabel(transaction_frame, text=f"-₹{expense}", font=ctk.CTkFont(size=14), text_color="red").grid(row=i, column=1, padx=10, pady=5)

            delete_btn = ctk.CTkButton(transaction_frame,text="Delete",font=ctk.CTkFont(size=12),command=lambda idx=i-1: self.delete_transaction(idx))
            delete_btn.grid(row=i, column=2, padx=10, pady=5)

        back_btn = ctk.CTkButton(self.main_frame, text="Back", command=self.balance, width=200, height=50)
        back_btn.pack(pady=10)

    def add_expense(self):
        self.clear()

        ctk.CTkLabel(self.main_frame, text="Add New Transaction", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=10)

        form_frame = ctk.CTkFrame(self.main_frame, corner_radius=10)
        form_frame.pack(pady=20)


        ctk.CTkLabel(form_frame, text="Category:").grid(row=0, column=0, padx=10, pady=10)
        category_entry = ctk.CTkEntry(form_frame, width=200)
        category_entry.grid(row=0, column=1, padx=10, pady=10)


        ctk.CTkLabel(form_frame, text="Amount:").grid(row=1, column=0, padx=10, pady=10)
        amount_entry = ctk.CTkEntry(form_frame, width=200)
        amount_entry.grid(row=1, column=1, padx=10, pady=10)

        ctk.CTkLabel(form_frame, text="Type:").grid(row=2, column=0, padx=10, pady=10)
        type = ctk.StringVar()
        income_radio = ctk.CTkRadioButton(form_frame, text="Income", variable=type, value="Income")
        income_radio.grid(row=2, column=1, padx=5, sticky="w")
        expense_radio = ctk.CTkRadioButton(form_frame, text="Expense", variable=type, value="Expense")
        expense_radio.grid(row=2, column=1, padx=5, sticky="e")

        def submit_transaction():
            category = category_entry.get()
            t_type = type.get()
            try:
                amount = float(amount_entry.get())
                if category and amount > 0 and t_type:
                    if t_type == 'Income':
                        self.transaction_list.append((category, amount, 0))
                    else:
                        self.transaction_list.append((category, 0, amount))
                    self.balance()
                else:
                    self.status_bar.configure(text='Enter valid category or amount')
                    self.add_expense()
            except ValueError:
                self.status_bar.configure(text='Enter a valid amount')
                self.add_expense()

        submit_btn = ctk.CTkButton(self.main_frame, text="Submit", command=submit_transaction)
        submit_btn.pack(pady=10)


        back_btn = ctk.CTkButton(self.main_frame, text="Back", command=self.balance)
        back_btn.pack(pady=10)

    def delete_transaction(self, idx):
        del self.transaction_list[idx]
        self.transaction()


root = ctk.CTk()
app = App(root)
root.mainloop()
