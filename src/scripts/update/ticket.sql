UPDATE ticket t1 SET
    train_id=t2.id,
    pnr_number=%s,
    price=%s
INNER JOIN train t2 ON t1.train_id = t2.id
WHERE t2.name = "%s";
