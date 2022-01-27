from django.db import models

# Create your models here.

class Question_Set(models.Model):
    section = models.CharField(max_length=250)

    def __str__(self):
        return self.section

class Question(models.Model):
    question_set = models.ForeignKey(Question_Set, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    correct_ans = models.CharField(max_length=250)
    explanation = models.TextField(max_length=500)

    def __str__(self):
        return self.text

class Options(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name='choices')
    option=models.CharField(max_length=250)
    '''op1=models.CharField(max_length=100)
    op2=models.CharField(max_length=100)
    op3=models.CharField(max_length=100)
    op4=models.CharField(max_length=100)'''

    def __str__(self):
        return self.option

