from django.shortcuts import render
from . import models
from django.http import HttpResponse

# Create your views here.
def home(req):
    return render(req,'base.html')

def select_category(req):
    return render(req,'select_category.html')

def textall_categories(req):
    catdata=models.Question_Set.objects.all()
    return render(req,"all_cat.html",{'data':catdata})

def imgall_categories(req):
    catdata=models.Question_Set.objects.all()
    return render(req,"imgall_cat.html",{'data':catdata})

def textcategory_questions(req,cat_id):
    category=models.Question_Set.objects.get(id=cat_id)
    question=models.Question.objects.filter(question_set=category).order_by('id').first()
    '''option = []
    for i in question:
        op = models.Options.objects.filter(question=i)
        option.append(op)

    #option= models.Options.objects.all()
    print(option)
    print(question)'''
    option=question.choices.all()

    return render(req,"category_questions.html",{'question':question,'category':category,'option':option})

def submit_ans(req,cat_id,quest_id):
    if req.method=="POST":
        

        category=models.Question_Set.objects.get(id=cat_id)
        question=models.Question.objects.filter(question_set=category,id__gt=quest_id).exclude(id=quest_id).order_by('id').first()
        #option=models.Options.objects.filter(option=question)
    
        #option=models.Options.objects.filter(option=question)
        option=question.choices.all()

        return render(req,"category_questions.html",{'question':question,'category':category,'option':option})
    else:
        return HttpResponse("method not allowed")

    
def submit_ans1(req,cat_id,quest_id):
    if req.method=="POST":
        

        category=models.Question_Set.objects.get(id=cat_id)
        question=models.Question.objects.filter(question_set=category,id__gt=quest_id).exclude(id=quest_id).order_by('id').first()
        #option=models.Options.objects.filter(option=question)
    
        #option=models.Options.objects.filter(option=question)
        option=question.choices.all()

        return render(req,"imgcategory_questions.html",{'question':question,'category':category,'option':option})
    else:
        return HttpResponse("method not allowed")

    

def imgcategory_questions(req,cat_id):
    category=models.Question_Set.objects.get(id=cat_id)
    question=models.Question.objects.filter(question_set=category).order_by('id').first()
    option=question.choices.all()

    return render(req,"imgcategory_questions.html",{'question':question,'category':category,'option':option})