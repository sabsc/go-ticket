import datetime
import json
import re

from django.core.management.base import BaseCommand, CommandError
from django.utils.encoding import smart_text
from fand.theaters.models import Movie, Showtime, Theater

# Here we are creating a custom management command to load our winner data into
# Django models.
# The Command class is loaded by Django at runtime and executed when the file
# that contains it is specified as the command to manage.py
# In our case this file is called `load_winners.py` so the command we will use
# to execute this file is `manage.py load_winners path/to/winners.json`
class Command(BaseCommand):
    help = 'Load winner data into the database'

    # add_arguments lets us specify arguments and options to read from the command
    # line when the command is executed.
    # We are going to add 1 argument- "json_file" which is a string (type=str)
    # representing the path to a json file containing our data to load.
    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    # The handle method is the main function of the command. This is the entry
    # point for our command and contains all our business logic.
    def handle(self, *args, **options):
        # Grab the path from our commandline arguments
        json_path = options['json_file']

        # We are going to write output to the screen as we process things so
        # the user has feedback the script is running.
        self.stdout.write(self.style.SUCCESS('Loading JSON from "{}"'.format(json_path)))

        data = json.load(open(json_path, encoding="utf-8"))

        # Track the total number of records
        total = len(data)

        # Let the user know we're running
        self.stdout.write(self.style.SUCCESS('Processing {} rows'.format(total)))

        # Create an array to hang on to anything skipped while processing
        skipped = []

        # json_pretty = json.dumps(data, sort_keys=True, indent=4)
        # self.stdout.write(json_pretty)

        # Loop over each row in the data with the enumerate function so we have
        # a row counter

        # for key, value in data.items():
        #     if key == 'theaters':
        #         for theater in value:
        #             for key2, val2 in theater.items():
        #                 # if key2 == 'geo':
        #                 #     json_pretty = json.dumps(val2, sort_keys=True, indent=4)
        #                 #     self.stdout.write(json_pretty)
        #                 if key2 == 'address1':
        #                     address1 = val2
        #                     self.stdout.write(address1)
        #                 if key2 == 'address2':
        #                     address2 = val2
        #                     # if address2 != "":
        #                     #     self.stdout.write(address2)
        #                 if key2 == 'agePolicy':
        #                     agePolicy = val2
        #                 if key2 == 'city':
        #                     city = val2
        #                 if key2 == 'name':
        #                     name = val2
        #                 if key2 == 'phone':
        #                     phone = val2
        #                 if key2 == 'id':
        #                     id = val2
        #                 if key2 == 'state':
        #                     state = val2
        #                 if key2 == 'zip':
        #                     zip = val2
        #                 if key2 == 'geo':
        #                     for geo in val2:
        #                         for key3, val3 in geo.items():
        #                             if key3 == 'latitude':
        #                                 lat = val3
        #                             if key3 == 'longitude':
        #                                 lng = val3
        #                         self.stdout.write(lat)
        #         self.stdout.write("end of loop")

        for i, row in enumerate(data):
            id = row['id']
            addressOne = row['address1']
            addressTwo = row['address2']
            agePolicy = row['agePolicy']
            city = row['city']
            theaterName = row['name']
            phone = row['phone']
            state = row['state']
            zip = row['zip']

            geos = row.get('geo')
            lat = str(geos['latitude'])
            #self.stdout.write(lat)
            lng = geos.get('longitude')

            if not id or not addressOne or not city or not theaterName or not state or not zip or not lat or not lng:
                skipped.append(row)
                continue

            theater_instance, _ = Theater.objects.get_or_create(
                id = id,
                addressOne = addressOne,
                addressTwo = addressTwo,
                agePolicy = agePolicy,
                city = city,
                theaterName = theaterName,
                phone = phone,
                state = state,
                zip = zip,
                lat = lat,
                lng = lng,
            )

            # theater.save()

            movies = row.get('movies')
            # title = movies[0]['title']
            try:
                for m, movie in enumerate(movies):
                    title = movies[m]['title']
                    movid = movies[m]['id']
                    runtime = movies[m]['runtime']
                    genre = movies[m]['genres']
                    # releaseDate = movies[m]['releaseDate'][:10]
                    rating = movies[m]['rating']
                    # posters = movies.get('poster')
                    # for p, poster in enumerate(posters):
                    poster = movies[m]['poster']['size']['full']
                    # self.stdout.write(poster)
                    movie_instance, _ = Movie.objects.get_or_create(
                        title=title,
                        movid=movid,
                        runtime=runtime,
                        genres=genre,
                        # releaseDate=releaseDate,
                        rating=rating,
                        poster=poster,
                        # theaters=theater
                        # gender=row['gender'],
                        # dob=datetime.datetime.fromtimestamp(row['date_of_birth'] / 1000),
                    )
                    movie_instance.theaters.add(theater_instance)
                    #theater_instance.movie_set.add(movie_instance)

                    variants = movie.get('variants')
                    if variants:
                        for v, variant in enumerate(variants):
                            amenityGroups = variant.get('amenityGroups')
                            if amenityGroups:
                                for a, amenity in enumerate(amenityGroups):
                                    showtimes = amenity.get('showtimes')
                                    if showtimes:
                                        for s, showtime in enumerate(showtimes):
                                            showtime_instance, _ = Showtime.objects.get_or_create(
                                                # movie = movie_instance,
                                                # theater = theater_instance,
                                                time = showtime['date'],
                                                ticketingUrl = showtime['ticketingUrl'],
                                                showid = showtime['id'],
                                                # ticketingDate = showtime['ticketingDate'][:10]
                                            )

                                            showtime_instance.movie=movie_instance
                                            showtime_instance.theater=theater_instance
                                            showtime_instance.save()
                                            # movie_instance.showtime_set.add(showtime_instance)
            except:
                skipped.append(row)
                continue
            # json_pretty = json.dumps(lat, sort_keys=True, indent=4)
            # self.stdout.write(json_pretty)
            # for g, geo in enumerate(geos):
            #     lat = geos.get('latitude')
            #     lng = geos.get('longitude')
            #     self.stdout.write(lng)
            #     self.stdout.flush()
            #make list/array/[] thing with row['theaters']
            #grab the key/value pair if the key is 'theaters'
            # for t, theater in enumerate(theaters):
            #     self.stdout.write(theaters['name'])
                #grab wat u need
                #throw into theater oject


                # movies = theater['movies']
                #
                # for m, movie in enumerate(movies)

                # .get('name of json key') is safe because no error if null/does not exist
                # if theaters dont have movies they wont have movies key
            # Ensure we have a country, category, and gender as these are all required
            self.stdout.write("processed 1 theater")
            continue



            # isLoggedIn
            # noShowtimesRedirect
            # pagination
            # printerFriendlyUrl
            # theaters
            #     geo
            #         latitude
            #         longitude
            #     movies
            #         bunch of movie specific info
            #         Showtimes
            #             showtime specific info

            # theaters = row['theaters']
            #make list/array/[] thing with row['theaters']
            #grab the key/value pair if the key is 'theaters'
            #for t, theater in enumerate(theaters):
                #grab wat u need
                #throw into theater object


                # movies = theater['movies']
                # for m, movie in enumerate(movies)

                # .get('name of json key') is safe because no error if null/does not exist
                # if theaters dont have movies they wont have movies key
            # Ensure we have a country, category, and gender as these are all required
            country_name = row['country']
            category_name = row['category']
            gender = row['gender']

            # If we don't have this data add the row to the skipped list and
            # continue to the next item in the for loop
            if not country_name or not category_name or not gender:
                skipped.append(row)
                continue

            # Here we will create the objects that a winning record relies on.
            # We use the get_or_create method to avoid creating duplicaates
            # https://docs.djangoproject.com/en/2.0/ref/models/querysets/#get-or-create
            # This lets us create a new category object called "Physics" the first
            # time we see it but otherwise return the already existing category object
            # from the database and use it.
            # This is the same for country and person but note that we have to
            # specify all the fields for the person object.
            id, _ = Theater.objects.get_or_create(name=id)
            category, _ = Category.objects.get_or_create(name=category_name)
            person, _ = Person.objects.get_or_create(
                name=row['name'],
                gender=row['gender'],
                dob=datetime.datetime.fromtimestamp(row['date_of_birth'] / 1000),
            )

            # Now that we have created our dependencies we can create a winner
            # record which ties all the objects together along with the year
            # that the award was won.
            w = Winner.objects.get_or_create(
                person=person,
                country=country,
                category=category,
                year=row['year'],
            )

            # Now we tell the user which object count we just updated.
            # By using the line ending `\r` (return) we return to the begginging
            # of the line and start writing again. This writes over the same line
            # and gives the illusion of the count incrementing without cluttering
            # the screens output.
            self.stdout.write(self.style.SUCCESS('Processed {}/{}'.format(i + 1, total)), ending='\r')
            # We call flush to force the output to be written
            self.stdout.flush()

        # If we have any skipped rows write them out as json.
        # Then the user can manually evaluate / edit the json and reload it once
        # it has been fixed with `manage.py load_winners skipped.json`
        if skipped:
            self.stdout.write(self.style.WARNING("Skipped {} records".format(len(skipped))))
            with open('skipped.json', 'w') as fh:
                json.dump(skipped, fh)
