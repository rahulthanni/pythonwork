fmovie=open("movies.txt")
movie_details=[movies.rstrip("\n").split(",") for movies in fmovie]
#print(movie_details)

# number of movies released in 2022
released_2022=[movie for movie in movie_details if movie[1]=="2022"]
print(released_2022)

# number malayalam movies
no_malyalam=[movie for movie in movie_details if movie[3]=="malayalam"]
print(no_malyalam)
print(f"Malayalam movies: {len(no_malyalam)}")
# theater released movies
theat_release=[movie for movie in movie_details if movie[4]=="theater"]
print(theat_release)
# list of movies whose rating > 5
high_rating=[movie for movie in movie_details if movie[2]>str(5)]
print(high_rating)
# {2022:,4,2021:6,2020:2}
release_year={}
for mov in movie_details:
    year=mov[1]
    if year in release_year:
        release_year[year]+=1
    else:
        release_year[year]=1

print(release_year)
# 2021

movie_out=max(release_year.items(),key=lambda ite:ite[1])
print(movie_out)