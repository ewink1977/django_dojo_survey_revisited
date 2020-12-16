from django.shortcuts import render, HttpResponse, redirect

def index(request):
    print('INDEX PAGE REQUESTED')
    return render(request, 'index.html')

def result(request):
    if request.method == "POST":
        print("POST REQUEST MADE TO RESULT")
        your_name = request.POST["your_name"]
        location = request.POST["location"]
        language = request.POST["language"]
        end = request.POST["end"]
        frameworks = request.POST.getlist("frameworks")
        comments = request.POST["comments"]
        context = {
            'name': your_name,
            'location': location,
            'language': language,
            'end': end,
            'frameworks': frameworks,
            'comments': comments,
        }
        return render(request, 'results.html', context)
    if request.method == "GET":
        print("GET REQUEST MADE TO RESULT. INVALID AND REDIRECTING.")
        redirect("/")

