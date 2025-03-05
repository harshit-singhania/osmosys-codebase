using System; 

public class InvalidAgeException : Exception {
    public InvalidAgeException() {

    }

    public InvalidAgeException(string message) : base(message) {

    }
}

class Program {
    static void checkAge(int age) {
        if (age < 18) {
            throw new InvalidAgeException("Age is less than 18");
        } else {
            Console.WriteLine("Age is: " + age);
        }
    }

    static void Main() {
        try {
            Console.WriteLine("Enter your age: ");
            int age = Convert.ToInt32(Console.ReadLine());
            checkAge(age);
        }
        catch (InvalidAgeException e) {
            Console.WriteLine("Invalid Age Exception: " + e.Message);
        }
        catch (Exception e) {
            Console.WriteLine("Exception: " + e.Message);
        }
    }
}