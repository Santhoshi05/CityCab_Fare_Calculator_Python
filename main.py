class InvalidVehicleType(Exception):
    pass
rates = {'Economy': 10,'Premium': 18 , 'Suv': 25}
def calculate_fare(km,vehicle_type, hour,minu):
    rate = rates[vehicle_type]
    price = km * rate
    if ((hour > 17) or hour == 17 and minu >= 0) and ((hour < 20) or hour == 20 and minu >= 0):
        price *= 1.5
    return price
print("Welcome to City Cab Fare Calculator")
while True:
    while True:
        try:
            km = float(input("Enter distance in km:"))
            if km <=0:
                raise ValueError("Enter valid distance")
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            vehicle_type = input("Enter vehicle type (Economy, Premium, SUV):").title()
            if vehicle_type not in rates:
                raise InvalidVehicleType("Service Not Available")
            break
        except InvalidVehicleType as e:
            print(e)
            again = input("Do you want to continue(yes/no): ").lower()
            if again != "yes":
                print("Thank you user")
                exit()
    while True:
        try:
            time = input("Enter start time in hour(0-23): ")
            p = time.split()
            if len(p) != 2:
                raise ValueError("Enter time in format: HH MM")
            hour = int(p[0])
            minu = int(p[1])
            if not (0 <= hour <= 23 and 0 <= minu <= 59):
                raise ValueError("Enter Valid time in hour")
            break
        except ValueError as e:
            print(e)
    price = calculate_fare(km,vehicle_type,hour,minu)
    print("\n   PRICE RECEIPT  ")
    print(f"Distance      : {km} km")
    print(f"Vehicle Type  : {vehicle_type}")
    print(f"Start Time    : {hour:02d}:{minu:02d}")
    print(f"Total Fare    : {price}")
    print()
    again = input("Do you want to continue(yes/no): ").lower()
    if again != "yes":
        print("Thank you user")
        break



