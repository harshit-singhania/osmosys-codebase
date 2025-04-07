def can_finish_books(pages, difficulty, p, h):
    total_hours = 0
    
    for i in range(len(pages)):
        # Calculate effective reading speed (ceiling of p/d)
        effective_pages = (p + difficulty[i] - 1) // difficulty[i]
        
        # Hours needed to finish this book (ceiling of pages/effectivePages)
        hours_needed = (pages[i] + effective_pages - 1) // effective_pages
        
        total_hours += hours_needed
        if total_hours > h:
            return False
    
    return True

def min_reading_pace(pages, difficulty, h):
    left, right = 1, 10**18  # Large upper bound
    
    while left < right:
        mid = left + (right - left) // 2
        
        if can_finish_books(pages, difficulty, mid, h):
            right = mid
        else:
            left = mid + 1
    
    return left

if __name__ == "__main__":
    
    # Test cases
    test_cases = [
        ([150, 200, 350, 100], [2, 3, 4, 1], 20),
        ([80, 120, 60], [2, 1, 3], 10)
    ]
    
    for pages, difficulty, h in test_cases:
        print(f"Test case - Pages: {pages}, Difficulty: {difficulty}, Hours: {h}")
        print("Minimum Reading Pace:", min_reading_pace(pages, difficulty, h))
        print()
