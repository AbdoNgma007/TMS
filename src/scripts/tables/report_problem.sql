CREATE TABLE IF NOT EXISTS report_problem(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    train_id INT NOT NULL,
    employee_id INT NOT NULL,
    company_id INT NOT NULL,
    title_problem VARCHAR(50),
    type_problem VARCHAR(50),
    datetime_problem DATE DEFAULT CURRENT_DATE,
    description_problem TEXT(1500),
    bidget FLOAT(5, 2),
    FOREIGN KEY (train_id) REFERENCES train(id),
    FOREIGN KEY (employee_id) REFERENCES employee(id),
    FOREIGN KEY (company_id) REFERENCES company(id)
);