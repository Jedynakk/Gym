from django.db import models

PARTIE = (
    (0, 'PARTIA'),
    (1, 'PLECY'),
    (2, 'BARKI'),
    (3, 'KLATA'),
    (4, 'NOGI'),
    (5, 'POŚLADKI'),
    (6, 'TRICEPS'),
    (7, 'BICEPS'),
    (8, 'BRZUCH'),
    (9, 'CARDIO'),

)

DAYS = (
    (1, 'MONDAY'),
    (2, 'TUESDAY'),
    (3, 'WEDNESDAY'),
    (4, 'THURSDAY'),
    (5, 'FRIDAY'),
    (6, 'SATURDAY'),
    (7, 'SUNDAY'),

)


def __str__(self):
    return self.name


SI = (
    (1, 'KG'),
    (2, 'KM'),
)


class Exercise(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    muscle = models.IntegerField(choices=PARTIE, default=0)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name


class Plan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return self.name


class ExercisePlan(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    day_name = models.IntegerField(choices=DAYS, default=0)


class PR(models.Model):
    date = models.DateField(auto_now_add=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    pr = models.PositiveIntegerField(choices=SI, default=1)
    weight = models.PositiveIntegerField(default=0)
    reps = models.PositiveIntegerField(default=0)


class CurrentPlan(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
