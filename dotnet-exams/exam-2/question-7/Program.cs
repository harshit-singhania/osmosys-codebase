using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main(string[] args)
    {
        // Define the Students list
        var students = new List<Student>
        {
            new Student { Id = 1, FirstName = "John", LastName = "Doe", SchoolId = 2 },
            new Student { Id = 2, FirstName = "Lorem", LastName = "Ipsum", SchoolId = 4 },
            new Student { Id = 3, FirstName = "Ram", LastName = "Kapoor", SchoolId = 1 }
        };

        // Define the Schools list
        var schools = new List<School>
        {
            new School { Id = 1, SchoolName = "Sister Stanislas English School" },
            new School { Id = 2, SchoolName = "St. Joseph’s English School" },
            new School { Id = 3, SchoolName = "Kendriya Vidyalaya, Hyderabad" }
        };

        // Task 1: Find the students whose last name starts with a vowel
        var vowels = new HashSet<char> { 'A', 'E', 'I', 'O', 'U' };

        var studentsWithVowelLastName =
            from student in students
            where vowels.Contains(char.ToUpper(student.LastName[0]))
            select student;

        Console.WriteLine("Task 1: Students whose last name starts with a vowel:");
        foreach (var student in studentsWithVowelLastName)
        {
            Console.WriteLine($"{student.FirstName} {student.LastName}");
        }

        // Task 2: Find the first student by ID from a School X (X is input)
        Console.Write("Enter the school name: ");
        string schoolName = Console.ReadLine();

        var firstStudentFromSchool =
            (from student in students
             join school in schools on student.SchoolId equals school.Id
             where school.SchoolName == schoolName
             orderby student.Id
             select student).FirstOrDefault();

        Console.WriteLine("\nTask 2: First student from the specified school:");
        if (firstStudentFromSchool != null)
        {
            Console.WriteLine($"{firstStudentFromSchool.FirstName} {firstStudentFromSchool.LastName}");
        }
        else
        {
            Console.WriteLine($"No students found from {schoolName}");
        }

        // Task 3: Find the count of students from each school
        var studentCountBySchool =
            from student in students
            join school in schools on student.SchoolId equals school.Id into studentGroup
            from sg in studentGroup.DefaultIfEmpty()
            group sg by sg?.SchoolName into g
            select new
            {
                SchoolName = g.Key ?? "Unknown School",
                StudentCount = g.Count(s => s != null)
            };

        Console.WriteLine("\nTask 3: Count of students from each school:");
        foreach (var item in studentCountBySchool)
        {
            Console.WriteLine($"{item.SchoolName}: {item.StudentCount}");
        }

        // Task 4: Add a list of students to an existing list
        var newStudents =
            from student in new[]
            {
                new Student { Id = 4, FirstName = "Alice", LastName = "Smith", SchoolId = 3 },
                new Student { Id = 5, FirstName = "Bob", LastName = "Johnson", SchoolId = 2 }
            }
            select student;

        students.AddRange(newStudents);

        Console.WriteLine("\nTask 4: Updated student list after adding new students:");
        foreach (var student in students)
        {
            Console.WriteLine($"{student.Id}: {student.FirstName} {student.LastName}");
        }
    }
}

// Define the Student class
public class Student
{
    public int Id { get; set; }
    public string FirstName { get; set; }
    public string LastName { get; set; }
    public int SchoolId { get; set; }
}

// Define the School class
public class School
{
    public int Id { get; set; }
    public string SchoolName { get; set; }
}