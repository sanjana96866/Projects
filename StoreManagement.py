import tkinter as tk
from tkinter import messagebox
import random

class RetailBillingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Retail Billing System")
        self.root.geometry("700x600")
        
        # Variables
        self.items = []
        self.total_amount = 0
        self.bill_number = random.randint(1000, 9999)
        
        # UI Elements
        self.create_ui()
    
    def create_ui(self):
        # Title
        title_label = tk.Label(self.root, text="Retail Billing System", font=("Arial", 20, "bold"), bg="blue", fg="white")
        title_label.pack(fill=tk.X)

        # Item Frame
        item_frame = tk.Frame(self.root, bd=5, relief=tk.GROOVE)
        item_frame.place(x=20, y=60, width=660, height=120)

        tk.Label(item_frame, text="Item Name", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
        self.item_name_entry = tk.Entry(item_frame, font=("Arial", 12), width=20)
        self.item_name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(item_frame, text="Price", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)
        self.price_entry = tk.Entry(item_frame, font=("Arial", 12), width=20)
        self.price_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(item_frame, text="Quantity", font=("Arial", 12)).grid(row=0, column=2, padx=10, pady=5)
        self.quantity_entry = tk.Entry(item_frame, font=("Arial", 12), width=20)
        self.quantity_entry.grid(row=0, column=3, padx=10, pady=5)

        # Buttons in Item Frame
        tk.Button(item_frame, text="Add Item", command=self.add_item, font=("Arial", 12), bg="green", fg="white").grid(row=1, column=2, padx=10, pady=5)
        tk.Button(item_frame, text="Clear", command=self.clear_item_fields, font=("Arial", 12), bg="red", fg="white").grid(row=1, column=3, padx=10, pady=5)

        # Bill Display Frame
        bill_frame = tk.Frame(self.root, bd=5, relief=tk.GROOVE)
        bill_frame.place(x=20, y=200, width=660, height=260)

        tk.Label(bill_frame, text="Bill Details", font=("Arial", 14, "bold")).pack(anchor="nw")

        self.bill_text = tk.Text(bill_frame, font=("Arial", 12), state="normal")
        self.bill_text.pack(fill=tk.BOTH, expand=1)

        # Buttons at the Bottom
        tk.Button(self.root, text="Generate Bill", command=self.generate_bill, font=("Arial", 14), bg="blue", fg="white").place(x=150, y=500, width=150)
        tk.Button(self.root, text="Clear Bill", command=self.clear_bill, font=("Arial", 14), bg="orange", fg="white").place(x=320, y=500, width=150)
        tk.Button(self.root, text="Exit", command=self.root.quit, font=("Arial", 14), bg="red", fg="white").place(x=490, y=500, width=150)

    def add_item(self):
        """Add an item to the bill."""
        item_name = self.item_name_entry.get().strip()
        try:
            price = float(self.price_entry.get().strip())
            quantity = int(self.quantity_entry.get().strip())
        except ValueError:
            messagebox.showerror("Input Error", "Price must be a number and quantity must be an integer.")
            return
        
        if not item_name:
            messagebox.showerror("Input Error", "Item name cannot be empty.")
            return

        self.items.append((item_name, price, quantity))
        self.update_bill_display(item_name, price, quantity)
        self.clear_item_fields()

    def update_bill_display(self, item_name, price, quantity):
        """Update the bill display with the added item."""
        item_total = price * quantity
        self.total_amount += item_total
        self.bill_text.insert(tk.END, f"{item_name}\t\t{quantity} x {price:.2f} = {item_total:.2f}\n")

    def clear_item_fields(self):
        """Clear the item input fields."""
        self.item_name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

    def generate_bill(self):
        """Generate the final bill."""
        if not self.items:
            messagebox.showerror("No Items", "No items to generate a bill.")
            return
        
        self.bill_text.insert(tk.END, "\n" + "="*50 + "\n")
        self.bill_text.insert(tk.END, f"Bill Number: {self.bill_number}\n")
        self.bill_text.insert(tk.END, f"Total Amount: {self.total_amount:.2f}\n")
        self.bill_text.insert(tk.END, "="*50 + "\n")
        messagebox.showinfo("Bill Generated", f"Bill Number {self.bill_number} generated successfully!")

    def clear_bill(self):
        """Clear the bill."""
        self.items = []
        self.total_amount = 0
        self.bill_number = random.randint(1000, 9999)
        self.bill_text.delete(1.0, tk.END)
        messagebox.showinfo("Bill Cleared", "The bill has been cleared.")


# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = RetailBillingSystem(root)
    root.mainloop()
