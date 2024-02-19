import datetime
today = datetime.datetime.now()
day = datetime.timedelta(1)
print ("Yesterday:", today - day )
print("Today:", today)
print("Tomorrow:", today + day)
