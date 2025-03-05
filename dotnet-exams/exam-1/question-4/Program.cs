// there are 3 ways of passing a value by reference 
// ref: When the function modifies an existing variable. it is beneficial when swapping values, modifying settings
// out:	When the function returns multiple values. it is beneficial in cases where we are calculating sum and product, parsing
// in:	When passing large structs without modifying them it is beneficial to ensure performance optimization for large data


using System;

struct LargeStruct {
    public int x;
    public int y;
    public int z;
}

class Program {
    // using ref for swapping 
    static void Swap(ref int a, ref int b) {
        int temp = a;
        a = b;
        b = temp;
    }

    // using out for returning multiple values
    static void Calculate(int x, int y, out int sum, out int product) {
        sum = x + y;
        product = x * y;
    }

    // using in for passing large struct without modifying it
    static void Display(in LargeStruct largeStruct) {
        Console.WriteLine($"x: {largeStruct.x}, y: {largeStruct.y}, z: {largeStruct.z}");
    }

    static void Main() {
        int a = 10;
        int b = 20;

        Console.WriteLine($"Before swap: a = {a}, b = {b}");
        Swap(ref a, ref b);
        Console.WriteLine($"After swap: a = {a}, b = {b}");

        int x = 5;
        int y = 10;
        int sum;
        int product;

        Calculate(x, y, out sum, out product);
        Console.WriteLine($"Sum: {sum}, Product: {product}");

        LargeStruct largeStruct = new LargeStruct { x = 1, y = 2, z = 3 };
        Display(largeStruct);
    }
}