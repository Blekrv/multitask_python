import time
import tracemalloc
from faker import Faker
import csv
from faker.providers import BaseProvider
import threading


def file_clear():
    clear = {}
    header = ['password', 'login', 'address', 'name']
    with open('data.csv', 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writerow(clear)
    file.close()


def single_function(obj):
    header = ['password', 'login', 'address', 'name']
    with open('data.csv', 'a', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writerow(obj)

    file.close()


tracemalloc.start()
start = time.time()


class Login(BaseProvider):
    def login(self):
        return 'Unknown login'


file_clear()
threads = []
for item in range(10000):
    fake = Faker()
    fake.add_provider(Login)
    temp = {'name': fake.name(), 'login': fake.login(
    ), 'password': fake.password(), 'address': fake.address()}
    thread = threading.Thread(target=single_function, args=(temp,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
print('Current %d, Peak %d' % tracemalloc.get_traced_memory())
print("All done!! {}".format(time.time() - start))
