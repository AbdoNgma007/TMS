INSERT INTO report_problem(
    train_id,
    employee_id,
    company_id,
    title_problem,
    type_problem,
    description_problem,
    bidget
)
VALUES(%s,%s,%s,%s,%s,%s,%s);