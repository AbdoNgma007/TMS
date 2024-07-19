CREATE TABLE IF NOT EXISTS report_solve(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    train_id INT NOT NULL,
    employee_id INT NOT NULL,
    company_id INT NOT NULL,
    title_solve VARCHAR(50),
    type_solve VARCHAR(50),
    datetime_solve DATE DEFAULT CURRENT_DATE,
    description_solve TEXT,
    bidget FLOAT(5, 2),
    FOREIGN KEY (train_id) REFERENCES train(id),
    FOREIGN KEY (employee_id) REFERENCES employee(id),
    FOREIGN KEY (company_id) REFERENCES company(id)
);