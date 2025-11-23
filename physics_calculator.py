# Physics Calculator
# Simple Python application for physics calculations

def calculate_velocity(distance, time):
    """Calculate velocity: v = d/t"""
    return distance / time

def calculate_force(mass, acceleration):
    """Calculate force: F = m*a"""
    return mass * acceleration

def main():
    print("=== Physics Calculator ===")
    print("1. Calculate Velocity (v = d/t)")
    print("2. Calculate Force (F = m*a)")
    
    choice = input("Choose option (1/2): ")
    
    if choice == "1":
        print("\n--- Velocity Calculation ---")
        distance = float(input("Enter distance (meters): "))
        time = float(input("Enter time (seconds): "))
        velocity = calculate_velocity(distance, time)
        print(f"Velocity = {velocity} m/s")
        
    elif choice == "2":
        print("\n--- Force Calculation ---")
        mass = float(input("Enter mass (kg): "))
        acceleration = float(input("Enter acceleration (m/s²): "))
        force = calculate_force(mass, acceleration)
        print(f"Force = {force} N")
        
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
