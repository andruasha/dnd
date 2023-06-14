from django.shortcuts import render
from home.forms import SummaryForm
from home.generator import convert
from home.models import Summary
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def index(request):
    currentUserId = request.user.id

    summaries = Summary.objects.filter(user=currentUserId)

    context = {
        'title': 'CVMaker',
        'summaries': summaries,
    }
    return render(request, 'home/index.html', context)


@login_required(login_url='users:login')
def home(request):
    if request.method == 'POST':

        title = request.POST['title']
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        number = request.POST['number']
        education = request.POST['education']
        experience = request.POST['experience']
        skills = request.POST['skills']
        languages = request.POST['languages']

        return convert(title, name, surname, email, number, education, experience, skills, languages, request)

    else:
        form = SummaryForm()
    context = {'form': form}
    return render(request, 'home/home.html', context)


def download(request, path):
    with open(path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="resume.pdf"'
        return response