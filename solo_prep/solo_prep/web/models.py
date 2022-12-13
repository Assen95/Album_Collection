from django.core import validators
from django.db import models
from solo_prep.web.validations import check_if_username_is_acceptable


class Profile(models.Model):
    MAX_USER_LEN = 15
    MIN_USER_LEN = 2

    username = models.CharField(
        max_length=MAX_USER_LEN,
        validators=(
            validators.MinLengthValidator(MIN_USER_LEN),
        ),
        null=False,
        blank=False,

    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.username


class Album(models.Model):
    MAX_LEN_ALBUM_NAME = 30
    MAX_LEN_ARTIST_NAME = 30
    MAX_GENRE_LEN = 30

    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = "Jazz Music"
    RNB_MUSIC = "R&B Music"
    ROCK_MUSIC = "Rock Music"
    COUNTRY_MUSIC = "Country Music"
    DANCE_MUSIC = "Dance Music"
    HIP_HOP_MUSIC = "Hip Hop Music"
    OTHER_MUSIC = "Other"

    MUSICS = (
        (POP_MUSIC, POP_MUSIC),
        (JAZZ_MUSIC, JAZZ_MUSIC),
        (RNB_MUSIC, RNB_MUSIC),
        (ROCK_MUSIC, ROCK_MUSIC),
        (COUNTRY_MUSIC, COUNTRY_MUSIC),
        (DANCE_MUSIC, DANCE_MUSIC),
        (HIP_HOP_MUSIC, HIP_HOP_MUSIC),
        (OTHER_MUSIC, OTHER_MUSIC),
    )

    album_name = models.CharField(
        max_length=MAX_LEN_ALBUM_NAME,
        null=False,
        blank=False,
        verbose_name='Album Name'
    )
    artist = models.CharField(
        max_length=MAX_LEN_ARTIST_NAME,
        null=False,
        blank=False,
    )
    genre = models.CharField(
        max_length=MAX_GENRE_LEN,
        choices=MUSICS,
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL'
    )
    price = models.FloatField(
        validators=(
            validators.MinValueValidator(0.0),
        ),
    )
