from datetime import datetime, timedelta


users = [{'name': 'Any', 'birthday': datetime(year=2000, month=3, day=1).date()},
          {'name': 'An', 'birthday': datetime(year=2011, month=3, day=2).date()},
          {'name': 'Go', 'birthday': datetime(year=2021, month=3, day=3).date()},
          {'name': 'Igor', 'birthday': datetime(year=2001, month=2, day=27).date()},
          {'name': 'Daniel', 'birthday': datetime(year=2021, month=2, day=28).date()},
          {'name': 'Ja', 'birthday': datetime(year=2021, month=3, day=1).date()},
          {'name': 'Kiril', 'birthday': datetime(year=2021, month=3, day=2).date()},
          {'name': 'Ty', 'birthday': datetime(year=2021, month=3, day=2).date()},
          {'name': 'My', 'birthday': datetime(year=2021, month=3, day=1).date()}]






d = datetime.now()

monday = []
tuesday = []
wednesday = []
thursday = []
friday = []
   

list_for_week = []

if d.weekday() == 1:
    s = (datetime.now() + timedelta(days = 4)).date()
    for i in range (7):
        next_week = (datetime.now() + timedelta(days = 4+i)).date()
        for user in users:
            if (next_week.month == user["birthday"].month and next_week.day == user["birthday"].day):     
                if next_week.weekday() == 1:
                    tuesday.append(user['name'])
                elif next_week.weekday() == 2:
                    wednesday.append(user['name'])
                elif next_week.weekday() == 3:
                    thursday.append(user['name'])
                elif next_week.weekday() == 4:
                    friday.append(user['name'])
                else:
                    monday.append(user['name'])
    
                #print(user['name'])
        #print(next_week)
print(', '.join(monday))
    
    

        
        
