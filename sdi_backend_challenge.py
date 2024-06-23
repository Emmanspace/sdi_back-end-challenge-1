def calculate_optimized_cost(seats):
    cars = [
        {"size": "S", "capacity": 5, "cost": 5000},
        {"size": "M", "capacity": 10, "cost": 8000},
        {"size": "L", "capacity": 15, "cost": 12000}
    ]
    
    # Sort cars by cost per capacity to ensure we use the most cost-effective cars
    cars.sort(key=lambda x: (x["cost"] / x["capacity"]))
    
    # Calculate the minimum cost and car distribution
    total_cost = 0
    car_count = {"S": 0, "M": 0, "L": 0}
    
    # Iterate from most cost-effective to least
    for car in cars:
        while seats >= car["capacity"]:
            seats -= car["capacity"]
            total_cost += car["cost"]
            car_count[car["size"]] += 1
    
    # Handle remaining seats with the smallest car available
    if seats > 0:
        smallest_car = cars[0]
        total_cost += smallest_car["cost"]
        car_count[smallest_car["size"]] += 1

    return car_count, total_cost

def take_car_seats():
    seats = int(input("Please input number (seat): "))
    car_count, total_cost = calculate_optimized_cost(seats)
    
    for size, count in car_count.items():
        if count > 0:
            print(f"{size} x {count}")
    print(f"Total = PHP {total_cost}")

def main():
    import sys

    take_car_seats()

if __name__ == "__main__":
    main()


# backend problem