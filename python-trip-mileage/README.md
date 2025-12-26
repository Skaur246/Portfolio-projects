# Road-Trip-Fuel-Efficiency-Calculator
Assignment 4 
Trip Mileage Calculator

This program calculates fuel efficiency and total fuel cost for a road trip using Canadian units (kilometres, litres, and litres per 100 km).
It asks the user for the trip distance, number of fuel stops, litres of fuel purchased at each stop, and fuel price per litre.
The program then computes:

Total litres of fuel used

Fuel consumption in L/100 km

Total fuel cost

It also handles error cases if the distance or total fuel is less than or equal to zero.

## Structured Pseudocode in both ways ##

Natural Language Pseducode:
##Input##
1.Ask the user for the trip distance in kilometres
2.Ask the user for the number of fuel stops
3.Ask the user for the price per litre of fuel
##Processing / Logic##
4.If the distance is less than or equal to 0
#   display an error message and stop
5.Set total fuel to 0
6.Set counter to 1
7.While the counter is less than or equal to the number of stops
 #   ask the user for the litres of fuel at this stop
 #   add the litres to the total fuel
 #   increase the counter by 1
8.If the total fuel is less than or equal to 0
#   display an error message and stop
9.Calculate fuel consumption as (total fuel / distance) * 100
10.Calculate total cost as total fuel * price per litre
##output##
11.Display the total distance
12.Display the number of stops
13.Display the total fuel used
14.Display the fuel consumption in L/100 km
15.Display the total fuel cost

### strctured psedocode ###
BEGIN

"" INPUT ""

INPUT distance_km
INPUT num_stops
INPUT price_per_litre

    "" LOGIC / PROCESSING ""

IF distance_km <= 0 THEN
    DISPLAY "Error: distance must be greater than 0."
    STOP
ENDIF

SET total_fuel = 0
SET counter = 1

WHILE counter <= num_stops DO
    INPUT litres_at_stop
    total_fuel = total_fuel + litres_at_stop
    counter = counter + 1
ENDWHILE

IF total_fuel <= 0 THEN
    DISPLAY "Error: total fuel used must be greater than 0."
    STOP
ENDIF

SET fuel_consumption = (total_fuel / distance_km) * 100
SET total_cost = total_fuel * price_per_litre

    "" OUTPUT ""

DISPLAY "Total distance (km): ", distance_km
DISPLAY "Number of stops: ", num_stops
DISPLAY "Total fuel used (L): ", total_fuel
DISPLAY "Fuel consumption (L/100 km): ", fuel_consumption
DISPLAY "Total fuel cost ($): ", total_cost

END

Below is the flowchart that represents the logic of the program:
<img width="1219" height="2800" alt="flowchart png" src="https://github.com/user-attachments/assets/398014a7-d053-4250-8d85-4498c88265be" />

Algorithmic Patterns

Sequence:
The program runs steps in order — input → calculations → output.

Loop:
A while loop collects fuel amounts at each fuel stop.

Decision / Branching:
Two if statements check for invalid values (distance ≤ 0 and total_fuel ≤ 0).

Calculation:
Math formulas compute L/100 km and total fuel cost.


