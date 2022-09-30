import time, datetime
import os

from driver import currentTime

print(currentTime().strftime('%m%d %H:%M'))


path = os.path.join(os.getcwd(), 'mobile')
app = path + '\\wehago1.apk'
print(app)
print(os.getcwd())

# 날짜 테스트
now = datetime.datetime.now()
now = now + datetime.timedelta(days = 1)
now = now.strftime('%d %#m월 %Y')

# //android.view.View[@content-desc="16 9월 2022"]

print(now)

# 날짜 테스트 2
day = (currentTime() + datetime.timedelta(days=10)).strftime('%#d')
print(day)


# 날짜 테스트 3
currentmonth = currentTime().strftime('%m')
month = (currentTime() + datetime.timedelta(days=3)).strftime('%m')
print(currentmonth)
print(month)
if month > currentmonth :
    print('!')

# 날짜 테스트4

date = currentTime().strftime('%Y.%m.%d')
print(date)