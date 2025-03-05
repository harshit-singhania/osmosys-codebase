// an abstract class in C# is a class that cannot be instantiated, and can only be used as a base class for 
// other classes in order to derive from it. an abstract class can have abstract properties and methods 
// that must be implemented in the derived class.

// example of an abstract class

using System;

abstract class Animal {
    public abstract void Walk(); 
    public abstract void Eat();

    public abstract void Sleep(); 
}

class Dog : Animal {
    public override void Walk() {
        Console.WriteLine("Dog is walking");
    }

    public override void Eat() {
        Console.WriteLine("Dog is eating");
    }

    public override void Sleep() {
        Console.WriteLine("Dog is sleeping");
    }
}

class Program {
    static void Main() {
        Dog dog = new Dog();
        dog.Walk();
        dog.Eat();
        dog.Sleep();
    }
}