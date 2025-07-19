CREATE DATABASE [PlataformaReservas]

CREATE TABLE Espacio (
    id INT IDENTITY(1,1) PRIMARY KEY, -- Automatic ID generation
    nombre VARCHAR(255) NOT NULL UNIQUE, -- Ensures unique names for spaces
    capacidad INT NOT NULL,
    horario_disponible VARCHAR(255), -- Example: '08:00 - 17:00'
    tipo VARCHAR(50) NOT NULL CHECK (tipo IN ('Laboratorio', 'Sala de Estudio', 'Auditorio')) -- Ensures valid types
);
GO

-- Optional: Add a few sample records to test
INSERT INTO Espacio (nombre, capacidad, horario_disponible, tipo) VALUES
('Laboratorio 101', 30, '08:00 - 18:00', 'Laboratorio'),
('Sala de Estudio A', 15, '09:00 - 20:00', 'Sala de Estudio'),
('Auditorio Principal', 200, '07:00 - 22:00', 'Auditorio');
GO

SELECT * FROM Espacio; -- Verify the table and data