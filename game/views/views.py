from django.http import HttpResponse

def index(request):
    line1 = '<h1>术士之战</h1>'
    line2 = '<img src="https://i.91danji.com/new_attachments/201511/04/10/2ppxsauzs.jpg" width=800>'
    return HttpResponse(line1 + line2)

