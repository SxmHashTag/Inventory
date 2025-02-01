from django.db import models

class Case(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=100)
    hovj = models.CharField(max_length=255)  
    team = models.CharField(max_length=255)  

    def __str__(self):
        return f"{self.name} ({self.number})"


class Evidence(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='evidences')
    description = models.TextField()
    collected_on = models.DateField()
    added_by = models.CharField(max_length=255)

    def __str__(self):
        return self.description
