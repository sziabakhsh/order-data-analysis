import pandas as pd
import random
from datetime import datetime, timedelta

recNo = 500
customers = ['Sam' , 'Mike', 'Jill' , 'John' , 'Sepi' , 'Ana', 'Sara']
cities = ['Vancouver' , 'Paris', 'Milan' , 'Rome', 'Belgerade' , 'Tehran', 'Dubai']

data = []

start_date = datetime(2024,1,1)
for i in range(1, recNo+1):
    customer = random.choice(customers)
    city = random.choice(cities)
    amount = random.randint(50, 1000)
    date = start_date + timedelta(days=random.randint(0, 364))
    date_str = date.strftime("%Y-%m-%d")
    data.append([i, customer, city, amount, date_str])

df = pd.DataFrame(data, columns=["order_id","customer","city","amount","date"])
df.to_csv("orders_500.csv", index=False)
print("orders_500.csv created with 500 records")
