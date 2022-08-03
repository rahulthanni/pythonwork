import functools
import random
import json
with open("songs.json")as f:
    data=json.load(f)
num_song=[song for song in data if song["album"]=="album1"]
print(len(num_song))

albu_song_count=list(filter(lambda song:song["album"]=="album1",data))
print(len(albu_song_count))

t_songs=functools.reduce(lambda s1,s2:s1 if s1["rating"]>s2["rating"] else s2,data)
print(t_songs)

sad_songs=[song for song in data if song["mode"]=="sad"]
print(random.sample(sad_songs,2))

total_albums=set([s["album"] for s in data])
print(len(total_albums))

sc={}
for song in data:
    album_name=song.get("album")
    if album_name in sc:
        sc[album_name]+=1
    else:
        sc[album_name]=1
print(sc)

print(max(sc.items(),key=lambda s:s[1]))