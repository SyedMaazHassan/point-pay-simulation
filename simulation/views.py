from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from simulation.models import *

from django.template.defaulttags import register


@login_required
def redirect_now(request):
    return redirect("simulation:index")


@login_required
def submit_feedback(request):
    if request.method == "POST":
        email = request.POST.get("email")
        feedback = request.POST.get("feedback")
        if email and feedback:
            new_feedback = Feedback(email=email, feedback=feedback)
            new_feedback.save()
            messages.success(request, "Thanks for writing the feedback!")
    return redirect("simulation:index")


@register.filter
def get_item(dictionary, key):
    return dictionary.get(str(key))


# Create your views here.
@login_required
def index(request):
    print(request.session["user_course"])
    context = {"all_simulations": Simulation.objects.all()}
    return render(request, "home/simulation/index.html", context)


@login_required
def single_simulation(request, sim_id, step_id):
    simulation = Simulation.objects.filter(id=sim_id).first()
    current_step = Step.objects.filter(id=step_id, simulation=simulation).first()
    if not simulation or not current_step:
        return redirect("simulation:index")

    temp = request.session["user_course"].copy()
    str_sim_id = str(simulation.id)
    if str_sim_id in temp:
        if current_step.id not in temp[str_sim_id]:
            temp[str_sim_id].append(current_step.id)
    else:
        temp[str_sim_id] = [current_step.id]
    request.session["user_course"] = temp
    request.session.modified = True
    context = {
        "all_simulations": Simulation.objects.all(),
        "current_simulation": simulation,
        "current_step": current_step,
    }
    return render(request, "home/simulation/index.html", context)
