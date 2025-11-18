# Extend a list with more list items
# Sort the list in reverse order
# Iterate and print list

best_pictures = [
  '2019 - Parasite',
  '2018 - Green Book',
  '2017 - The Shape of Water',
  '2016 - Moonlight',
  '2015 - Spotlight',
  '2014 - Birdman',
  '2013 - 12 Years a Slave',
  '2012 - Argo',
  '2011 - The Artist',
]

best_pictures.extend([
  '2020 - Nomadland',
  '2021 - CODA',
  '2022 - Everything Everywhere All at Once',
  '2023 - Oppenheimer',
  '2024 - Pacific Rim'
])

best_pictures.sort(reverse=True)

for movies in best_pictures:
  print (movies)