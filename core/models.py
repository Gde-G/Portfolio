from django.db import models
from django.utils.text import slugify


class Technology(models.Model):
    type_choices = [
        ('frontend', 'frontend'),
        ('backend', 'backend'),
        ('database', 'database'),
        ('cloud', 'cloud')
    ]

    name = models.CharField(max_length=200, unique=True)
    logo = models.ImageField(upload_to='images/technologies')
    type_tech = models.CharField(max_length=10, choices=type_choices)

    def __str__(self):
        return self.name


class ThirdParty(models.Model):
    kind_choices = [
        ('API', 'API'),
        ('Library', 'Library'),
        ('Other', 'Other')
    ]
    name = models.CharField(max_length=100, unique=True)
    kind = models.CharField(max_length=25, choices=kind_choices)
    description = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=100, unique=True)
    testimonial = models.TextField(max_length=250)
    image = models.ImageField(upload_to='images/testimonials')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-update_at', '-created_at']


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(max_length=1000)

    logo = models.ImageField(upload_to='images/projects')
    db_diagram = models.ImageField(
        upload_to='images/projects/diagrams', null=True, blank=True)

    link = models.URLField(max_length=120)

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True)
    technologies = models.ManyToManyField(
        Technology, through='ProjectTechnology')
    third_parties = models.ManyToManyField(
        ThirdParty, through='ProjectThirdparty')

    slug = models.SlugField(max_length=170, blank=True, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-update_at', '-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProjectTechnology(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)

    def __str__(self):
        return self.project.name + ', ' + self.technology.name


class ProjectThirdparty(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    third_party = models.ForeignKey(ThirdParty, on_delete=models.CASCADE)

    def __str__(self):
        return self.project.name + ', ' + self.third_party.name


class Consult(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=120)
    msg = models.CharField(max_length=900)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-update_at', '-created_at']
