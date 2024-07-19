INSERT INTO report_solve(
    train_id,
    employee_id,
    company_id,
    title_solve,
    type_solve,
    description_solve,
    bidget
)
VALUES(
    (SELECT id FROM train WHERE name=?),
    (SELECT id FROM employee WHERE ? IN ("fname" || " " ||  "lname")),
    (SELECT id FROM company WHERE name=?)
    ,?,?,?,?);