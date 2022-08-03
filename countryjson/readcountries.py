import json

with open("countries.json",encoding="utf-8") as f:
    data=json.load(f)

def get_country_data(country_name):
    return [country for country in data if country["name"].lower().startswith(country_name)]

# print total number of country details
print(len(data))

# print languages of ukrane
lang_of_ukr=[info["languages"] for info in data if info["name"]=="Ukraine"]
print(f"languages of ukraine:{lang_of_ukr}")
# print currency of china
curr_chn=[info["currencies"] for info in data if info["name"].lower().startswith("china")]
curr_name=[detail.get("name") for detail in curr_chn[0]]
print(curr_name)
# print population of india
india_data=get_country_data("india")
print(india_data)
# print nigehbouring countries of australia
aus_data=get_country_data("australia")
aus_borders=aus_data[0].get("borders")
print(aus_borders)

india_data=get_country_data("india")
country_borders=india_data[0].get("borders")
sharing_borders=[country.get("name") for country in data if country["alpha3Code"] in country_borders]
print(sharing_borders)

populate_country=max(data,key=lambda d:d.get("population"))
print(populate_country.get("name"))

less_pop_country=min(data,key=lambda d:d.get("population"))
print(less_pop_country.get("name"))