from datetime import datetime, timedelta

x = datetime.now()
y = x + timedelta(seconds=100)
print((x - y).total_seconds())
