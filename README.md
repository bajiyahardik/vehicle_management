# Vehicle Management System

## Overview
The **Vehicle Management System** is a simple graphical user interface (GUI) application built using Python's Tkinter library. It allows users to add, view, update, delete, and list vehicles stored in a JSON file. This application is ideal for managing vehicle data such as vehicle IDs, make, model, year, and color.

## Features
- **Add Vehicle**: Adds a new vehicle to the system.
- **View Vehicle**: View details of a vehicle by its ID.
- **Update Vehicle**: Update information of an existing vehicle.
- **Delete Vehicle**: Delete a vehicle from the system.
- **List All Vehicles**: View all vehicles currently stored in the system.

## Requirements
To run this project, you need to have the following:
- Python 3.x installed.
- Tkinter (comes pre-installed with Python).
- JSON file for storing vehicle data (`vehicles.json`).

## Installation Instructions

1. **Clone the repository** or download the project files to your local machine.

    ```bash
    git clone https://github.com/your-username/vehicle-management-system.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd vehicle-management-system
    ```

3. **Install required dependencies**:
    - The project uses Python’s built-in Tkinter library for the GUI, so no additional libraries are required.

4. **Run the application**:

    ```bash
    python vehicle_management_system.py
    ```

## Usage

Once the application is running, you will see the GUI window with the following options:

### 1. **Add Vehicle**
- Input vehicle details such as ID, make, model, year, and color.
- Click on the "Add Vehicle" button to add the vehicle to the system.

### 2. **View Vehicle**
- Input the vehicle ID.
- Click "View Vehicle" to see the details of the selected vehicle.

### 3. **Update Vehicle**
- Input the vehicle ID and any new details you wish to update.
- Click "Update Vehicle" to save changes.

### 4. **Delete Vehicle**
- Input the vehicle ID.
- Click "Delete Vehicle" to remove the vehicle from the system.

### 5. **List All Vehicles**
- Click "List All Vehicles" to view all vehicles stored in the system.

## How It Works

- **Vehicle class**: Represents a vehicle with attributes such as `vehicle_id`, `make`, `model`, `year`, and `color`.
- **VehicleManagementSystem class**: Manages vehicle data, allowing vehicles to be added, updated, deleted, and listed. It also handles reading and saving data from the `vehicles.json` file.
- **Tkinter GUI**: The graphical interface allows users to interact with the system, displaying input fields and buttons to perform actions.

## File Structure

```plaintext
vehicle-management-system/
│
├── vehicle_management_system.py  # Main Python script for the app
└── vehicles.json                 # JSON file where vehicle data is stored
