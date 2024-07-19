INSERT INTO report_problem(
    train_id,
    employee_id,
    company_id,
    title_problem,
    type_problem,
    description_problem,
    bidget
)
VALUES(
    (SELECT id FROM train WHERE name=?),
    (SELECT id FROM employee WHERE ? IN ("fname" || " " ||  "lname")),
    (SELECT id FROM company WHERE name=?)
    ,?,?,?,?);