user_mass : float = float(input("Enter the kilos of mass : "))

C : int = 299792458

print("e = mc^2")
print(f"mass = {user_mass}kg...")
print(f"Speed of light (C) = {C} m/s ...")

formula = (f"e = {user_mass * (C ** 2)} joules of energy!")
print("Putting the values in the equation....")
print(formula)