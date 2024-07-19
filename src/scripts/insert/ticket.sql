INSERT INTO ticket(
    train_id,
    pnr_number,
    price
)
VALUES( (SELECT id FROM train WHERE name=?),?,? );