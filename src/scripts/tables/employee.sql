CREATE TABLE IF NOT EXISTS employee(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fname VARCHAR(50) NOT NULL,
    lname VARCHAR(50) NOT NULL,
    nname VARCHAR(50) NOT NULL,
    birthday DATE DEFAULT CURRENT_DATE NOT NULL,
    gander VARCHAR(25) NOT NULL,
    governorate VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    st_or_ar VARCHAR(50) NOT NULL,
    home_no INT NOT NULL,
    floor VARCHAR(25) NOT NULL,
    university VARCHAR(50) NOT  NULL,
    certificate VARCHAR(50) NOT NULL,
    degree INT VARCHAR(50) NOT NULL,
    _work VARCHAR(50) NOT NULL,
    note VARCHAR(50),
    salary FLOAT(4,2) NOT NULL,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);