site_names = open('domains_random.txt').read().split()

domains = [domain.split('.')[1] for domain in site_names]

domains = list(set(domains))

with open('domains.txt', 'w') as file:
    file.write('\n'.join(domains))
