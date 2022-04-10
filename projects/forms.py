from .models import Projects, Rating,Reviews
from django.forms import ModelForm

class ProjectsForm(ModelForm):
    
    class Meta:
        model = Projects
        exclude = ('owner',)
        fields = '__all__'
        
class RatingForm(ModelForm):
    
    class Meta:
        model = Rating
        exclude = ('user','project')
        fields = '__all__'
        
class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        exclude = ('user','project','created')
        fields = '__all__'