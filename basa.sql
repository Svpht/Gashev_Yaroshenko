CREATE SCHEMA IF NOT EXISTS gashev_yaroshenko;
CREATE TABLE IF NOT EXISTS gashev_yaroshenko.taxi_cars (
    id_car INTEGER PRIMARY KEY,
    model TEXT NOT NULL,
    color TEXT NOT NULL,
    car_number TEXT UNIQUE NOT NULL,
    free_status BOOL NOT NULL
);
CREATE TABLE IF NOT EXISTS gashev_yaroshenko.driver (
    driver_id INTEGER PRIMARY KEY,
    rating_drive FLOAT NOT NULL
);
CREATE TABLE IF NOT EXISTS gashev_yaroshenko.passag (
    user_id INTEGER PRIMARY KEY,
    rating FLOAT NOT NULL
);


CREATE TABLE IF NOT EXISTS gashev_yaroshenko.orders (
    order_id INTEGER PRIMARY KEY,
    id_car INTEGER,
    user_id INTEGER,
    driver_id INTEGER,
    FOREIGN KEY (id_car) REFERENCES gashev_yaroshenko.taxi_cars(id_car),
    FOREIGN KEY (user_id) REFERENCES gashev_yaroshenko.passag(user_id),
    FOREIGN KEY (driver_id) REFERENCES gashev_yaroshenko.driver(driver_id),
    point_from TEXT NOT NULL,
    point_to TEXT NOT NULL,
    time_of_order TEXT NOT NULL,
    status TEXT NOT NULL
);
