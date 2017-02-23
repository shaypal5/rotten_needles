import omdb
import json, requests
import csv


def main():
    # res = omdb.request(t='True Grit')
    # print(res.text)
    #
    # movie = omdb.search('True Grit')
    # print(movie[0])
    #
    # url = "http://www.omdbapi.com/?t=scream"
    # response = requests.get(url)
    # python_dictionary_values = json.loads(response.text)
    #

    movies = {}

    entriesToKeep = ['Title', 'Director', 'Year', 'Genre', 'Country', 'imdbID', 'Rated', 'imdbVotes',
                     'imdbRating', 'Metascore', 'Runtime', 'imdbVotes', 'BoxOffice', 'tomatoFresh', 'tomatoMeter',
                     'tomatoRating']

    # baseurl = "http://omdbapi.com/?t="  # only submitting the title parameter
    # tomatoes = '&tomatoes=true'

    output = open('dataSet.csv', 'w')
    writer = csv.DictWriter(output, entriesToKeep, lineterminator='\n')
    writer.writeheader()
    with open("movies.txt", "r") as fin:
        counter = 0
        for line in fin:
            movieTitle = line.rstrip("\n")  # delete newline characters
            # response = requests.get(baseurl + movieTitle + tomatoes)
            response = omdb.request(t=movieTitle, tomatoes='true')
            if response.status_code == 200:
                try:
                    movies[movieTitle] = json.loads(response.text)
                    movies[movieTitle] = {key: movies[movieTitle][key] for key in entriesToKeep}
                    writer.writerow(movies[movieTitle])

                except:
                    pass
            else:
                raise ValueError("Bad request!")

            counter += 1
            print(counter, " ", movieTitle)

    output.close()


if __name__ == '__main__':
    main()
