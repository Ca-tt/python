# TODO: sort the music list by playing count

data = {
    'RadioHead': 156,
    'Kishore Kumar': 141,
    'The Black Keys': 35,
    'Neutral Milk Hotel': 94,
    'Beck': 88,
    'Travis Scott': 122,
    'Wilco': 111,
}


def find_top_artist(artist_list):
  top_artist = None
  max_plays = 0

  for artist in artist_list:
    if artist_list[artist] > max_plays:
      max_plays = artist_list[artist]
      top_artist = artist
  return [top_artist, max_plays]


def sort_top_artists(artist_list):
  sorted_music = {}
  
  for i in range(len(artist_list)):
    key = find_top_artist(artist_list)[0]
    value = find_top_artist(artist_list)[1]

    sorted_music[key] = value
    artist_list.pop(key)
  return sorted_music


result = sort_top_artists(data)

print(result)

for key in result:
  print(key, result[key])
