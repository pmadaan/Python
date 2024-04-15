from datetime import date, timedelta
from collections import defaultdict

outings = [
    {
        "trip": "India-Diwali",
        "begin": "2021-10-21",
        "end" : "2021-11-14"
    },
    {
        "trip": "Philly offsite",
        "begin": "2022-10-17",
        "end" : "2022-10-20"
    },
    {
        "trip": "India-Vaibhav ki shadi",
        "begin": "2022-11-20",
        "end" : "2023-02-06"
    },
    {
        "trip": "Phoenix/LA",
        "begin": "2023-10-07",
        "end" : "2023-10-21"
    },
    {
        "trip": "India-Ivan se milne",
        "begin": "2023-11-26",
        "end" : "2023-12-27"
    },
]

outings_map = dict()
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)+1):
        yield start_date + timedelta(n)

for trip in outings:
    begin = date.fromisoformat(trip["begin"])
    end = date.fromisoformat(trip["end"])

    for cal_date in daterange(begin, end):
        key = str(cal_date.year) + "-" + str(cal_date.month)
        if key in outings_map:
            outings_map[key] = (outings_map[key][0], cal_date.day)
        else:
            outings_map[key] = (cal_date.day, cal_date.day)

print("All outings parsed:")
print(outings_map)

landing = date.fromisoformat("2020-11-06")

total=0

curr_date = landing + timedelta(days=1)
while curr_date < date.today():
    key = str(curr_date.year) + "-" + str(curr_date.month)
    day = curr_date.day
    curr_date = curr_date + timedelta(days=1)
    if key in outings_map:
        outing_range_in_the_month = outings_map[key]
        if outing_range_in_the_month[0] <= day and day <= outing_range_in_the_month[1]:
            continue
    total += 1
    
print(f"Completed {total} days in Canada")