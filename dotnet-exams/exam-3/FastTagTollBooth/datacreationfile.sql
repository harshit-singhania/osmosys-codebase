CREATE database FastTagDB; 
USE FastTagDB; 

CREATE TABLE IF NOT EXISTS FastTagVehicles (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    RegNumber VARCHAR(12) NOT NULL UNIQUE,
    FastTagSerial VARCHAR(10) NOT NULL UNIQUE,
    Balance DECIMAL(10,2) NOT NULL
);

-- Sample inserts
INSERT INTO FastTagVehicles (RegNumber, FastTagSerial, Balance) VALUES
('MH12AB1234', '1234567890', 500.00),
('KA05CD6789', '0987654321', 1000.00),
('DL8CAF1111', '1122334455', 200.00);

select * from FastTagVehicle; 

RENAME TABLE FastTagVehicles TO FastTagVehicle;
