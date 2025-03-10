# Define the points and impossible events (adjust impossible based on actual data)
points = [
    [10, 50, 20],   # Day 1
    [20, 40, 10],   # Day 2
    [10, 70, 50],   # Day 3
    [10, 20, 20],   # Day 4
    [10, 10, 20],   # Day 5
    [10, 90, 20],   # Day 6
    [20, 100, 20],  # Day 7
    [20, 50, 50],   # Day 8
    [70, 10, 50],   # Day 9
    [70, 10, 20],   # Day 10
]

# If any events are impossible, mark them here. Currently all are possible.
impossible = [
    [False, False, False] for _ in range(10)
]

valid_combinations = [(), (0,), (1,), (2,), (0, 2)]

# Preprocess each day to get valid combinations and their points and events
preprocessed_days = []
for day in range(10):
    possible = []
    for comb in valid_combinations:
        # Check if all shifts in combination are possible
        valid = True
        for shift in comb:
            if impossible[day][shift]:
                valid = False
                break
        if not valid:
            continue
        # Calculate points and events
        points_sum = sum(points[day][shift] for shift in comb)
        events = [(day + 1, shift) for shift in comb]
        possible.append((comb, points_sum, events))
    preprocessed_days.append(possible)

# Initialize DP: previous day's shifts -> (total points, path)
dp_prev = { (): (0, []) }

for day in range(10):
    dp_current = {}
    current_combinations = preprocessed_days[day]
    for prev_shifts, (prev_total, prev_path) in dp_prev.items():
        for comb in current_combinations:
            curr_shifts, curr_points, curr_events = comb
            # Check if current shifts overlap with previous day's shifts
            overlap = any(shift in prev_shifts for shift in curr_shifts)
            if overlap:
                continue
            new_total = prev_total + curr_points
            new_path = prev_path + curr_events
            # Update dp_current if this is a better path
            if curr_shifts not in dp_current or new_total > dp_current[curr_shifts][0]:
                dp_current[curr_shifts] = (new_total, new_path)
    dp_prev = dp_current

# Find the maximum points and corresponding path
max_points = 0
best_path = []
for shifts, (total, path) in dp_prev.items():
    if total > max_points:
        max_points = total
        best_path = path

# Format the output
event_list = []
for event in best_path:
    day, shift = event
    time = ""
    if shift == 0:
        time = "Morning"
    elif shift == 1:
        time = "Afternoon"
    else:
        time = "Evening"
    event_list.append(f"Day {day} {time}")

print("Array of events:", event_list)
print("Maximum points:", max_points)