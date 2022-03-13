from django.db import models
from django.utils import timezone

# Create your models here.

# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver


class Feedback(models.Model):
    feedback = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    datetime = models.DateTimeField(default=timezone.now)


class Simulation(models.Model):
    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)
    img = models.ImageField(upload_to="simulation")

    def get_all_steps(self):
        all_steps = Step.objects.filter(simulation=self)
        return all_steps

    def get_first_step(self):
        all_steps = Step.objects.filter(simulation=self)
        return all_steps.first()

    def __str__(self):
        return self.heading


class Step(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    previous = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="previous_sim",
        null=True,
        blank=True,
    )
    next = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="next_sim", null=True, blank=True
    )
    image = models.ImageField(upload_to="sim-pics", null=True, blank=True)
    video_id = models.CharField(max_length=255, null=True, blank=True)
    simulation = models.ForeignKey(
        Simulation,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return f"{self.simulation} / {self.name}"
