from datetime import datetime

# start time
start_time: str = "2:13:57"
end_time: str = "11:46:38"

# convert time string to datetime
t1: datetime = datetime.strptime(start_time, "%H:%M:%S")
print("Start time:", t1.time())

t2: datetime = datetime.strptime(end_time, "%H:%M:%S")
print("End time:", t2.time())
print(t2.date())
print(t2)

# get difference
delta: datetime = t2 - t1

# time difference in seconds
sec: datetime = delta.total_seconds()
print(f"Time difference is {sec} seconds")

# time difference in minutes
min: datetime = sec / 60
print(f"Time difference is {min} minutes")

# time difference in hours
hours: datetime = sec / (60 * 60)
print(f"Time difference is {hours} hours")

# time difference in milliseconds
ms: datetime = delta.total_seconds() * 1000
print(f"Time difference is {ms} milliseconds")


# Timestamp
print("\n\n")
print(datetime.now())
print((datetime.now()).timestamp())