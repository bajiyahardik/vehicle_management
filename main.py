import tkinter as tk
from tkinter import messagebox
import json
import os

data_file = 'vehicle_data.json'

if os.path.exists(data_file):
    with open(data_file, 'r') as file:
        vehicles = json.load(file)
else:
    vehicles = []

def save_data():
    with open(data_file, 'w') as file:
        json.dump(vehicles, file)

def add_vehicle():
    brand = entry_brand.get()
    model = entry_model.get()
    name = entry_name.get()
    vehicle_type = entry_vehicle_type.get()
    owner_name = entry_owner_name.get()
    owner_number = entry_owner_number.get()
    
    if brand and model and name and vehicle_type and owner_name and owner_number:
        vehicles.append({
            'Brand': brand,
            'Model': model,
            'Name': name,
            'Type': vehicle_type,
            'Owner Name': owner_name,
            'Owner Number': owner_number
        })
        save_data()
        display_vehicles()
        messagebox.showinfo("Success", "Vehicle added successfully!")
        entry_brand.delete(0, tk.END)
        entry_model.delete(0, tk.END)
        entry_name.delete(0, tk.END)
        entry_vehicle_type.delete(0, tk.END)
        entry_owner_name.delete(0, tk.END)
        entry_owner_number.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields")

def remove_vehicle():
    selected_vehicle = listbox.curselection()
    if selected_vehicle:
        vehicle = listbox.get(selected_vehicle)
        brand = vehicle.split(" | ")[0]
        vehicles[:] = [v for v in vehicles if v['Brand'] != brand]
        save_data()
        display_vehicles()
        messagebox.showinfo("Success", "Vehicle removed successfully!")
    else:
        messagebox.showwarning("Selection Error", "Please select a vehicle to remove")

def display_vehicles():
    listbox.delete(0, tk.END)
    for vehicle in vehicles:
        listbox.insert(tk.END, f"{vehicle['Brand']} | {vehicle['Model']} | {vehicle['Name']} | {vehicle['Type']} | {vehicle['Owner Name']} | {vehicle['Owner Number']}")

root = tk.Tk()
root.title("Vehicle Management System")
root.configure(bg="#f0f0f0")

window_width = 700
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_left = int(screen_width / 2 - window_width / 2)
root.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

label_brand = tk.Label(root, text="Brand:", font=("Arial", 12), bg="#f0f0f0", fg="#333")
label_brand.grid(row=0, column=0, padx=10, pady=10)
entry_brand = tk.Entry(root, font=("Arial", 12))
entry_brand.grid(row=0, column=1, padx=10, pady=10)

label_model = tk.Label(root, text="Model:", font=("Arial", 12), bg="#f0f0f0", fg="#333")
label_model.grid(row=1, column=0, padx=10, pady=10)
entry_model = tk.Entry(root, font=("Arial", 12))
entry_model.grid(row=1, column=1, padx=10, pady=10)

label_name = tk.Label(root, text="Vehicle Name:", font=("Arial", 12), bg="#f0f0f0", fg="#333")
label_name.grid(row=2, column=0, padx=10, pady=10)
entry_name = tk.Entry(root, font=("Arial", 12))
entry_name.grid(row=2, column=1, padx=10, pady=10)

label_vehicle_type = tk.Label(root, text="Vehicle Type:", font=("Arial", 12), bg="#f0f0f0", fg="#333")
label_vehicle_type.grid(row=3, column=0, padx=10, pady=10)
entry_vehicle_type = tk.Entry(root, font=("Arial", 12))
entry_vehicle_type.grid(row=3, column=1, padx=10, pady=10)

label_owner_name = tk.Label(root, text="Owner Name:", font=("Arial", 12), bg="#f0f0f0", fg="#333")
label_owner_name.grid(row=4, column=0, padx=10, pady=10)
entry_owner_name = tk.Entry(root, font=("Arial", 12))
entry_owner_name.grid(row=4, column=1, padx=10, pady=10)

label_owner_number = tk.Label(root, text="Owner Number:", font=("Arial", 12), bg="#f0f0f0", fg="#333")
label_owner_number.grid(row=5, column=0, padx=10, pady=10)
entry_owner_number = tk.Entry(root, font=("Arial", 12))
entry_owner_number.grid(row=5, column=1, padx=10, pady=10)

btn_add = tk.Button(root, text="Add Vehicle", font=("Arial", 12), command=add_vehicle, bg="#4CAF50", fg="white", relief="solid", width=15)
btn_add.grid(row=6, column=0, padx=10, pady=10)
btn_remove = tk.Button(root, text="Remove Vehicle", font=("Arial", 12), command=remove_vehicle, bg="#FF5733", fg="white", relief="solid", width=15)
btn_remove.grid(row=6, column=1, padx=10, pady=10)

listbox = tk.Listbox(root, width=70, height=10, font=("Arial", 12), selectmode=tk.SINGLE)
listbox.grid(row=7, column=0, columnspan=2, padx=10, pady=20)

scrollbar = tk.Scrollbar(root, orient="vertical", command=listbox.yview)
scrollbar.grid(row=7, column=2, sticky="ns")
listbox.config(yscrollcommand=scrollbar.set)

display_vehicles()

root.mainloop()
