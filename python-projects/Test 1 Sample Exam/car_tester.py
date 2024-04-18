#imports car class
from car import Car

with open("cars.txt") as file:
    cars_list = []

    for line in file:
        stripped_line=line.strip()
        tokens = stripped_line.split()
        color = tokens[0]
        engine_type = tokens[1]
        gas_tank_value = tokens[2]
        odometer = tokens[3]

        car = Car(color, engine_type, int(gas_tank_value), int(odometer))
        cars_list.append(car)

    print(f"Car details: {cars_list[0]}")

    gas_tank_value = cars_list[0].get_gas_tank()
    print(f"Gas tank value: {gas_tank_value} gallons")

    odometer_value = cars_list[0].get_odometer()
    print(f"Odometer value: {odometer} miles")

    cars_list[0].drive()
    
    gas_tank_value = cars_list[0].get_gas_tank()
    print(f"Gas tank value: {gas_tank_value} gallons")

    odometer = cars_list[0].get_odometer()
    print(f"Odometer value: {odometer} miles")



    print(f"Car details: {cars_list[1]}")
    
    gas_tank_value = cars_list[1].get_gas_tank()
    print(f"Gas tank value: {gas_tank_value} gallons")

    odometer_value = cars_list[1].get_odometer()
    print(f"Odometer value: {odometer} miles")

    cars_list[1].drive()

    gas_tank_value = cars_list[1].get_gas_tank()
    print(f"Gas tank value: {gas_tank_value} gallons")

    odometer = cars_list[1].get_odometer()
    print(f"Odometer value: {odometer} miles")
