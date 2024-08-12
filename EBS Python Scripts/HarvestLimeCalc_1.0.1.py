"""
Program Title: Harvest Lime Calculator
Program Version: (Found in tk labels)
Author: Hunter Brown
Date Created: (08/01/2024)
Last Modified: (08/11/2024)
Description: Dehydrated Lime Pack Estimations for CA Environments
Dependencies: Python 3.12.5
License: None
#FIXME- DEV Notes: All input parameters are provided in the INFO buttons
#FIXME- ERRORS: -Info Here-
Error History Below
"""
#------------------------------------------------------------------------------------------------------------
# Import Modules
import tkinter as tk
from tkinter import messagebox


# -- Lime Calculation Factors --
# With Lime Scrubber (y)
lime_calculation_factor_y = {
    'gala': 5.5, 'honeycrisp': 22, 'organic_honeycrisp': 22,
    'red': 6.6, 'organic_red': 6.6, 'organic_golden': 6.6,
    'golden': 6.6, 'grannysmith': 5.5, 'organic_grannysmith': 5.5,
    'fuji': 5.5, 'organic_fuji': 5.5, 'pink_lady': 5.5,
    'organic_pink_lady': 5.5, 'frozen_pink_lady': 10.5,
}

# Without Lime Scrubber (n)
lime_calculation_factor_n = {
    'gala': 15.4, 'honeycrisp': 55, 'organic_honeycrisp': 55,
    'red': 15.4, 'organic_red': 15.4, 'organic_golden': 22,
    'golden': 22, 'grannysmith': 15.4, 'organic_grannysmith': 15.4,
    'fuji': 15.4, 'organic_fuji': 15.4, 'pink_lady': 15.4,
    'organic_pink_lady': 15.4, 'frozen_pink_lady': 33,
}

#------------------------------------------------------------------------------------------------------------

# -- Conversion Function --

def calculate_lime_pallets(calculation_factor, bin_count, variety):
    if calculation_factor == "y":
        lime_factor = lime_calculation_factor_y.get(variety)
    elif calculation_factor == "n":
        lime_factor = lime_calculation_factor_n.get(variety)
    else:
        return None, None

    if lime_factor is None:
        return None, None

    lime_lbs = lime_factor * bin_count
    lime_packs = lime_lbs / 50
    lime_pallets = lime_packs / 7
    return lime_packs, lime_pallets

#------------------------------------------------------------------------------------------------------------

# -- Main Program (Calculate Button) --
def calculate():
    try:
        # Data Retrieval Tools
        fruit_variety = entry_variety.get()
        bin_count = float(entry_bin_count.get())
        calculation_factor = entry_calc_factor.get().lower()

        # Calculate Lime Pack and Pallet Count
        lime_packs, lime_pallets = calculate_lime_pallets(calculation_factor, bin_count, fruit_variety)

        if lime_packs is not None and lime_pallets is not None:
            # Result Output Message
            messagebox.showinfo("CA Lime Requirements",
                                f"Pallets Required: {lime_pallets:.2f}")
        # Syntax Error
        else:
            messagebox.showerror("Error", "Invalid fruit variety or calculation factor.")
    # Numerical Error
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")


#------------------------------------------------------------------------------------------------------------

# -- Help Functions --

# Help with Fruit Variety Names (CASE SENSITIVE)
def helpvar():
    messagebox.showinfo(title="Fruit Variety",
                        message="Entries are Case Sensitive\n\n"
                                "gala\n"
                                "honeycrisp\n"
                                "organic_honeycrisp\n"
                                "red\n"
                                "organic_red\n"
                                "golden\n"
                                "organic_golden\n"
                                "grannysmith\n"
                                "organic_grannysmith\n"
                                "fuji\n"
                                "organic_fuji\n"
                                "pink_lady\n"
                                "organic_pink_lady\n"
                                "frozen_pink_lady")


# Help Bin Count
def helpbin():
    messagebox.showinfo(title="Bin Count",
                        message="Total # of bins stored in CA Room")


# Help Calculation Factor
def helpfact():
    messagebox.showinfo(title="Calculation Factor",
                        message="WITH Lime Scrubbers: ( y )\n"
                                "WITHOUT Lime Scrubbers: ( n )")


#------------------------------------------------------------------------------------------------------------

# -- Tkinter Window Assembler --

# -- Create Tkinter window --
window = tk.Tk()
window.title("Harvest Lime Calculator")

# -- Create input labels and entry widgets --

# Version Label
label_version = tk.Label(window, text="Version: 1.0.1")
label_version.grid(row=4, column=0, padx=5, pady=5)

# Variety
label_variety = tk.Label(window, text="Fruit Variety:")
entry_variety = tk.Entry(window)

# Bin Count
label_bin_count = tk.Label(window, text="Bin Count of CA:")
entry_bin_count = tk.Entry(window)

# Calculation Factor
label_calc_factor = tk.Label(window, text="Using Lime Scrub? ( y / n ):")
entry_calc_factor = tk.Entry(window)

# Create Buttons
button_calculate = tk.Button(window, text="Calculate", command=calculate)
button_helpvar = tk.Button(window, text="   INFO   ", command=helpvar)
button_helpbin = tk.Button(window, text="   INFO   ", command=helpbin)
button_helpfact = tk.Button(window, text="   INFO   ", command=helpfact)

# -- Label / Entry Grid Positions --

#Variety
label_variety.grid(row=0, column=0, padx=10, pady=5)
entry_variety.grid(row=0, column=1, padx=10, pady=5)
button_helpvar.grid(row=0, column=2, padx=2, pady=5)

# Bin Count
label_bin_count.grid(row=1, column=0, padx=10, pady=5)
entry_bin_count.grid(row=1, column=1, padx=10, pady=5)
button_helpbin.grid(row=1, column=2, padx=2, pady=5)

# Calculation Factor
label_calc_factor.grid(row=2, column=0, padx=10, pady=5)
entry_calc_factor.grid(row=2, column=1, padx=10, pady=5)
button_helpfact.grid(row=2, column=2, padx=2, pady=5)

# Calculation Function
button_calculate.grid(row=4, column=1, padx=10, pady=10)

# Run the Tkinter event loop
window.mainloop()

#------------------------------------------------------------------------------------------------------------
# DEV Version Changes
'''
Date: MM/DD/YYYY
DEV: Your_Name_Here
Entry: Template
-------------------------------------------------------------------------------
Date: 08/06/2024
DEV: Hunter Brown
Entry: Redesigned program layout, added proper functionality for 2024 Harvest Conditions.
-------------------------------------------------------------------------------
Date: 08/06/2024
DEV: Hunter Brown
Entry: Finalized program, Added Notation for easy editing
-------------------------------------------------------------------------------
'''
