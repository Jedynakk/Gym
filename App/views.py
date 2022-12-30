from django.shortcuts import render, redirect
from django.views import View

from App.forms import AddExerciseForm, AddPlanForm, AddToPlan, AddPR
from App.models import Exercise, Plan, DAYS, ExercisePlan, PR, CurrentPlan


class MainPageView(View):
    def get(self, request):
        id = CurrentPlan.objects.get()
        cplan = id.plan_id
        plan = Plan.objects.get(pk=cplan)
        exerciseplan = ExercisePlan.objects.filter(plan=plan).order_by('day_name')
        dayinplan = sorted(list(set(day.day_name for day in exerciseplan)))
        return render(request, 'main/main_page.html',
                      {'plan': plan, 'exerciseplan': exerciseplan, 'dayinplan': dayinplan, 'day_name': DAYS})


class AddExerciseView(View):
    def get(self, request):
        form = AddExerciseForm()
        return render(request, 'exercises/add_exercise.html', {'form': form})

    def post(self, request):
        form = AddExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')
        return render(request, 'exercises/add_exercise.html', {'form': form})


class ExerciseList(View):
    def get(self, request):
        exercises = Exercise.objects.all()
        return render(request, 'exercises/exercise_list.html', {'exercises': exercises})


class ExerciseView(View):
    def get(self, request, id):
        exercise = Exercise.objects.get(pk=id)
        return render(request, 'exercises/exercise_view.html', {'exercise': exercise})


class AddToPlanView(View):
    def get(self, request, id):
        form = AddToPlan()
        exe = Exercise.objects.get(pk=id)
        return render(request, 'exercises/add_to_plan.html', {'form': form, 'exe': exe})

    def post(self, request, id):
        exe = Exercise.objects.get(pk=id)
        form = AddToPlan(request.POST)
        if form.is_valid():
            e = form.save(commit=False)
            e.exercise = exe
            e.save()
            form.save()
            return redirect('main_page')
        return render(request, 'exercises/add_to_plan.html', {'form': form, 'exe': exe})


class AddPlanView(View):
    def get(self, request):
        form = AddPlanForm()
        return render(request, 'plan/add_new_plan.html', {'form': form})

    def post(self, request):
        form = AddPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')
        return render(request, 'plan/add_new_plan.html', {'form': form})


class PlanList(View):
    def get(self, request):
        plan = Plan.objects.all()
        return render(request, 'plan/plan_list.html', {'plan': plan})


class PlanView(View):
    def get(self, request, id):
        plan = Plan.objects.get(pk=id)
        exerciseplan = ExercisePlan.objects.filter(plan=plan).order_by('day_name')
        dayinplan = sorted(list(set(day.day_name for day in exerciseplan)))
        return render(request, 'plan/plan_view.html',
                      {'plan': plan, 'exerciseplan': exerciseplan, 'dayinplan': dayinplan, 'day_name': DAYS})

    def post(self, request, id):
        plan = Plan.objects.get(pk=id)
        current = CurrentPlan.objects.all()
        current.delete()
        CurrentPlan.objects.create(plan=plan)
        return redirect('main_page')


class AddPrView(View):
    def get(self, request, id):
        form = AddPR()
        exercise = Exercise.objects.get(pk=id)
        return render(request, 'exercises/new_pr.html', {'exercise': exercise, 'form': form})

    def post(self, request, id):
        exercise = Exercise.objects.get(pk=id)
        form = AddPR(request.POST)
        if form.is_valid():
            e = form.save(commit=False)
            e.exercise = exercise
            e.save()
            form.save()
            return redirect('main_page')
        return render(request, 'exercises/new_pr.html', {'exercise': exercise, 'form': form})


class PrsView(View):
    def get(self, request, id):
        exercise = Exercise.objects.get(pk=id)
        pr = PR.objects.filter(exercise_id=exercise.pk)
        return render(request, 'exercises/prs.html', {'exercise': exercise, 'pr': pr})
