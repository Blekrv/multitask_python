import time
import tracemalloc
from faker import Faker
import csv
from faker.providers import BaseProvider
from multiprocessing import Pool


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
tracemalloc.start()
start = time.time()


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


def pool_handler():
    p = Pool()
    p.map(single_function, data)


if __name__ == '__main__':
    # file_clear()
    print(data)
    pool_handler()

    print('Current %d, Peak %d' % tracemalloc.get_traced_memory())
    print("All done!! {}".format(time.time() - start))
