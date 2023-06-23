import tkinter as tk

def calculate_next_risk(previous_loss, current_profit):
    if previous_loss <= -1:
        return 0.5
    elif previous_loss == -0.5:
        return 0.5
    elif current_profit >= abs(0.5 * previous_loss):
        return 1
    else:
        return 0.5

def split_lot_size():
    # Get input values from GUI
    lot_size = float(lot_size_entry.get())
    num_of_partials = int(num_partials_entry.get())

    # Define fixed split percentages based on number of partials
    if num_of_partials == 2:
        partial_1_pct = 0.3
        partial_2_pct = 0.7
    elif num_of_partials == 3:
        partial_1_pct = 0.2
        partial_2_pct = 0.3
        partial_3_pct = 0.5
    else:
        output_label.config(text="Error: Unsupported number of partials")
        return

    # Calculate lot size for each partial using fixed split percentages
    if num_of_partials == 2:
        partial_1_size = lot_size * partial_1_pct
        partial_2_size = lot_size * partial_2_pct

        # Update output label with lot sizes for each partial
        output_label.config(text=f"Partial 1 Lot Size: {round(partial_1_size, 2)}\nPartial 2 Lot Size: {round(partial_2_size, 2)}")
    elif num_of_partials == 3:
        partial_1_size = lot_size * partial_1_pct
        partial_2_size = lot_size * partial_2_pct
        partial_3_size = lot_size * partial_3_pct

        # Update output label with lot sizes for each partial
        output_label.config(text=f"Partial 1 Lot Size: {round(partial_1_size, 2)}\nPartial 2 Lot Size: {round(partial_2_size, 2)}\nPartial 3 Lot Size: {round(partial_3_size, 2)}")

# Create main window and set title
root = tk.Tk()
root.title("Lot Size Splitter and Risk Calculator")

# Create input labels and entries for lot size split
lot_size_label = tk.Label(root, text="Lot Size:")
lot_size_entry = tk.Entry(root)
num_partials_label = tk.Label(root, text="Number of Partials:")
num_partials_entry = tk.Entry(root)

# Create output label for lot size split
output_label = tk.Label(root, text="")

# Create button to trigger lot size split calculation
calculate_button = tk.Button(root, text="Split Lot Size", command=split_lot_size)

# Create input labels and entries for risk calculation
previous_loss_label = tk.Label(root, text="Previous Loss (%):")
previous_loss_entry = tk.Entry(root)
current_profit_label = tk.Label(root, text="Current Profit (%):")
current_profit_entry = tk.Entry(root)

# Create output label for risk calculation
risk_output_label = tk.Label(root, text="")

# Create button to trigger risk calculation
risk_button = tk.Button(root, text="Calculate Next Risk", command=lambda: risk_output_label.config(text=f"Next Risk: {calculate_next_risk(float(previous_loss_entry.get()), float(current_profit_entry.get()))}"))

# Arrange input labels and entries for lot size split on GUI grid
lot_size_label.grid(row=0, column=0, padx=5, pady=5)
lot_size_entry.grid(row=0, column=1, padx=5, pady=5)
num_partials_label.grid(row=1, column=0, padx=5, pady=5)
num_partials_entry.grid(row=1, column=1, padx=5, pady=5)

# Arrange output label for lot size split on GUI grid
output_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Arrange button for lot size split on GUI grid
calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Arrange input labels and entries for risk calculation on GUI grid
previous_loss_label.grid(row=4, column=0, padx=5, pady=5)
previous_loss_entry.grid(row=4, column=1, padx=5, pady=5)
current_profit_label.grid(row=5, column=0, padx=5, pady=5)
current_profit_entry.grid(row=5, column=1, padx=5, pady=5)

# Arrange output label for risk calculation on GUI grid
risk_output_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Arrange button for risk calculation on GUI grid
risk_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

# Start GUI event loop
root.mainloop()
