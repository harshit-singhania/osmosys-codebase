const employees = [
    { name: "Alice", age: 25, salary: 2500 },
    { name: "Bob", age: 35, salary: 3000 },
    { name: "Charlie", age: 28, salary: 2200 },
    { name: "David", age: 45, salary: 1500 },
    { name: "Eve", age: 32, salary: 4000 }
]

// // 1. Map function to reduce salaries by 200
// const reducedSalaries = employees.map(emp => ({
//     ...emp,
//     salary: emp.salary - 200
// }));

// console.log("Employees with reduced salaries:", reducedSalaries);

// // 2. Filter employees over 30
// const olderEmployees = employees.filter(emp => emp.age > 30);
// console.log("Employees over 30:", olderEmployees);

const olderEmployeeFunction = (employeeList, age) => {
    const olderEmployeeList = employeeList.filter(emp => emp.age > age); 
    return olderEmployeeList; 
}

console.log(olderEmployeeFunction(employees, 30));

// // 3. Foreach to get employees with salary > 2000
// const highPaidEmployees = [];
// employees.forEach(emp => {
//     if (emp.salary > 2000) {
//         highPaidEmployees.push(emp);
//     }
// });
// console.log("Employees with salary > 2000:", highPaidEmployees);

