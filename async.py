import time
import tracemalloc
from faker import Faker
import csv
from faker.providers import BaseProvider
import asyncio
import itertools


class Login(BaseProvider):
    def login(self):
        return 'Unknown login'


data = []
for i in range(10000):
    fake = Faker()
    fake.add_provider(Login)
    temp = {'name': fake.name(), 'login': fake.login(
    ), 'password': fake.password(), 'address': fake.address()}
    data.append(temp)
print(data)


loop = asyncio.get_event_loop()


async def file_clear():
    clear = {}
    header = ['password', 'login', 'address', 'name']
    with open('data.csv', 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writerow(clear)
    file.close()


async def single_function(obj):
    header = ['password', 'login', 'address', 'name']
    with open('data.csv', 'a', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerow(obj)

    file.close()


tracemalloc.start()
start = time.time()


class Login(BaseProvider):
    def login(self):
        return 'Unknown login'


file_clear()
responses = itertools.starmap(single_function, data)
loop.run_until_complete(asyncio.gather(*responses))
loop.close()
# for item in range(10000):
#     fake = Faker()
#     fake.add_provider(Login)
#     temp = {'name': fake.name(), 'login': fake.login(
#     ), 'password': fake.password(), 'address': fake.address()}
#     single_function(temp)

print('Current %d, Peak %d' % tracemalloc.get_traced_memory())
print("All done!! {}".format(time.time() - start))
