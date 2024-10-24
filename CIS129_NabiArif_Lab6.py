import math

def main():
    # Local variable for the total number of hot dogs needed.
    total = get_total_hot_dogs()

    # Named constants for the package sizes
    DOGS = 10   # Hot dogs in a package
    BUNS = 8    # Hot dog buns in a package

    # Local variables
    dogs_left = (DOGS - total % DOGS) % DOGS  # Left over hot dogs
    min_dogs = math.ceil(total / DOGS)        # Minimum packages of hot dogs
    buns_left = (BUNS - total % BUNS) % BUNS  # Left over hot dog buns
    min_buns = math.ceil(total / BUNS)        # Minimum packages of hot dog buns

    # Output the results
    show_results(dogs_left, min_dogs, buns_left, min_buns)

def get_total_hot_dogs():
    # Local variables
    people = int(input("Enter the number of people attending the cookout: "))
    hot_dogs = int(input("Enter the number of hot dogs for each person: "))

    # Calculate the total number of hot dogs needed.
    total = people * hot_dogs
    return total

def show_results(dogs_left, min_dogs, buns_left, min_buns):
    # Display the minimum packages of hot dogs needed.
    print(f"Minimum packages of hot dogs needed: {min_dogs}")

    # Display the minimum packages of buns needed.
    print(f"Minimum packages of hot dog buns needed: {min_buns}")

    # Display the number of hot dogs left over.
    print(f"Hot dogs left over: {dogs_left}")

    # Display the number of hot dog buns left over.
    print(f"Hot dog buns left over: {buns_left}")

# Run the main function
if __name__ == "__main__":
    main()
