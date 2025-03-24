using System;

public static class StringExtensions
{
    public static string ToPascalCase(this string input)
    {
        if (string.IsNullOrEmpty(input))
        {
            return input;
        }
        return char.ToUpper(input[0]) + input.Substring(1);
    }
}

class Program
{
    static void Main(string[] args)
    {
        // Example usage
        string camelCaseString = "helloWorld";
        string pascalCaseString = camelCaseString.ToPascalCase();

        Console.WriteLine($"CamelCase: {camelCaseString}");
        Console.WriteLine($"PascalCase: {pascalCaseString}");
    }
}