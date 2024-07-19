CREATE TABLE IF NOT EXISTS train(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL,
    class VARCHAR(50) NOT NULL,
    source VARCHAR(50) NOT NULL,
    destination VARCHAR(50) NOT NULL,
    travel_time TIME NOT NULL,
    arrival_time TIME NOT NULL,
    journey_date DATE NOT NULL,
    departure_time TIME NOT NULL,
    day_availability VARCHAR(50) NOT NULL,
    available_seats INT NOT NULL,
    price FLOAT(3,2),
    active BOOLEAN DEFAULT true NOT NULL
);