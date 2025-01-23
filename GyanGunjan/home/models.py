from django.db import models

# Model 1: Landing Page Sections (Iks Gyan Gunjan, 100 Regions, Jeevan Darshan)
class LandingPageSection(models.Model):
    SECTION_CHOICES = [
        ('hero1', 'Iks Gyan Gunjan'),
        ('hero2', '100 Regions'),
        ('hero3', 'Jeevan Darshan'),
    ]

    section_type = models.CharField(
        max_length=10,
        choices=SECTION_CHOICES,
        unique=True,
        help_text="Select the section type (e.g., Iks Gyan Gunjan)"
    )
    title = models.CharField(
        max_length=200,
        help_text="Main heading for the section"
    )
    short_description = models.TextField(
        help_text="Brief summary (1-2 sentences)"
    )
    long_description = models.TextField(
        help_text="Detailed description for the section"
    )
    additional_text = models.TextField(
        blank=True,
        help_text="Extra content (e.g., paragraph for Jeevan Darshan)"
    )

    class Meta:
        verbose_name = "Landing Page Section"
        verbose_name_plural = "Landing Page Sections"

    def __str__(self):
        return f"{self.get_section_type_display()} Section"


# Model 2: Images for Landing Page Sections
class LandingImage(models.Model):
    section = models.ForeignKey(
        LandingPageSection,
        on_delete=models.CASCADE,
        related_name='images',
        help_text="Select the section this image belongs to"
    )
    image = models.ImageField(
        upload_to='landing_images/',
        help_text="Upload image for the section"
    )
    caption = models.CharField(
        max_length=200,
        blank=True,
        help_text="Optional image caption"
    )

    class Meta:
        verbose_name = "Section Image"
        verbose_name_plural = "Section Images"

    def __str__(self):
        return f"Image for {self.section.get_section_type_display()}"





#jeevan darshan models 
class JeevanDarshanSection(models.Model):
    section_title = models.CharField(max_length=200, help_text="Main title of the section")
    section_description = models.TextField(help_text="Main description of the section")

    class Meta:
        verbose_name = "Jeevan Darshan Section"
        verbose_name_plural = "Jeevan Darshan Section"

    def __str__(self):
        return self.section_title

class JeevanDarshanImage(models.Model):
    section = models.ForeignKey(
        JeevanDarshanSection,
        on_delete=models.CASCADE,
        related_name='images',
        help_text="Associated Jeevan Darshan section"
    )
    image = models.ImageField(upload_to='jeevan_darshan/')
    image_title = models.CharField(max_length=200, help_text="Title for this image")
    image_description = models.TextField(help_text="Description for this image")

    class Meta:
        verbose_name = "Jeevan Darshan Image"
        verbose_name_plural = "Jeevan Darshan Images"

    def __str__(self):
        return f"{self.section.section_title} - {self.image_title}"
    




class Thematic(models.Model):
    name = models.CharField(max_length=200)
    headline = models.CharField(max_length=255)
    cover_picture = models.ImageField(upload_to="Thematic/")

    def __str__(self):
        return self.headline



class Movie(models.Model):
    name = models.CharField(max_length=255, help_text="Enter the name of the movie")
    description = models.TextField(blank=True, help_text="A short description of the movie")
    is_landing_movie = models.BooleanField(default=False, help_text="Check if this movie is for the landing page")
    is_recommended = models.BooleanField(default=False, help_text="Check if this movie is recommended")
    is_short_film = models.BooleanField(default=False, help_text="Check if this movie is a short film")
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
    movie_thumbnail = models.ImageField(
        upload_to="movie_thumbnails/",
        blank=True,
        null=True,
        help_text="Thumbnail for the movie"
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




from django.db import models

class CoffeeTableBook(models.Model):
    coffee_table_book_name = models.CharField(max_length=200)
    description = models.TextField()
    book_pdf = models.FileField(upload_to='Coffee Table Book/')
    cover_image = models.ImageField(upload_to='Coffee Table Book/Covers/', blank=True, null=True)

    def __str__(self):
        return self.coffee_table_book_name


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









# about project model class

class AboutProject(models.Model):
    title = models.CharField(max_length=200)
    tag = models.CharField(max_length=100)
    description_left = models.TextField()
    description_right = models.TextField()
    logo_image = models.ImageField(upload_to="about_project/")

from django.db import models

class AboutProject(models.Model):
    title = models.CharField(max_length=200)
    tag = models.CharField(max_length=100, blank=True, null=True)
    description_left = models.TextField()
    description_right = models.TextField()
    logo_image = models.ImageField(upload_to="about_project/")

    def __str__(self):
        return self.title

class AboutProjectImage(models.Model):
    about_project = models.ForeignKey(AboutProject, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="about_project/images/")
    alt_text = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.about_project.title}"