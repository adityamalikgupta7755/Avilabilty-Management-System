from django.db import models

# Create your models here.
class emp_statustype(models. Model):
    status = models.CharField(max_length=120)

    def __str__(self):
        return self.status



class emp_shift(models. Model):
    shift_time = models.CharField(max_length=120)
    def __str__(self):
        return self.shift_time

class emp(models.Model):
    emp_id = models.CharField(max_length=120)
    emp_name = models.CharField(max_length=120)
    emp_shift = models.ForeignKey(emp_shift,  on_delete=models.CASCADE)
    def __str__(self):
        return self.emp_name

class emp_status(models. Model):
    emp = models.ForeignKey(emp, blank=True, null=True, on_delete=models.CASCADE)
    status = models.ForeignKey(emp_statustype, blank=True, null=True, on_delete=models.CASCADE)
    Date = models.DateField(auto_now=False, auto_now_add=False, blank=True,)
    def __str__(self):
        return self.emp.emp_name


class Csv(models.Model):
    file_name = models.FileField(upload_to='csvS')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)
    def __str__(self):
        return f" File id : {self.id}"


class record_delete(models. Model):
    day = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    Date = models.DateField(auto_now=False, auto_now_add=False, blank=True,null=True)
    deactivated = models.BooleanField(default=False)
    def __str__(self):
        return self.day


class record_created(models. Model):
    day = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    Date = models.DateField(auto_now=False, auto_now_add=False, blank=True,null=True)
    active = models.BooleanField(default=False)
    def __str__(self):
        return self.day