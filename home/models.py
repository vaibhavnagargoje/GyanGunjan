from django.db import models
from ckeditor.fields import RichTextField

# Model 1: Landing Page Sections (Iks Gyan Gunjan, 100 Regions, Jeevan Darshan)
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
    short_description = RichTextField(
        help_text="Brief summary (1-2 sentences)"
    )
    long_description = RichTextField(
        help_text="Detailed description for the section"
    )
    additional_text = RichTextField(
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



# Jeevan Darshan Section
class JeevanDarshanSection(models.Model):
    title = models.CharField(max_length=200, help_text="Main title of the section")
    short_description = RichTextField(help_text="Short description for homepage display")
    left_description = RichTextField(help_text="Left side description for the philosophy")
    right_description = RichTextField(help_text="Right side description for the philosophy")

    related_coffee_table_book = models.ForeignKey(
        'CoffeeTableBook', on_delete=models.SET_NULL, null=True, blank=True, 
        related_name='jeevan_darshan_sections',
        help_text="Select a related Coffee Table Book"
    )
    related_thematic = models.ForeignKey(
        'Thematic', on_delete=models.SET_NULL, null=True, blank=True, 
        related_name='jeevan_darshan_sections',
        help_text="Select a related Thematic book"
    )

    class Meta:
        verbose_name = "Jeevan Darshan Section"
        verbose_name_plural = "Jeevan Darshan Sections"

    def __str__(self):
        return self.title


class JeevanDarshanImage(models.Model):
    section = models.ForeignKey(JeevanDarshanSection, on_delete=models.CASCADE, related_name='images', help_text="Associated Jeevan Darshan section")
    title = models.CharField(max_length=200, help_text="Title for the philosophy/image")
    short_description = RichTextField(help_text="Short description for homepage display")
    image = models.ImageField(
        upload_to='jeevan_darshan/', help_text="Image for the philosophy")

    class Meta:
        verbose_name = "Jeevan Darshan Image"
        verbose_name_plural = "Jeevan Darshan Images"
        ordering = ['id']

    def __str__(self):
        return self.title


class Thematic(models.Model):
    name = models.CharField(max_length=200)
    headline = models.CharField(max_length=255)
    cover_picture = models.ImageField(upload_to="Thematic/")
    book_pdf = models.FileField(upload_to='Thematic/',blank=True, null=True)


    def __str__(self):
        return self.headline


class CoffeeTableBook(models.Model):
    coffee_table_book_name = models.CharField(max_length=200)
    description = RichTextField()
    book_pdf = models.FileField(upload_to='Coffee Table Book/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='Coffee Table Book/Covers/', blank=True, null=True)

    def __str__(self):
        return self.coffee_table_book_name





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
    description = RichTextField()
    state = models.ForeignKey('State', on_delete=models.CASCADE, related_name="flipbooks")
    region = models.ForeignKey('Region', on_delete=models.CASCADE, related_name="flipbooks", null=True, blank=True)
    book_pdf = models.FileField(upload_to="flipbooks/", blank=True, null=True)
    cover_image = models.ImageField(upload_to="flipbooks/covers/", blank=True, null=True)

    def __str__(self):
        return self.title








# about project model class
class AboutProject(models.Model):
    title = models.CharField(max_length=200)
    tag = models.CharField(max_length=100, blank=True, null=True)
    description_left = RichTextField()
    description_right = RichTextField()
    logo_image = models.ImageField(upload_to="about_project/")
    first_discripton = RichTextField(blank=True, null=True)
    first_discripton_image = models.ImageField(upload_to="about_project/", blank=True, null=True)
    long_discripton = RichTextField(blank=True, null=True)
    second_description = RichTextField(blank=True, null=True)
    second_discripton_image = models.ImageField(upload_to="about_project/", blank=True, null=True)
    third_description = RichTextField(blank=True, null=True)
    third_discripton_image = models.ImageField(upload_to="about_project/", blank=True, null=True)
    fourth_description = RichTextField(blank=True, null=True)
    fourth_discripton_image = models.ImageField(upload_to="about_project/", blank=True, null=True)
    fifth_description = RichTextField(blank=True, null=True)
    fifth_discripton_image = models.ImageField(upload_to="about_project/", blank=True, null=True)
    sixth_description = RichTextField(blank=True, null=True)
    sixth_discripton_image = models.ImageField(upload_to="about_project/", blank=True, null=True)

    def __str__(self):
        return self.title

class AboutProjectImage(models.Model):
    about_project = models.ForeignKey(AboutProject, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="about_project/images/")
    alt_text = RichTextField(blank=True, null=True)

    def __str__(self):
        return f"Image for {self.about_project.title}"