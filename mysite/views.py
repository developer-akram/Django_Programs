from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def faq(request):
    return render(request, 'faq.html')

def contact(request):
    return render(request, 'contact.html')

def courses(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        name = f"{fname} {lname}"
        gender = request.POST['gender']
        course = request.POST.getlist('course')
        courses = ''
        for i in range(len(course)):
            if course[i] == '':
                continue
            if i == len(course) - 1:
                courses += course[i]
            else:
                courses += course[i] + ', '
        country = request.POST['country']
        state = request.POST.getlist('state')
        states = ''
        for i in range(len(state)):
            if state[i] == '':
                continue
            if i == len(state) - 1:
                states += state[i]
            else:
                states += state[i] + ', '
        message = request.POST['message']
        return render(request, 'courses.html',{'key':{'Name : ':name, 'Gender : ':gender, 'Selected Courses : ':courses, 'Country : ':country, 'State : ':states, 'Message : ':message}})
    return render(request, 'courses.html')
# Create your views here.
