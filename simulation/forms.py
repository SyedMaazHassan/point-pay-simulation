from django.forms import ModelForm
from simulation.models import *


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"
        exclude = ["datetime"]
