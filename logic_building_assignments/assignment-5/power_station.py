def simulate_power_grid(initial_fuel, town_consumption, restoration_threshold, fuel_rate, start_day="Sunday"):
    """
    Simulates the power grid operation with limited fuel.
    
    Args:
        initial_fuel: Initial fuel in KL
        town_consumption: List of daily power consumption per town (kWh)
        restoration_threshold: Fuel level that triggers restoration (KL)
        fuel_rate: Fuel consumption rate (Liters/kWh)
        start_day: Starting day of the week
    
    Returns:
        Dictionary containing blackout logs, complete blackout days, and restoration day
    """
    # Initialize
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    day_index = days.index(start_day)
    fuel = initial_fuel * 1000  # Convert to Liters
    
    # Sort towns by consumption for blackout priority
    towns_sorted = sorted(enumerate(town_consumption), key=lambda x: x[1])
    
    # Track blackouts and days
    day_counter = 1
    blackout_logs = []
    complete_blackout_days = []
    restoration_day = None
    restoration_active = False
    restoration_fuel = 0
    
    # Generate Fibonacci numbers up to a reasonable limit
    fib = [1, 2]
    while fib[-1] < 1000:  # Assuming we won't simulate for more than 1000 days
        fib.append(fib[-1] + fib[-2])
    
    while True:
        current_day = days[day_index]
        
        # Check if it's a Fibonacci day for fuel recharge
        if day_counter in fib and not restoration_active:
            fib_index = fib.index(day_counter)
            extra_fuel = fib[fib_index] * 10
            fuel += extra_fuel
            print(f"Day {day_counter} ({current_day}): Fibonacci day! Added {extra_fuel}L fuel")
        
        # Calculate heat dissipation based on day
        heat_dissipation = 10 if day_index >= 1 and day_index <= 5 else 15  # Weekday vs Weekend
        
        # If in restoration mode
        if restoration_active:
            if day_counter == restoration_start_day + 1:
                restoration_fuel = 10  # First day of restoration
            else:
                restoration_fuel += restoration_fuel * 0.1  # 10% increase each day
            
            print(f"Day {day_counter} ({current_day}): Restoration in progress. Fuel = {restoration_fuel:.2f}L")
            
            # Check if restoration is complete
            if restoration_fuel + fuel >= restoration_threshold * 1000:
                fuel += restoration_fuel
                restoration_active = False
                restoration_day = day_counter
                print(f"Day {day_counter} ({current_day}): Restoration complete! Fuel = {fuel:.2f}L")
                break
        else:
            # Calculate power needs
            total_consumption = sum(town_consumption) + heat_dissipation
            fuel_needed = total_consumption * fuel_rate
            
            # Check if we have enough fuel
            if fuel >= fuel_needed:
                # We have enough fuel for everyone
                fuel -= fuel_needed
                print(f"Day {day_counter} ({current_day}): All towns powered. Remaining fuel: {fuel:.2f}L")
            else:
                # Not enough fuel, need to do blackouts
                blackout_towns = []
                available_power = fuel / fuel_rate
                remaining_power = available_power - heat_dissipation
                
                if remaining_power <= 0:
                    # Complete blackout
                    blackout_towns = list(range(len(town_consumption)))
                    complete_blackout_days.append(day_counter)
                    print(f"Day {day_counter} ({current_day}): COMPLETE BLACKOUT! No power available after heat dissipation.")
                else:
                    # Partial blackout
                    power_needed = total_consumption - heat_dissipation
                    towns_to_power = list(range(len(town_consumption)))
                    
                    for town_idx, consumption in towns_sorted:
                        if remaining_power < consumption:
                            blackout_towns.append(town_idx)
                            towns_to_power.remove(town_idx)
                        else:
                            remaining_power -= consumption
                    
                    print(f"Day {day_counter} ({current_day}): Towns {blackout_towns} experiencing blackout.")
                
                # Record blackout information
                if blackout_towns:
                    blackout_logs.append({
                        "day": day_counter,
                        "weekday": current_day,
                        "towns": blackout_towns
                    })
                
                # Check if we need to start restoration
                if fuel < restoration_threshold * 1000 and not restoration_active:
                    restoration_active = True
                    restoration_start_day = day_counter
                    print(f"Day {day_counter} ({current_day}): Fuel below threshold, starting restoration.")
                
                # Use available fuel
                actual_consumption = heat_dissipation
                for town_idx in range(len(town_consumption)):
                    if town_idx not in blackout_towns:
                        actual_consumption += town_consumption[town_idx]
                
                fuel_used = min(fuel, actual_consumption * fuel_rate)
                fuel -= fuel_used
        
        # Move to next day
        day_counter += 1
        day_index = (day_index + 1) % 7
        
        # Safety check to prevent infinite loops
        if day_counter > 1000 and not restoration_active:
            print("Simulation exceeded 1000 days without reaching restoration, stopping.")
            break
    
    return {
        "blackout_logs": blackout_logs,
        "complete_blackout_days": complete_blackout_days,
        "restoration_day": restoration_day
    }

# Run the simulation with given parameters
if __name__ == "__main__":
    initial_fuel = 50  # KL
    town_consumption = [3000, 2200, 1200, 4400, 3500]  # kWh
    restoration_threshold = 10  # KL
    fuel_rate = 0.25  # Liters/kWh
    
    results = simulate_power_grid(initial_fuel, town_consumption, restoration_threshold, fuel_rate, "Sunday")
    
    print("\n===== SUMMARY =====")
    print(f"Blackout events occurred on {len(results['blackout_logs'])} days")
    print(f"Complete blackout days: {results['complete_blackout_days']}")
    print(f"Restoration completed on day: {results['restoration_day']}")
    
    print("\n===== DETAILED BLACKOUT LOGS =====")
    for log in results['blackout_logs']:
        print(f"Day {log['day']} ({log['weekday']}): Towns {log['towns']} without power")