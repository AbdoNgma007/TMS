SELECT ti.pnr_number, tr.name, tr.journey_date, tr.departure_time, tr.day_availability
FROM ticket ti
INNER JOIN train tr ON ti.train_id = tr.id
ORDER BY ti.id DESC;