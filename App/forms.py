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
            'name':"",
            'description':'',
            'muscle':'',
            'image':'IMAGE',
        }

class AddPlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['name', 'description']
        widgets ={
            'name': forms.TextInput(attrs={'class': 'fields', 'placeholder': 'NAME'}),
            'descriptiom':forms.TextInput(attrs={'class': 'description', 'placeholder': 'DESCRIPTION'}),
        }
        lebels = {
            "name":"",
            "description":"",
        }

class AddToPlan(forms.ModelForm):
    class Meta:
        model = ExercisePlan
        fields = ['plan', 'day_name']
        widgets = {
            'plan': forms.Select(attrs={'class': 'select', 'placeholder': 'PLAN'}),
            'day_name': forms.Select(attrs={'class': 'select', 'placeholder': 'DAY'}),
        }
        label = {
            "plan":"",
            "day_name":""
        }


class AddPR(forms.ModelForm):
    class Meta:
        model = PR
        fields = ['reps', 'pr', 'weight']
        widgets = {
            'reps': forms.TextInput(attrs={'class': 'fields', 'placeholder': 'REPS'}),
            'weight': forms.TextInput(attrs={'class': 'fields', 'placeholder': 'WEIGHT'}),
            'pr': forms.Select(attrs={'class': 'select', 'placeholder': 'PR'}),

        }