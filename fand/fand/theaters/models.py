from django.db import models

from django.urls import reverse
#
# GENDER_CHOICES = (
#     ('male', 'Male'),
#     ('female', 'Female'),
# )

# class Category(models.Model):
#     name = models.CharField(max_length=100)
#
#     class Meta:
#         ordering = ('name',)
#
#     def __str__(self):
#         return self.name

class Theater(models.Model):
    addressOne = models.CharField(max_length=200)
    addressTwo = models.CharField(max_length=200, null=True)
    agePolicy = models.CharField(max_length=400, null=True)
    city = models.CharField(max_length=100)
    theaterName = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=20)
    zip = models.CharField(max_length=5)
    id = models.CharField(max_length=100, primary_key=True)
    # alpha_code = models.CharField(max_length=3, blank=True, null=True)
    # numeric_code = models.CharField(max_length=3, blank=True, null=True)
    lat = models.CharField(max_length=10, blank=True, null=True)
    lng = models.CharField(max_length=10, blank=True, null=True)

    # showtimes = models.ForeignKey(Showtimes, "CASCADE")
    # movies = models.ForeignKey(Movie, "CASCADE")

    # def __str__(self):
    #     return "{} {} - {} ({})".format(self.location.name, self.movies.title, self.showtimes)
#
    def __str__(self):
        return "{} - {}".format(self.theaterName, self.city)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    movid = models.CharField(max_length=100, primary_key=True, default=0)
    # gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    # dob = models.DateField()

    runtime = models.CharField(max_length=6)
    genres = models.CharField(max_length=120)
    # releaseDate = models.DateField(null=True)
    rating = models.CharField(max_length=6)
    poster = models.CharField(max_length=1000)

    theaters = models.ManyToManyField(Theater)
    # theaters = models.ForeignKey(Theater, "CASCADE")
    #this movie is playing at these theaters
    #one to many relationship
    class Meta:
        ordering = ('title',)

    def __str__(self):
        #return self.name
        return "{}".format(self.title,)

class Showtime(models.Model):
    time = models.CharField(max_length=8)
    # ticketingDate = models.CharField(max_length=10)
    showid = models.CharField(max_length=100)
    # type = models.CharField(max_length=200)
    ticketingUrl = models.CharField(max_length=400)
    # movie = models.ManyToManyField(Movie)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, null=True)
    # theater = models.ForeignKey(Theater, on_delete=models.CASCADE, default="0")

    # movies = models.ForeignKey(Movie, "CASCADE")
    #"this movie plays at this many times"
    #one to many relationship
    class Meta:
        ordering = ('time',)

    def __str__(self):
        return "{} - Movie: {} - Theater: {}".format(self.time,self.movie,self.theater)

    # def to_json(self):
    #     return {
            # "name": self.name,
            # "alpha_code": self.alpha_code,
            # "numeric_code": self.numeric_code,
            # "lat": self.lat,
            # "lng": self.lng,
        # }



# class Theater(models.Model):
#     location = models.ForeignKey(Location, "CASCADE")
#     showtimes = models.ForeignKey(Showtimes, "CASCADE")
#     movies = models.ForeignKey(Movie, "CASCADE")
#
#     def __str__(self):
#         return "{} {} - {} ({})".format(self.location.name, self.movies.title, self.showtimes)
# #
#     def get_absolute_url(self):
#         from django.urls import reverse
#         return reverse('winners:winners-detail', args=[str(self.id)])
#
#     def to_json(self):
#         return {
#             "name": self.person.name,
#             "gender": self.person.gender,
#             "category": self.category.name,
#             "country": self.country.to_json(),
#             "year": self.year,
#         }
#
#     # def get_absolute_url(self):
#     #     return reverse('winners-detail',args={'person': self.person})



# class Winner(models.Model):
#     person = models.ForeignKey(Person, "CASCADE")
#     category = models.ForeignKey(Category, "CASCADE")
#     country = models.ForeignKey(Country, "CASCADE")
#     year = models.PositiveIntegerField()
#
#     def __str__(self):
#         return "{} {} - {} ({})".format(self.person.name, self.category, self.country, self.year)
#
#     def get_absolute_url(self):
#         from django.urls import reverse
#         return reverse('winners:winners-detail', args=[str(self.id)])
#
#     def to_json(self):
#         return {
#             "name": self.person.name,
#             "gender": self.person.gender,
#             "category": self.category.name,
#             "country": self.country.to_json(),
#             "year": self.year,
#         }
#
#     # def get_absolute_url(self):
#     #     return reverse('winners-detail',args={'person': self.person})
