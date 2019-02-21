import csv

# I'm using mousehead's Song Lyrics dataset, you can get it from here:
# https://www.kaggle.com/mousehead/songlyrics/home

# change this so it points to where you downloaded your dataset...
dataPath = "D:\\Data\\songdata.csv"

# select the Artist you want...
artist = "ABBA"

# we can store the count of the songs here
songs = 0

# read the data, it's in csv format
with open(dataPath) as csvfile:
    # use the csv module to read the file
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')

    # iterate through the rows in the dataset
    for row in reader:
        # the first column is the artist name
        if row[0] == artist:
            # increase the count
            songs += 1

print("{} has {} songs in the dataset!".format(artist, songs))
