--
-- File generated with SQLiteStudio v3.3.3 on jue. oct. 28 02:07:15 2021
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: agendaCita
CREATE TABLE agendaCita (idAgenda INTEGER PRIMARY KEY NOT NULL, idMedico INTEGER REFERENCES Medico (idMedico) MATCH SIMPLE NOT NULL, idPaciente INTEGER REFERENCES pacientes (idPaciente) MATCH SIMPLE NOT NULL, idCita INTEGER NOT NULL REFERENCES Cita (idCita) MATCH SIMPLE);

-- Table: Calificacion
CREATE TABLE Calificacion (idCalificacion INTEGER PRIMARY KEY NOT NULL, "Calificacion
" NOT NULL);

-- Table: Cita
CREATE TABLE Cita (idCita INTEGER PRIMARY KEY NOT NULL, horaInicial VARCHAR NOT NULL, horaTerminada VARCHAR NOT NULL, fecha VARCHAR NOT NULL);

-- Table: Consulta
CREATE TABLE Consulta (idConsulta INTEGER PRIMARY KEY NOT NULL, idCita INTEGER REFERENCES Cita (idCita) MATCH SIMPLE NOT NULL, idObsevacion INTEGER NOT NULL REFERENCES Observacion (idObservacion) MATCH SIMPLE, idCalificacion INTEGER REFERENCES Calificacion (idCalificacion) MATCH SIMPLE NOT NULL);

-- Table: Especialidad
CREATE TABLE Especialidad (idEspecialidad INTEGER PRIMARY KEY NOT NULL, Nombre VARCHAR NOT NULL, descripcion VARCHAR NOT NULL);

-- Table: historiaClinica
CREATE TABLE historiaClinica (idHistoriaClinica INTEGER PRIMARY KEY NOT NULL, idMedico INTEGER REFERENCES Medico (idMedico) MATCH SIMPLE NOT NULL, idPaciente INTEGER REFERENCES pacientes (idPaciente) MATCH SIMPLE NOT NULL, idConsulta INTEGER REFERENCES Consulta (idConsulta) MATCH SIMPLE);

-- Table: Medico
CREATE TABLE Medico (idMedico INTEGER PRIMARY KEY NOT NULL, IdEspecialidad INTEGER NOT NULL REFERENCES Especialidad ("idEspecialidad
") MATCH SIMPLE, IdTurno INTEGER NOT NULL REFERENCES turno (idTurno) MATCH SIMPLE, idCalificacion INTEGER NOT NULL REFERENCES Calificacion (idCalificacion) MATCH SIMPLE, tipoDocumento VARCHAR NOT NULL, nIden VARCHAR NOT NULL, nombres VARCHAR NOT NULL, apellidos VARCHAR NOT NULL, genero VARCHAR NOT NULL, ciudad VARCHAR NOT NULL, email VARCHAR NOT NULL, contraseña VARCHAR NOT NULL);

-- Table: Observacion
CREATE TABLE Observacion (idObservacion INTEGER PRIMARY KEY NOT NULL, descripcion VARCHAR NOT NULL);

-- Table: pacientes
CREATE TABLE pacientes (idPaciente INTEGER PRIMARY KEY NOT NULL, tipoDocumento VARCHAR NOT NULL, nIden VARCHAR NOT NULL, nombres VARCHAR NOT NULL, apellidos VARCHAR NOT NULL, genero VARCHAR NOT NULL, ciudad VARCHAR NOT NULL, email VARCHAR NOT NULL, contraseña VARCHAR NOT NULL);

-- Table: Root
CREATE TABLE Root (idRoot INTEGER PRIMARY KEY NOT NULL, email VARCHAR NOT NULL, contraseña VARCHAR NOT NULL);

-- Table: turno
CREATE TABLE turno (idTurno INTEGER PRIMARY KEY NOT NULL, descripcion NOT NULL, fechaTurno NOT NULL, estado NOT NULL);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
