weather = [
    {"district": "tvm", "temp": 30},
    {"district": "ktm", "temp": 28},
    {"district": "apy", "temp": 27},
    {"district": "idk", "temp": 18},
    {"district": "ekm", "temp": 31},
    {"district": "pta", "temp": 21},
    {"district": "tsr", "temp": 24},
    {"district": "kzd", "temp": 29},
    {"district": "pkd", "temp": 34},
    {"district": "mpm", "temp": 31},
    {"district": "tvm", "temp": 31},
    {"district": "ktm", "temp": 29},
    {"district": "apy", "temp": 26},
    {"district": "idk", "temp": 20},
    {"district": "ekm", "temp": 30},
    {"district": "pta", "temp": 22},
    {"district": "tsr", "temp": 27},
    {"district": "kzd", "temp": 28},
    {"district": "pkd", "temp": 30},
    {"district": "mpm", "temp": 29},

]
# out={"tvm":31,"ktm":29,}
out={}
for data in weather:
    district_name=data["district"]
    curr_temp=data["temp"]
    if district_name in out:
        old_temp=out[district_name]
        if curr_temp>old_temp:
            out[district_name]=curr_temp
    else:
        out[district_name]=curr_temp

print(out)
# find max tem district

maxtemp_weather = max(weather, key=lambda temp: temp["temp"])
print(maxtemp_weather)

# find min tem district
mintemp_weather = min(weather, key=lambda temp: temp["temp"])
print(mintemp_weather)
