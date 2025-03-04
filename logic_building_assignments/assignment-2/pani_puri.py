def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def simulate_pani_puri_stall():
    # Initial parameters
    total_puris = 2000
    puris_per_plate = 6
    plate_cost = 30
    seconds_per_puri = 6
    
    # Track earnings and time
    total_earnings = 0
    current_minute = 0  # Minutes after 5:00 PM
    queue = []  # List to track arrival time of each plate in queue
    max_wait_time = 0
    
    # Track plates served for breakage calculation
    plates_served = 0
    
    # Run simulation until puris are exhausted
    while total_puris > 0:
        # Calculate current hour and minute
        hour = 17 + (current_minute // 60)  # Starting at 17:00 (5:00 PM)
        minute = current_minute % 60
        
        # Handle day change
        if hour >= 24:
            hour -= 24
        
        # Calculate digit sum for current time
        time_str = f"{hour}{minute:02d}"  # Format: HHMM
        digit_sum = sum(int(digit) for digit in time_str)
        
        # Check if customers arrive at this minute
        if is_prime(digit_sum):
            group_size = minute % 10  # Unit digit of current minute
            
            if group_size > 0:
                # Calculate waiting time for this group
                waiting_time = len(queue) * puris_per_plate * seconds_per_puri
                if waiting_time > max_wait_time:
                    max_wait_time = waiting_time
                
                # Add this group's plates to the queue
                for _ in range(group_size):
                    queue.append(current_minute)
        
        # Process serving: 10 puris per minute (60 seconds / 6 seconds per puri)
        puris_to_serve = min(10, len(queue) * puris_per_plate)
        
        # Calculate how many plates are fully served
        plates_to_serve = puris_to_serve // puris_per_plate
        
        if plates_to_serve > 0:
            # Remove served plates from queue
            queue = queue[plates_to_serve:]
            
            # Calculate total puris used including breakage
            breakage = plates_to_serve // 3  # One puri breaks for every 3 plates
            puris_used = plates_to_serve * puris_per_plate + breakage
            
            # Update tracking variables
            total_puris -= puris_used
            total_earnings += plates_to_serve * plate_cost
            plates_served += plates_to_serve
        
        # Move to next minute
        current_minute += 1
        
        # If we don't have enough puris for even one more plate
        if total_puris < puris_per_plate + 1:  # +1 for potential breakage
            break
    
    # Calculate end time
    end_hour = 17 + (current_minute // 60)
    end_minute = current_minute % 60
    if end_hour >= 24:
        end_hour -= 24
    
    # Format max wait time
    max_wait_minutes = max_wait_time // 60
    max_wait_seconds = max_wait_time % 60
    
    return {
        "total_earnings": total_earnings,
        "end_time": f"{end_hour:02d}:{end_minute:02d}",
        "max_wait": f"{max_wait_minutes} minutes and {max_wait_seconds} seconds"
    }

# Run the simulation
results = simulate_pani_puri_stall()
print(f"Total earnings: Rs. {results['total_earnings']}")
print(f"All pani puris sold out by: {results['end_time']}")
print(f"Maximum waiting time for any batch: {results['max_wait']}")
