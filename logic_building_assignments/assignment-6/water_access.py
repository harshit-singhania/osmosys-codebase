def optimize_water_distribution(well_capacities, household_requirements, distances):
    """
    Optimize the assignment of households to wells to minimize total travel distance.
    
    Args:
        well_capacities: List of daily water capacity for each well
        household_requirements: List of daily water requirement for each household
        distances: 2D list where distances[h][w] is distance from household h to well w
        
    Returns:
        Dictionary mapping household indices to their assigned well indices
    """
    try:
        # Try to use PuLP for optimal solution via linear programming
        from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpStatus, value
        
        # Create optimization model
        model = LpProblem(name="water_distribution", sense=LpMinimize)
        
        num_households = len(household_requirements)
        num_wells = len(well_capacities)
        
        # Decision variables: x[h,w] = 1 if household h is assigned to well w
        x = {}
        for h in range(num_households):
            for w in range(num_wells):
                x[(h, w)] = LpVariable(f"x_{h}_{w}", 0, 1, cat="Binary")
        
        # Objective: Minimize total distance traveled
        model += lpSum(x[(h, w)] * distances[h][w] for h in range(num_households) 
                      for w in range(num_wells))
        
        # Constraint 1: Each household must be assigned to exactly one well
        for h in range(num_households):
            model += lpSum(x[(h, w)] for w in range(num_wells)) == 1
        
        # Constraint 2: Well capacity constraints
        for w in range(num_wells):
            model += lpSum(x[(h, w)] * household_requirements[h] 
                          for h in range(num_households)) <= well_capacities[w]
        
        # Solve the model
        model.solve()
        
        if LpStatus[model.status] != "Optimal":
            return None  # No feasible solution
        
        # Extract solution
        assignment = {}
        for h in range(num_households):
            for w in range(num_wells):
                if value(x[(h, w)]) > 0.5:  # Account for floating point
                    assignment[h] = w
        
        return assignment
        
    except ImportError:
        # Fallback to greedy approach if PuLP isn't available
        return greedy_water_distribution(well_capacities, household_requirements, distances)


def greedy_water_distribution(well_capacities, household_requirements, distances):
    """
    Greedy approach for water distribution assignment.
    """
    num_households = len(household_requirements)
    num_wells = len(well_capacities)
    
    # Track remaining capacity of each well
    remaining_capacity = well_capacities.copy()
    
    # Sort households by water requirement (highest first)
    households = [(h, household_requirements[h]) for h in range(num_households)]
    households.sort(key=lambda x: x[1], reverse=True)
    
    assignment = {}
    
    for h_id, requirement in households:
        # Find closest well with enough capacity
        well_distances = [(w, distances[h_id][w]) for w in range(num_wells)]
        well_distances.sort(key=lambda x: x[1])  # Sort by distance
        
        assigned = False
        for w_id, distance in well_distances:
            if remaining_capacity[w_id] >= requirement:
                assignment[h_id] = w_id
                remaining_capacity[w_id] -= requirement
                assigned = True
                break
        
        if not assigned:
            return None  # No feasible solution
    
    return assignment


def main():
    """Example usage with sample data"""
    # Sample data
    well_capacities = [100, 150, 200]
    
    household_requirements = [20, 15, 25, 10, 30, 25, 20, 15, 10, 40]
    
    distances = [
        [5, 10, 15],  # Distances from household 0 to all wells
        [8, 6, 12],   # Distances from household 1 to all wells
        [12, 8, 5],   # etc.
        [6, 15, 10],
        [9, 7, 11],
        [14, 6, 8],
        [7, 12, 11],
        [10, 9, 6],
        [5, 11, 15],
        [8, 10, 7]
    ]
    
    # Find optimal assignment
    assignment = optimize_water_distribution(well_capacities, household_requirements, distances)
    
    if assignment is None:
        print("No feasible solution exists.")
    else:
        # Display results
        print("Optimal Assignment:")
        well_usage = [0] * len(well_capacities)
        total_distance = 0
        
        for household, well in sorted(assignment.items()):
            distance = distances[household][well]
            requirement = household_requirements[household]
            well_usage[well] += requirement
            total_distance += distance
            
            print(f"Household {household} (needs {requirement} units) → Well {well} (distance: {distance})")
        
        print("\nWell Usage:")
        for well in range(len(well_capacities)):
            print(f"Well {well}: {well_usage[well]}/{well_capacities[well]} units " 
                  f"({well_usage[well]/well_capacities[well]*100:.1f}%)")
        
        print(f"\nTotal distance: {total_distance}")


if __name__ == "__main__":
    main()