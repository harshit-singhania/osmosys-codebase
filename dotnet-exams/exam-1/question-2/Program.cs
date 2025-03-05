// there are several differences between type casting and type conversion, including:
// type casting is the process of converting a variable from one type to another done by the programmer while type conversion 
// is the process of converting a variable from one type to another. Type casting can happen at both compile time and run time, 
// depending on the type of casting being performed. While type conversion can only happen at run time. 

// type casting is done generally for the primitive data types, while type conversion can be done for both primitive and non-primitive data types.

// it is possible to do type casting in a user defined data type

// example of type casting

using System;

class Distance
{
    private double meters;

    public Distance(double meters)
    {
        this.meters = meters;
    }

    // Explicit conversion operator from Distance to int
    public static explicit operator int(Distance d)
    {
        return (int)d.meters;
    }

    public double GetMeters()
    {
        return meters;
    }
}

class Program
{
    static void Main()
    {
        // Example 1: Casting a double to an integer
        double doubleValue = 123.45;
        int intValue = (int)doubleValue; // Explicit cast (truncates decimal)
        Console.WriteLine($"Double to int: {intValue}");

        // Example 2: Casting a char to an integer
        char character = 'A';
        int asciiValue = (int)character; // Converts 'A' to its ASCII value (65)
        Console.WriteLine($"Char to int (ASCII): {asciiValue}");

        // Example 3: Converting a string to an integer using Convert class
        string numberString = "123";
        int convertedNumber = Convert.ToInt32(numberString);
        Console.WriteLine($"String to int: {convertedNumber}");

        // Using the Distance class with parameterized constructor
        Distance distance = new Distance(100.5);

        // Explicitly casting Distance to int
        int meters = (int)distance;
        Console.WriteLine($"Distance to int: {meters}");
    }
}