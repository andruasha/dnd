from django.http import HttpResponse
from home.models import Summary
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter
import re
import os


def convert(title, name, surname, email, number, education, experience, skills, languages, request):
    fontPath = os.path.join(os.path.dirname(__file__), 'fonts/arial.ttf')
    pdfmetrics.registerFont(TTFont('Arial', fontPath))

    resumePath = os.path.join(os.path.dirname(__file__), 'resumes')
    files = os.listdir(resumePath)

    digitNameFiles = []
    for file in files:
        fileName, fileExt = os.path.splitext(file)
        if fileName.isdigit():
            digitNameFiles.append(int(fileName))

    if digitNameFiles:
        maximum = max(digitNameFiles)
        nextFilename = str(int(maximum) + 1) + '.pdf'
        filePath = os.path.join(resumePath, nextFilename)
    else:
        filePath = os.path.join(os.path.dirname(__file__), 'resumes', '0.pdf')
    p = canvas.Canvas(filePath, pagesize=letter)

    p.setFont("Arial", 18)
    p.drawCentredString(300, 800, f"{surname} {name}")

    p.setFont("Arial", 14)
    p.drawCentredString(300, 780, email)
    p.drawCentredString(300, 760, number)

    p.setFont("Arial", 18)
    p.drawString(50, 680, "Образование")
    p.line(50, 670, 550, 670)
    p.setFont("Arial", 12)
    y = 650
    lines = re.split(r'[\r\n]+', education)
    for line in lines:
        p.drawString(50, y, "• " + line)
        y -= 15
    y = y - 20

    p.setFont("Arial", 18)
    p.drawString(50, y, "Опыт работы")
    p.line(50, y - 10, 550, y - 10)
    y = y - 30
    p.setFont("Arial", 12)
    lines = re.split(r'[\r\n]+', experience)
    for line in lines:
        p.drawString(50, y, "• " + line)
        y -= 15
    y = y - 20

    p.setFont("Arial", 18)
    p.drawString(50, y, "Профессиональные навыки")
    p.line(50, y - 10, 550, y - 10)
    y = y - 30
    p.setFont("Arial", 12)
    lines = re.split(r'[\r\n]+', skills)
    for line in lines:
        p.drawString(50, y, "• " + line)
        y -= 15
    y = y - 20

    p.setFont("Arial", 18)
    p.drawString(50, y, "Знание языков")
    p.line(50, y - 10, 550, y - 10)
    y = y - 30
    p.setFont("Arial", 12)
    lines = re.split(r'[\r\n]+', languages)
    for line in lines:
        p.drawString(50, y, "• " + line)
        y -= 15
    y = y - 20

    p.showPage()
    p.save()

    with open(filePath, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

    Summary.objects.create(name=title, path=filePath, user=request.user.id)

    return response
