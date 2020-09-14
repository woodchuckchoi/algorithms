from datetime import datetime, timedelta

start   = datetime.strptime("19641010", "%Y%m%d")
end     = datetime.strptime("20200724", "%Y%m%d")
step    = timedelta(days=1)

while start <= end:
    day = bin(int(start.strftime("%Y%m%d"))).replace("0b", "")
    if day == day[::-1]:
        print(start.strftime("%Y%m%d"))
    start += step