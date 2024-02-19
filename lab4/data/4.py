from datetime import datetime
date1_str = input()
data1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
data2_str = input()
data2 = datetime.strptime(data2_str, "%Y-%m-%d %H:%M:%S")
seconds = abs((data1 - data2).total_seconds())
print(seconds)