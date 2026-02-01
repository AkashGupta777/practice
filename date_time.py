from datetime import datetime
time=datetime.now()
hour=time.hour
minute=time.minute 

total_minute=hour*60+minute

morning_start=4*60+30
morning_end=11*60+59
afternoon_start=12*60+00
afternoon_end=4*59+00
goodnight_start=5*60+00
goodnight_end=4*60+29


if morning_start<=total_minute<=morning_end:
 print("GOOD MORNING BODY")
elif afternoon_start<=total_minute<=afternoon_end:
 print("GOOD AFTERNOON")
else :
 print("GOOD NIGHT")