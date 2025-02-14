class Mechanic {
    constructor(name, employeeNumber) {
        this.name = name;
        this.employeeNumber = employeeNumber;
        this.activeJobs = 0;
        this.serviceHistory = [];
    }
}

class Job {
    constructor(make, model, year, license, mechanic) {
        this.jobId = Job.generateJobId();
        this.make = make;
        this.model = model;
        this.year = year;
        this.license = license;
        this.jobDate = new Date();
        this.status = "UNDER_REPAIR";
        this.mechanicId = mechanic.employeeNumber;
    }

    static generateJobId() {
        return 'JOB' + Math.random().toString(36).substr(2, 9).toUpperCase();
    }
}

class GarageManagementSystem {
    constructor() {
        this.mechanics = new Map();
        this.jobs = new Map();
    }

    // Helper method to validate Indian vehicle license number
    validateLicenseNumber(license) {
        // Indian vehicle registration format: AA BB CC DDDD
        // AA: State code
        // BB: District code
        // CC: Series code
        // DDDD: Number
        const indianLicensePattern = /^[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}$/;
        return indianLicensePattern.test(license);
    }

    // Helper method to find available mechanic
    findAvailableMechanic() {
        let availableMechanic = null;
        let lowestJobCount = Infinity;

        for (const mechanic of this.mechanics.values()) {
            if (mechanic.activeJobs < lowestJobCount) {
                lowestJobCount = mechanic.activeJobs;
                availableMechanic = mechanic;
            }
        }

        return availableMechanic;
    }

    addMechanic(name, employeeNumber) {
        if (this.mechanics.has(employeeNumber)) {
            throw new Error('Mechanic with this employee number already exists');
        }
        this.mechanics.set(employeeNumber, new Mechanic(name, employeeNumber));
    }

    addJob(make, model, year, license) {
        // Validate year
        if (year < 2000) {
            throw new Error('Cannot service vehicles made before 2000');
        }

        // Validate license
        if (!this.validateLicenseNumber(license)) {
            throw new Error('Invalid Indian vehicle license number');
        }

        // Find available mechanic
        const mechanic = this.findAvailableMechanic();
        if (!mechanic) {
            throw new Error('No mechanics available');
        }

        // Create and store job
        const job = new Job(make, model, year, license, mechanic);
        this.jobs.set(job.jobId, job);
        
        // Update mechanic's status
        mechanic.activeJobs++;
        mechanic.serviceHistory.push(job.jobId);

        return job.jobId;
    }

    getNumberOfCars(searchString) {
        const [make, model, year] = searchString.split(' ');
        let count = 0;

        for (const job of this.jobs.values()) {
            if (job.make === make && 
                job.model === model && 
                job.year === parseInt(year)) {
                count++;
            }
        }

        return count;
    }

    getServicedCarsByMechanic(employeeNumber) {
        const mechanic = this.mechanics.get(employeeNumber);
        if (!mechanic) {
            throw new Error('Mechanic not found');
        }

        return mechanic.serviceHistory
            .slice(0, 5)
            .map(jobId => this.jobs.get(jobId));
    }

    getCarsBetweenDate(fromDate, toDate) {
        const from = new Date(fromDate);
        const to = new Date(toDate);

        return Array.from(this.jobs.values()).filter(job => {
            const jobDate = new Date(job.jobDate);
            return jobDate >= from && jobDate <= to;
        });
    }

    markAsReady(jobId) {
        const job = this.jobs.get(jobId);
        if (!job) {
            throw new Error('Job not found');
        }

        if (job.status === "UNDER_REPAIR") {
            job.status = "READY";
            const mechanic = this.mechanics.get(job.mechanicId);
            if (mechanic) {
                mechanic.activeJobs--;
            }
        }
    }
}

const garage = new GarageManagementSystem();

// Add mechanics
garage.addMechanic("John Doe", "EMP001");
garage.addMechanic("Jane Smith", "EMP002");
garage.addMechanic("Don Doe", "EMP003");

// Add a new job
let createdJobId;
try {
    createdJobId = garage.addJob("Maruti", "Alto", 2004, "MH12AB1234");
    console.log(`New job created with ID: ${createdJobId}`);
} catch (error) {
    console.error(error.message);
}

// add another job 
try {
    createdJobId = garage.addJob("BMW", "320", 2018, "MH12AB1236");
    console.log(`New job created with ID: ${createdJobId}`);
} catch (error) {
    console.error(error.message);
}

// add another job 
try {
    createdJobId = garage.addJob("Tesla", "Model S", 2022, "MH12AB1237");
    console.log(`New job created with ID: ${createdJobId}`);
} catch (error) {
    console.error(error.message);
}

// Get number of specific cars
const carCount = garage.getNumberOfCars("Maruti Alto 2004");
console.log(`Number of Maruti Alto 2004: ${carCount}`);

// Get cars between dates
const carsBetweenDates = garage.getCarsBetweenDate("2024-02-01", "2024-02-14");
console.log("Cars serviced between dates:", carsBetweenDates);

// service history of mechanic 1 
const mechanicHistory1 = garage.getServicedCarsByMechanic("EMP001");
console.log("Last 5 cars serviced by mechanic:", mechanicHistory1);

// service history of mechanic 2 
const mechanicHistory2 = garage.getServicedCarsByMechanic("EMP002");
console.log("Last 5 cars serviced by mechanic:", mechanicHistory2);

// service history of mechanic 3 
const mechanicHistory3 = garage.getServicedCarsByMechanic("EMP003");
console.log("Last 5 cars serviced by mechanic:", mechanicHistory3);

// Mark a job as ready using the stored jobId
if (createdJobId) {
    garage.markAsReady(createdJobId);
    console.log(`Job ${createdJobId} marked as ready`);
}