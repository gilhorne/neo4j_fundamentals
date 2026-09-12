from driver_instance import driver
from neo4j.time import DateTime, Duration
from datetime import timezone, timedelta

# --- WRITING TEMPORAL TYPES ---
driver.execute_query("""
CREATE (e:Event {
startsAt: $datetime,
createdAt: datetime($dtstring),
updatedAt: datetime()
})
""",

    datetime = DateTime(
        2024, 5, 15, 14, 30, 0,
        tzinfo = timezone(timedelta(hours=2))
    ),
    dtstring = "2024-05-15T14:30:00+02:00" #ISO 8601 format string
)

# --- READING TEMPORAL TYPES ---
# querying returning temporal types

records, summary, keys = driver.execute_query("""
RETURN date() AS date,
time() AS time, 
datetime() AS datetime,
toString(datetime()) AS asString
"""
)

#Access the first record 
for record in records:
    #automtic conversion to python driver types
    date = record["date"]
    time = record["time"]
    datetime = record["datetime"]
    as_string = record["asString"]

# --- WORKING WITH DURATIONS ---
starts_at = DateTime.now()
event_length = duration(hours=1, minutes=30)
end_at = starts_at + event_length

driver.execute_query("""
CREATE (e:Event {
    startsAt: $StartsAt, 
    endsAt: $endsAt,
    duration: $eventLength,
    interval: Duration("P30M")
})
""",
    startsAt = starts_at,
    endsAt = ends_at,
    eventLength = event_length
    )

#duration.between calculate the duration between two date or time objects

