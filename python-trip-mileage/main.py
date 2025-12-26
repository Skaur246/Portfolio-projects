# importing the calculation functions from the trip_calculations file
from trip_calculations import (calculate_fuel_consumption_l_per_100km,calculate_total_cost)
# Importing the summary function that prints the trip summary
from summary import print_summary

print("=== Trip Mileage Calculator ===")

# ----- INPUT -----
distance_km = float(input("Enter trip distance in kilometers: "))
num_stops = int(input("Enter number of fuel stops: "))
price_per_litre = float(input("Enter fuel price per litre (e.g., 1.63): "))

# ----- CHECK DISTANCE -----
if distance_km <= 0:
    print("Error: distance must be greater than 0.")
else:
   
    total_fuel = 0.0
    counter = 1
    
    while counter <= num_stops:
        litres_at_stop = float(input(f"Enter litres of fuel purchased at stop #{counter}: "))
        total_fuel = total_fuel + litres_at_stop
        counter = counter + 1

# ----- CHECKING TOTAL FUEL -----
if total_fuel <= 0:
        print("Error: total fuel used must be greater than 0.")
else:
# using the functions from the trip_calculations file to do calculations
    fuel_consumption = calculate_fuel_consumption_l_per_100km(total_fuel, distance_km)
    total_cost = calculate_total_cost(total_fuel, price_per_litre)

    # ----- OUTPUT -----
print_summary(distance_km, num_stops, total_fuel, fuel_consumption, total_cost)
