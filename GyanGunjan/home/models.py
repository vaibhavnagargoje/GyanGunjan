from django.db import models


class Thematic(models.Model):
    name = models.CharField(max_length=200)
    headline = models.CharField(max_length=255)
    cover_picture = models.ImageField(upload_to="Thematic/")

    def __str__(self):
        return self.headline


# class Contribute(models.Model):

#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.EmailField(max_length=150)
#     subscribed = models.BooleanField(default=False)
#     message = models.TextField()

#     # File fields for different media types
#     photo = models.ImageField(upload_to='Contribute/Photos/', null=True, blank=True)
#     video = models.FileField(upload_to='Contribute/Videos/', null=True, blank=True)
#     pdf = models.FileField(upload_to='Contribute/PDFs/', null=True, blank=True)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name} ({self.contribute_type})"



class LandingPageData(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class LandingImages(models.Model):
    landing_page = models.ForeignKey(LandingPageData, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="landingImages/")

    def __str__(self):
        return f"Image for {self.landing_page.title}"
    





class Movie(models.Model):
    name = models.CharField(max_length=255, help_text="Enter the name of the movie")
    description = models.TextField(blank=True, help_text="A short description of the movie")
    youtube_link = models.URLField(
        blank=True, 
        null=True, 
        help_text="YouTube link for the movie. Leave blank if the movie is directly uploaded."
    )
    uploaded_movie = models.FileField(
        upload_to="movies/",
        blank=True,
        null=True,
        help_text="Upload the movie file directly if not available on YouTube."
    )


    def __str__(self):
        return self.name

    @property
    def is_youtube_movie(self):
        """Check if the movie is linked via YouTube."""
        return bool(self.youtube_link)

    @property
    def movie_source(self):
        """Determine the movie source (YouTube or uploaded file)."""
        if self.youtube_link:
            return self.youtube_link
        elif self.uploaded_movie:
            return self.uploaded_movie.url
        return None




class CoffeeTableBook(models.Model):
    coffee_table_book_name =  models.CharField(max_length=200)
    description = models.TextField()
    book_pdf = models.FileField(upload_to='Coffee Table Book/')




from django.db import models


class State(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Region(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="regions")
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.state.name})"






class Flipbook(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="flipbooks")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="flipbooks", null=True, blank=True)
    file = models.FileField(upload_to="flipbooks/")

    def __str__(self):
        return self.title


