
using System;

class Calculator {

    // returns sum as integer
    public int Add(int[] numbers) {
        int sum = 0; 
        foreach (int num in numbers) {
            sum += num;
        }
        return sum;
    }

    // returns sum as double
    public double Add(double[] numbers) {
        double sum = 0; 
        foreach (double num in numbers) {
            sum += num;
        }
        return sum;
    }

    // returns int as string 
    public string AddToString(int[] numbers) {
        int sum = 0; 
        foreach (int num in numbers) {
            sum += num;
        }
        return sum.ToString();
    }

    // returns double as string
    public string AddToString(double[] numbers) {
        double sum = 0; 
        foreach (double num in numbers) {
            sum += num;
        }
        return sum.ToString();
    }
}

class Program {
    static void Main() {
        int[] intNumbers = {1, 2, 3, 4, 5};
        double[] doubleNumbers = {1.1, 2.2, 3.3, 4.4, 5.5};

        Calculator calculator = new Calculator();
        
        int intSum = calculator.Add(intNumbers);
        double doubleSum = calculator.Add(doubleNumbers);
        string intSumString = calculator.AddToString(intNumbers);
        string doubleSumString = calculator.AddToString(doubleNumbers);

        Console.WriteLine($"Sum of integers: {intSum}");
        Console.WriteLine($"Sum of doubles: {doubleSum}");
        Console.WriteLine($"Sum of integers as string: {intSumString}");
        Console.WriteLine($"Sum of doubles as string: {doubleSumString}");
    }
}