countries = {
    "CZ": "Česko",
    "SK": "Slovensko",
    "DE": "Německo",
    "AT": "Rakousko",
    "PL": "Polsko",
}

countries_name = {}
full_countries_length = {}

for key, value in countries.items():
    countries_name[value] = key
print(countries_name)

for key, value in countries.items():
    full_countries_length[key] = len(value)
print(full_countries_length)
