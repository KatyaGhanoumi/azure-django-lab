from django.shortcuts import render

def task_list(request):
    # Hardcoded data for now -- will come from DynamoDB in Part 4
    # This is the context dictionary passed to the template (step 5 of the request flow)
    tasks = [
        {'taskName': 'Write the lab report', 'status': 'In Progress'},
        {'taskName': 'Study for the exam', 'status': 'Pending'},
        {'taskName': 'Submit the assignment', 'status': 'Done'},
    ]
    context = {'tasks': tasks}
    return render(request, 'task_list.html', context)