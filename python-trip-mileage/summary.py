def print_summary(distance_km, num_stops, total_fuel, fuel_consumption, total_cost):
    print("\n=== Trip Summary ===")
    print(f"Total distance (km): {distance_km:.2f}")
    print(f"Number of stops: {num_stops}")
    print(f"Total fuel used (L): {total_fuel:.2f}")
    print(f"Fuel consumption (L/100 km): {fuel_consumption:.2f}")
    print(f"Total fuel cost ($): {total_cost:.2f}")