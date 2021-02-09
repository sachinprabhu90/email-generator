import random
import pandas as pd


first_names = open('first_names.txt', 'r').read().split()
last_names = open('last_names.txt', 'r').read().split()
domains = open('domains.txt', 'r').read().split()

first_names_cleaned = [name.title() for name in first_names]
last_names_cleaned = [name.title() for name in last_names]

chars = ['_', '.', '-', '']
nums = ['', 1, 2, 3, 4, 5, 6, 7, 8, 9]
sites = ['gmail', 'live', 'yahoo', 'yandex', 'outlook', 'icloud', 'aol']


def gen_email():
    first_name = random.choice(first_names_cleaned).lower()
    rand_char = random.choice(chars)
    last_name = random.choice(last_names_cleaned).lower()
    rand_char2 = random.choice(chars)
    num = random.choice(nums)
    domain = random.choice(domains)
    site = random.choice(sites)

    email = f'{first_name}{rand_char}{last_name}{rand_char2}{num}@{site}.{domain}'

    return (first_name, last_name, email)


l = []
rows = 1000000
for row in range(rows):
    print(
        f'working on {row+1} out of {rows} ({round((row+1)/rows * 100, 2)}%)')
    l.append(gen_email())

df = pd.DataFrame(l)
df.columns = ['first_name', 'last_name', 'email']
df.to_csv('info.csv', index=False)
