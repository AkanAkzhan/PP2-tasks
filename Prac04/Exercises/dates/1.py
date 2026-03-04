import datetime

today = datetime.datetime.now()
five_days = datetime.timedelta(days=5)

new_date = today - five_days

print("Today:", today)
print("5 days ago:", new_date)