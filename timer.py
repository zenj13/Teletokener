import datetime

# Example timestamp in milliseconds
timestamp_ms = 1656240000  # Replace with your timestamp in milliseconds

# Convert milliseconds to a datetime object
#dt = datetime.datetime(1970, 1, 1) + datetime.timedelta(milliseconds=timestamp_ms)
exp_epoch = utc_timestamp = datetime.datetime.now().timestamp()
print(f"utc: {exp_epoch}")
dt_ep = dt_exp = datetime.datetime.fromtimestamp(exp_epoch)
# Print the datetime object
print(dt_ep)