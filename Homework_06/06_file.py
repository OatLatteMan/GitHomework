countries = {
    "CZ": "Česko",
    "SK": "Slovensko",
    "DE": "Německo",
    "AT": "Rakousko",
    "PL": "Polsko",
}

countries_name = {}
countries_length = {}

for key, value in countries.items():
    countries_name[value] = key

for key, value in countries.items():
    countries_length[key] = len(value)

print(countries_length)
print(countries_name)