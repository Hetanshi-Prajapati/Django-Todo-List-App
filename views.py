from django.shortcuts import render, redirect, get_object_or_404
# render → Used to render an HTML template with data.
# redirect → Redirects to another URL after a POST request.
# get_object_or_404 → Fetches an object from the database or returns a 404 error if it does not exist.
from .models import Task
from django.contrib import messages
# Task → Your database model for storing tasks.
#tasks = [] # no usage
def index(request):
    tasks = Task.objects.all() # Get all tasks from the database
    return render(request,"hello.html",{"tasks":tasks}) #Passes the tasks to hello.html for display.
def tasks_view(request):
    if request.method == "POST":
        if "toggle_id" in request.POST:
            task_id = request.POST["toggle_id"]#Gets the task_id from the form, it is dictionary, toogle_id is the key and value is "1" or "2"
            task = Task.objects.get(id=task_id)
            task.completed = not task.completed  # Toggle completion
            task.save()
            return redirect("tasks")
    
        elif "ntask" in request.POST and not "update_id" in request.POST and not "delete_id" in request.POST:
            ntask = request.POST.get("ntask")#name of input field#Gets task text using request.POST.get("ntask")#<input type="text" name="ntask" placeholder="Enter your Task..." required>
            #if ntask:
            Task.objects.create(title=ntask)  # Save to database
            #messages.success(request, "Task added successfully!")
            return redirect("tasks")
            #else:
            #    messages.error(request, "Task cannot be empty!")

        elif "update_id" in request.POST:
            task_id = int(request.POST.get("update_id"))#name of input field 
            task = get_object_or_404(Task, id=task_id)#to get the task from the database
            task.title = request.POST.get("task")  # Update task title #name of input field
            task.save()
            return redirect("tasks")

        elif "delete_id" in request.POST:
            task_id = int(request.POST.get("delete_id"))#Retrieves the task_id from the form
            task = get_object_or_404(Task, id=task_id)#to find the task
            task.delete()  # Delete from database
            return redirect("tasks")#show the updated task list


    # Fetch all tasks from the database (even after restart)
    tasks = Task.objects.all()  
    return render(request, "tasks.html", {"tasks": tasks})
