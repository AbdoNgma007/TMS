CREATE TABLE IF NOT EXISTS ticket(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    train_id INT NOT NULL,
    pnr_number INT NOT NULL,
    price FLOAT(3, 2),
    FOREIGN KEY (train_id) REFERENCES train(id)
);
