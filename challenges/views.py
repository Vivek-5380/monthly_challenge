from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect , Http404
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january" : "Eat No meat for entire month!",
    "february" : "Walk for atleast 20 mins everyday!",
    "march" : "Learn Django for atleast 20 mins everyday!",
    "april" : "Eat No meat for entire month!",
    "may" : "Walk for atleast 20 mins everyday!",
    "june" : "Learn Django for atleast 20 mins everyday!",
    "july" : "Eat No meat for entire month!",
    "august" : "Walk for atleast 20 mins everyday!",
    "september" : "Learn Django for atleast 20 mins everyday!",
    "october" : "Eat No meat for entire month!",
    "november" : "Walk for atleast 20 mins everyday!",
    "december" : None
}

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())
    
    # for month in months:
    #     month_path = reverse("month-challenge" , args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{month.capitalize()}</a></li>" 
    
    # response_data = f"<ul>{list_items}</ul>"
    
    # return HttpResponse(response_data)
    
    return render(request,"challenges/index.html" , {
        "months" : months ,
    })

def monthly_challenge_by_number(request , month):
    months = list(monthly_challenges.keys())
    
    if month > len(months) or month < 1:
        return HttpResponseNotFound("Invalid Month")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge" , args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request , month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = f"<h1>{challenge_text}</h1>"
        
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        
        return render(request,"challenges/challenge.html" , {
            "text" : challenge_text,
            "month" : month
        })
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404()
        
    
