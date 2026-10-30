PRAGMA foreign_keys = ON;
CREATE TABLE people (
    person_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    specialty TEXT NOT NULL
);
CREATE TABLE experiments (
    experiment_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    leader_id INTEGER NOT NULL REFERENCES people(person_id),
    status TEXT NOT NULL CHECK(status IN ('completed','running','cancelled')),
    started_at TEXT NOT NULL,
    finished_at TEXT
);
CREATE TABLE participation (
    experiment_id INTEGER NOT NULL REFERENCES experiments(experiment_id),
    person_id INTEGER NOT NULL REFERENCES people(person_id),
    role TEXT NOT NULL,
    PRIMARY KEY(experiment_id, person_id)
);
CREATE TABLE measurements (
    measurement_id INTEGER PRIMARY KEY,
    experiment_id INTEGER NOT NULL REFERENCES experiments(experiment_id),
    metric TEXT NOT NULL,
    value REAL,
    unit TEXT NOT NULL,
    measured_at TEXT NOT NULL,
    quality TEXT NOT NULL CHECK(quality IN ('valid','suspect','missing'))
);
CREATE TABLE equipment (
    equipment_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    serial TEXT NOT NULL UNIQUE
);
CREATE TABLE inspections (
    inspection_id INTEGER PRIMARY KEY,
    equipment_id INTEGER NOT NULL REFERENCES equipment(equipment_id),
    inspected_at TEXT NOT NULL,
    condition TEXT NOT NULL CHECK(condition IN ('ok','broken','unknown'))
);
CREATE TABLE reports (
    report_id INTEGER PRIMARY KEY,
    experiment_id INTEGER NOT NULL REFERENCES experiments(experiment_id),
    version INTEGER NOT NULL,
    published_at TEXT NOT NULL,
    conclusion TEXT NOT NULL,
    UNIQUE(experiment_id, version)
);
