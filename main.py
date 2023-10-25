'''
Type your code here
'''

#Driver code
# Create instances of Vehicle, Car, and Motorcycle
vehicle1 = Vehicle("Toyota", "Camry", 2022)
car1 = Car("Tesla", "Model 3", 2023, "Electric")
motorcycle1 = Motorcycle("Honda", "CBR500R", 2021, 471)

# Demonstrate class variables and inheritance
vehicle1.display_vehicle_count()

# Demonstrate private and protected variables
motorcycle1.__vin = "ABC123"  # Attempt to set private variable (won't work)
motorcycle1.set_color("Red")  # Set protected variable
print(f"Motorcycle color: {motorcycle1._color}")
print(f"Motorcycle VIN: {motorcycle1.get_vin()}")  # Access private variable

# Demonstrate generator functions
print("Counting up to 5:")
for num in count_up_to(5):
    print(num, end=" ")

print("\nFibonacci sequence up to 50:")
for num in fibonacci(50):
    print(num, end=" ")

# Demonstrate class variables
vehicle2 = Vehicle("Ford", "F-150", 2022)
vehicle3 = Vehicle("Honda", "Civic", 2022)
vehicle2.display_vehicle_count()
