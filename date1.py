from datetime import datetime, timedelta
# просто проверка даты и даты через 5 дней
now = datetime.now()
print(now)

future = now + timedelta(days=5)
print(future)
