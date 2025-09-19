# Songbook

# https://open.kattis.com/problems/sangbok

min, songs = map(int,input().split())
min*=60
song_sec = [*map(int,input().split())]
song_sec.sort()
time = 0
for song in song_sec:
    time += song
    if time>min:
        time -= song
        break
print(time)