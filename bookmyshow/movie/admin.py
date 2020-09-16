from django.contrib import admin
from .models import Movie

from django import forms


class Movie_Form(forms.ModelForm):
    GENRE = (("ADVENTURE", "Adventure"),
    ("FAMILY", "Family"),
    ("FANTASY" , "Fantasy"),
    ("MUSICAL" , "Musical"),
    ("ACTION", "Action"),
    ("SciFi" , "Sci-Fi"),
    ("DRAMA" , "Drama"),
    ("WAR" , "War"),
    ("HORROR" , "Horror"),
    ("MYSTERY" , "Mystery"),
    ("THRILLER" , "Thriller"),
    ("ROMANCE" , "Romance"),
     ("ANIMATION" , "Animation"),
     ("CRIME" , "Crime"),
     ("COMEDY" , "Comedy"))

    genre = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=GENRE)


admin.site.register(Movie)
# Register your models here.
