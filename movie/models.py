from django.db import models


class Movie(models.Model):
    movieid = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=30)
    year = models.CharField(max_length=4)
    date = models.CharField(max_length=10)
    rate = models.IntegerField(default=0)
    poster = models.URLField(default='')
    plot = models.CharField(max_length=200)
    trailer = models.URLField(default='')

    def __str__(self):
        return self.movieid + '|' + self.title


class Actor(models.Model):
    actorid = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=30)
    photo = models.URLField()

    def __str__(self):
        return self.actorid + '|' + self.name


class Act(models.Model):
    movieid = models.ForeignKey('Movie', default=1)
    actorid = models.ForeignKey('Actor', default=1)

    def __str__(self):
        return self.actorid.actorid + '|' + self.movieid.movieid


class Favorite(models.Model):
    username = models.CharField(max_length=150)
    movieid = models.ForeignKey('Movie', default=1)

    def __str__(self):
        return self.username + '|' + self.movieid.movieid
