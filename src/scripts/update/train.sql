UPDATE train SET
    name="%s",
    class="%s",
    source="%s",
    destination="%s",
    travel_time="%s",
    arrival_time="%s",
    journey_date="%s",
    departure_time="%s",
    day_availability="%s",
    available_seats=%s,
    active=%s
WHERE name="%s";

