def calculate_minimum_search_time(sections=10, shelves_per_section=50, books_per_shelf=30, 
                                num_students=5, seconds_per_book=30):
    """
    Calculate minimum time required to find a book with a specific topic.
    
    Args:
        sections: Number of sections in the library
        shelves_per_section: Number of shelves in each section
        books_per_shelf: Number of books on each shelf
        num_students: Number of students searching
        seconds_per_book: Time in seconds to check one book
        
    Returns:
        Dictionary containing total time in seconds, hours, minutes, and seconds
    """
    # Calculate total books in the library
    total_books = sections * shelves_per_section * books_per_shelf
    
    # Calculate books per student (using divide and conquer)
    books_per_student = total_books // num_students
    
    # In the worst case, the book with the required topic is the last one checked
    worst_case_time_seconds = books_per_student * seconds_per_book
    
    # Convert to hours, minutes, seconds for better readability
    hours = worst_case_time_seconds // 3600
    minutes = (worst_case_time_seconds % 3600) // 60
    seconds = worst_case_time_seconds % 60
    
    return {
        "total_books": total_books,
        "books_per_student": books_per_student,
        "total_seconds": worst_case_time_seconds,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    }

def run_test_case(name, **kwargs):
    """Run a test case with the given parameters"""
    print(f"\n=== Test Case: {name} ===")
    
    # Use default values for any parameters not provided
    result = calculate_minimum_search_time(**kwargs)
    
    # Display results
    print(f"Library size: {result['total_books']} books")
    print(f"Books per student: {result['books_per_student']}")
    print(f"Minimum search time: {result['total_seconds']} seconds")
    print(f"                   = {result['hours']} hours, {result['minutes']} minutes, {result['seconds']} seconds")

def run_all_tests():
    # Test Case 1: Default scenario from the problem
    run_test_case("Default Library Configuration")
    
    # Test Case 2: Small library
    run_test_case("Small Library", 
                 sections=2, 
                 shelves_per_section=10, 
                 books_per_shelf=15)
    
    # Test Case 3: More students
    run_test_case("More Students", 
                 num_students=10)
    
    # Test Case 4: Fewer students
    run_test_case("Fewer Students", 
                 num_students=3)
    
    # Test Case 5: Quicker book checking
    run_test_case("Faster Book Checking", 
                 seconds_per_book=15)
    
    # Test Case 6: Large library
    run_test_case("Large Library", 
                 sections=20, 
                 shelves_per_section=100, 
                 books_per_shelf=40)
    
    # Test Case 7: Combination of parameters
    run_test_case("Optimized Search", 
                 sections=10, 
                 shelves_per_section=50, 
                 books_per_shelf=30,
                 num_students=8, 
                 seconds_per_book=20)

# Run all test cases
if __name__ == "__main__":
    run_all_tests()