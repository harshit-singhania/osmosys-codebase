def make_coffee(kettle_available_at, microwave_available_at, stove_available_at, arrival_time):
    """
    Simulates the process of making a cup of coffee with optimal scheduling.
    
    Args:
        kettle_available_at: Time when kettle becomes available
        microwave_available_at: Time when microwave becomes available
        stove_available_at: Time when stove becomes available
        arrival_time: Time when person arrives
    
    Returns:
        tuple: (completion_time, new_kettle_time, new_microwave_time, new_stove_time)
    """
    # Start time is when person can begin using the first available appliance
    current_time = arrival_time
    
    # Calculate when we can start boiling water
    kettle_start_time = max(current_time, kettle_available_at)
    kettle_end_time = kettle_start_time + (250/1000) * 30  # 250ml at rate of 1L/30s 
    
    # Calculate when milk heating can start on each appliance
    microwave_start_time = max(current_time, microwave_available_at)
    microwave_end_time = microwave_start_time + 30  # 30 seconds in microwave
    
    stove_start_time = max(current_time, stove_available_at)
    stove_end_time = stove_start_time + 40  # 40 seconds on stove
    
    # Choose the appliance that will finish milk heating first
    if microwave_end_time <= stove_end_time:
        milk_end_time = microwave_end_time
        new_microwave_available_at = microwave_end_time
        new_stove_available_at = stove_available_at
    else:
        milk_end_time = stove_end_time
        new_microwave_available_at = microwave_available_at
        new_stove_available_at = stove_end_time
    
    # Time when both water and milk are ready
    heating_completion_time = max(kettle_end_time, milk_end_time)
    
    # Ingredients (coffee + sugar) take 10 seconds total
    # Calculate how much waiting time we have during the process
    # This is time we're waiting for appliances or while they're running
    total_process_time = heating_completion_time - arrival_time
    
    # If we have enough waiting time (≥10s), we can add ingredients during heating
    # Otherwise, we need extra time after heating
    ingredients_time_needed = 10  # 5s per spoon × 2
    
    if total_process_time >= ingredients_time_needed:
        completion_time = heating_completion_time
    else:
        # Need extra time to finish adding ingredients
        completion_time = heating_completion_time + (ingredients_time_needed - total_process_time)
    
    return (completion_time, kettle_end_time, new_microwave_available_at, new_stove_available_at)

def simulate_coffee_queue(num_people, arrival_interval=0):
    """
    Simulates multiple people making coffee.
    
    Args:
        num_people: Number of people in queue
        arrival_interval: Time between each person's arrival (0 means all arrive at once)
        
    Returns:
        list: Details about each person's coffee preparation
    """
    kettle_available_at = 0
    microwave_available_at = 0
    stove_available_at = 0
    
    results = []
    
    for i in range(num_people):
        arrival_time = i * arrival_interval
        
        completion_time, kettle_available_at, microwave_available_at, stove_available_at = make_coffee(
            kettle_available_at, microwave_available_at, stove_available_at, arrival_time
        )
        
        wait_time = completion_time - arrival_time
        results.append({
            "person": i+1,
            "arrival_time": arrival_time,
            "completion_time": completion_time,
            "wait_time": wait_time
        })
    
    return results

if __name__ == "__main__":
    # Simulate 5 people arriving at 10-second intervals
    results = simulate_coffee_queue(10, 10)
    
    print("Coffee Making Simulation Results:")
    print("=" * 50)
    for person in results:
        print(f"Person {person['person']}:")
        print(f"  Arrival time: {person['arrival_time']} seconds")
        print(f"  Completion time: {person['completion_time']:.1f} seconds")
        print(f"  Total wait time: {person['wait_time']:.1f} seconds")
        print("-" * 30)
    
    # Calculate average wait time
    avg_wait = sum(person['wait_time'] for person in results) / len(results)
    print(f"Average wait time: {avg_wait:.1f} seconds")