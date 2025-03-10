def find_charging_strategy(battery_capacity, current_charge_percent, current_location, 
                          destination, consumption_rate, charging_stations, driving_speed=100):
    """
    Find a simplified charging strategy to minimize total time.
    
    Args:
        battery_capacity: Battery capacity in kWh
        current_charge_percent: Current charge percentage (0-100)
        current_location: Current position in km
        destination: Destination in km
        consumption_rate: Energy consumption in kWh per km
        charging_stations: List of charging station dictionaries
        driving_speed: Driving speed in km/h
    """
    # Initialize variables
    current_charge = battery_capacity * (current_charge_percent / 100)  # kWh
    max_range = current_charge / consumption_rate  # km
    current_pos = current_location
    total_time = 0
    total_cost = 0
    journey = []
    
    # Sort stations by location
    stations = sorted(charging_stations, key=lambda s: s['location'])
    
    while current_pos < destination:
        # Check if we can reach destination directly
        if destination - current_pos <= max_range:
            # Calculate travel time to destination
            travel_time = (destination - current_pos) / driving_speed
            total_time += travel_time
            
            # Record journey step
            journey.append(f"Drive from {current_pos}km to {destination}km ({destination - current_pos}km)")
            journey.append(f"  Travel time: {travel_time:.2f} hours")
            
            # Update position
            current_pos = destination
            break
        
        # Find reachable stations
        reachable_stations = []
        for station in stations:
            if station['location'] > current_pos and station['location'] - current_pos <= max_range:
                reachable_stations.append(station)
        
        # If no stations are reachable, the journey is impossible
        if not reachable_stations:
            return f"Cannot complete journey. No reachable charging stations from {current_pos}km with {max_range:.1f}km range."
        
        # Simple strategy: Choose station based on a combined score of:
        # - Queue time
        # - Charging speed
        # - Distance progress
        best_station = None
        best_score = float('inf')
        
        for station in reachable_stations:
            # Calculate how long it takes to reach the station
            distance = station['location'] - current_pos
            travel_time = distance / driving_speed
            
            # Calculate remaining charge upon arrival at station
            charge_used = distance * consumption_rate
            arrival_charge = current_charge - charge_used
            
            # Target charge: Either 80% of capacity or enough to reach next station + 20% buffer
            next_station_loc = destination
            for s in stations:
                if s['location'] > station['location']:
                    next_station_loc = s['location']
                    break
                    
            distance_to_next = next_station_loc - station['location']
            charge_needed = min(
                0.8 * battery_capacity - arrival_charge,  # Up to 80% charge
                (distance_to_next * consumption_rate) * 1.2  # Plus 20% buffer
            )
            
            if charge_needed <= 0:
                charge_needed = 0  # No need to charge
            
            # Calculate queue and charging time
            queue_time = station['queue_length'] * station.get('avg_charging_time', 0.5)
            charging_time = charge_needed / (station['charging_speed'] / 60)
            
            # Calculate score (lower is better)
            # Consider: travel time, waiting time, charging time, and progress toward destination
            progress_ratio = distance / (destination - current_pos)
            time_penalty = travel_time + queue_time + charging_time
            
            score = time_penalty / progress_ratio
            
            if score < best_score:
                best_score = score
                best_station = {
                    'station': station,
                    'travel_time': travel_time,
                    'arrival_charge': arrival_charge,
                    'charge_needed': charge_needed,
                    'queue_time': queue_time,
                    'charging_time': charging_time,
                }
        
        # Use the best station
        station = best_station['station']
        charge_cost = best_station['charge_needed'] * station['cost_per_kwh']
        
        # Record journey step - driving to the station
        journey.append(f"Drive from {current_pos}km to {station['location']}km ({station['location'] - current_pos}km)")
        journey.append(f"  Travel time: {best_station['travel_time']:.2f} hours")
        
        # Record charging step
        if best_station['charge_needed'] > 0:
            from_percent = (best_station['arrival_charge'] / battery_capacity) * 100
            to_percent = ((best_station['arrival_charge'] + best_station['charge_needed']) / battery_capacity) * 100
            
            journey.append(f"Charge at station {station['location']}km:")
            journey.append(f"  From {from_percent:.1f}% to {to_percent:.1f}%")
            journey.append(f"  Queue time: {best_station['queue_time']:.2f} hours")
            journey.append(f"  Charging time: {best_station['charging_time']:.2f} hours")
            journey.append(f"  Cost: ${charge_cost:.2f}")
        
        # Update status
        current_pos = station['location']
        current_charge = best_station['arrival_charge'] + best_station['charge_needed']
        max_range = current_charge / consumption_rate
        total_time += best_station['travel_time'] + best_station['queue_time'] + best_station['charging_time']
        total_cost += charge_cost
    
    # Final summary
    journey.append(f"\nTotal journey summary:")
    journey.append(f"  Total time: {total_time:.2f} hours")
    journey.append(f"  Total cost: ${total_cost:.2f}")
    
    return "\n".join(journey)

if __name__ == "__main__":
    # Sample test case
    battery_capacity = 75  # kWh (e.g., Tesla Model 3 Long Range)
    current_charge_percent = 20
    current_location = 0
    destination_location = 400
    consumption_rate = 0.2  # kWh per km
    driving_speed = 100  # km/h
    
    # Sample charging stations
    charging_stations = [
        {'location': 50, 'charging_speed': 50, 'queue_length': 2, 'cost_per_kwh': 0.30, 'avg_charging_time': 0.5},
        {'location': 120, 'charging_speed': 150, 'queue_length': 3, 'cost_per_kwh': 0.45, 'avg_charging_time': 0.4},
        {'location': 200, 'charging_speed': 250, 'queue_length': 5, 'cost_per_kwh': 0.50, 'avg_charging_time': 0.35},
        {'location': 280, 'charging_speed': 120, 'queue_length': 1, 'cost_per_kwh': 0.40, 'avg_charging_time': 0.45},
        {'location': 350, 'charging_speed': 50, 'queue_length': 0, 'cost_per_kwh': 0.25, 'avg_charging_time': 0.5}
    ]
    
    # Find and print the charging strategy
    print(find_charging_strategy(
        battery_capacity,
        current_charge_percent,
        current_location,
        destination_location,
        consumption_rate,
        charging_stations,
        driving_speed
    ))