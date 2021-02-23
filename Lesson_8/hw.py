from datetime import datetime, timedelta
import random
import string


def congratulate(users):

    d = datetime.now()

    monday = []
    tuesday = []
    wednesday = []
    thursday = []
    friday = []
    if d.weekday() == 5:
        for i in range (7):
            next_week = (d + timedelta(days = i)).date()
    else:
        for i in range (7):
            next_week = (d + timedelta(days = i + (5 - d.weekday()))).date()

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
    
        print(f"Monday: {', '.join(monday)}\nTuesday: {', '.join(tuesday)}\nWednesday: {', '.join(wednesday)}\nThursday: {', '.join(thursday)}\nFriday: {', '.join(friday)}\n")
    return 'done'

users = []
def random_users():
    start_date = datetime(year=1985, month=3, day=20).date()
    end_date = datetime(year=1985, month=2, day=20).date()
    interval_delta = start_date - end_date
    
    for _ in range(30): 
        days_delta = random.randint(0, interval_delta.days)
        birthday_value = end_date + timedelta(days = days_delta)
        name_value = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        dict_user = {'name':name_value, 'birthday': birthday_value}
        users.append(dict_user)
    return users

def main():
    random_users()
    congratulate(users)



if __name__ == "__main__":
    main()
        


        
        
