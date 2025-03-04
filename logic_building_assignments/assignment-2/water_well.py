def calculate_time_to_fill_drum(family_members, drum_capacity):
    """
    Calculate how long it takes to fill the drum based on family members' capabilities.
    
    Parameters:
    - family_members: List of dictionaries containing each person's parameters
    - drum_capacity: The size of the drum to fill (in liters)
    
    Returns:
    - Time to fill the drum in minutes
    """
    # Calculate the rate at which water is added to the drum
    total_rate_per_minute = 0
    
    print("Family member contribution rates:")
    
    # Calculate each person's contribution rate
    for person in family_members:
        # Calculate effective water per trip
        max_water = min(person["drawing_capacity"], person["container_size"])
        effective_water = max_water * (1 - person["dropping_percentage"]/100)
        
        # Calculate trips per minute
        avg_trip_time = person["avg_trip_time"]
        trips_per_minute = 1 / avg_trip_time
        
        # Calculate liters per minute contribution
        rate = effective_water * trips_per_minute
        total_rate_per_minute += rate
        
        print(f"- {person['name']}: {effective_water:.2f} liters × {trips_per_minute:.4f} trips/min = {rate:.2f} liters/min")
    
    # Calculate time to fill the drum
    time_to_fill = drum_capacity / total_rate_per_minute
    
    return time_to_fill, total_rate_per_minute

# Define family members with their attributes
family = [
    {
        "name": "Father",
        "drawing_capacity": 10,      # liters per draw
        "container_size": 15,        # maximum liters they can carry
        "dropping_percentage": 5,    # percentage of water they spill
        "avg_trip_time": 2.2         # average minutes per trip
    },
    {
        "name": "Mother",
        "drawing_capacity": 8,
        "container_size": 10,
        "dropping_percentage": 3,
        "avg_trip_time": 2.5
    },
    {
        "name": "Daughter (18 yrs)",
        "drawing_capacity": 7,
        "container_size": 8,
        "dropping_percentage": 7,
        "avg_trip_time": 3.0
    },
    {
        "name": "Son (10 yrs)",
        "drawing_capacity": 4,
        "container_size": 5,
        "dropping_percentage": 10,
        "avg_trip_time": 4.0
    }
]

# Drum capacity in liters
drum_capacity = 100

# Calculate the time to fill the drum
time, rate = calculate_time_to_fill_drum(family, drum_capacity)

# Display results
print(f"\nTotal family contribution rate: {rate:.2f} liters per minute")
print(f"Time to fill the {drum_capacity}-liter drum: {time:.2f} minutes")

# Show individual contributions to filling the drum
print("\nIndividual contributions to filling the drum:")
for person in family:
    # Calculate effective water per trip
    max_water = min(person["drawing_capacity"], person["container_size"])
    effective_water = max_water * (1 - person["dropping_percentage"]/100)
    
    # Calculate trips per minute and total trips needed
    trips_per_minute = 1 / person["avg_trip_time"]
    trips_needed = (time * trips_per_minute)
    water_contributed = trips_needed * effective_water
    percentage = (water_contributed / drum_capacity) * 100
    
    print(f"- {person['name']}: {water_contributed:.2f} liters ({percentage:.1f}% of total)")