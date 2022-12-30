from django import forms

from App.models import Exercise, Plan, ExercisePlan, PR


class AddExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'description', 'muscle', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'fields', 'placeholder': 'NAME'}),
            'description': forms.TextInput(attrs={'class': 'fields', 'placeholder': 'DESCRIPTION'}),
            'muscle': forms.Select(attrs={'class': 'select', 'placeholder': 'MUSCLE'}),
        }

        labels = {
            'name':"NAME",
            'description':'DESCRIPTION',
            'muscle':'MUSCLE',
            'image':'IMAGE',
        }

class AddPlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['name', 'description']


class AddToPlan(forms.ModelForm):
    class Meta:
        model = ExercisePlan
        fields = ['plan', 'day_name']
        widgets = {
            'plan': forms.Select,
            'day_name': forms.Select,
        }


class AddPR(forms.ModelForm):
    class Meta:
        model = PR
        fields = ['reps', 'pr', 'weight']
