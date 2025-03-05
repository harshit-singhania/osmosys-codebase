using System;

interface IVehicle {
    void Drive();
    void Stop();
    void DisplayInfo();
}

// Car class implementing IVehicle
class Car : IVehicle {
    private string make;
    private string model;
    private int year;

    // Parameterized constructor
    public Car(string make, string model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }

    public void Drive() {
        Console.WriteLine("Car is being driven");
    }

    public void Stop() {
        Console.WriteLine("Car has stopped");
    }

    public void DisplayInfo() {
        Console.WriteLine($"This is a {year} {make} {model}");
    }
}

// Bike class implementing IVehicle
class Bike : IVehicle {
    private string make;
    private string model;
    private int year;

    // Parameterized constructor
    public Bike(string make, string model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }

    public void Drive() {
        Console.WriteLine("Bike is being driven");
    }

    public void Stop() {
        Console.WriteLine("Bike has stopped");
    }

    public void DisplayInfo() {
        Console.WriteLine($"This is a {year} {make} {model}");
    }
}

class Program {
    static void Main() {
        // Using parameterized constructors to initialize objects
        Car car = new Car("Toyota", "Corolla", 2020);
        Bike bike = new Bike("Honda", "CBR", 2019);

        car.Drive();
        car.Stop();
        car.DisplayInfo();

        bike.Drive();
        bike.Stop();
        bike.DisplayInfo();
    }
}