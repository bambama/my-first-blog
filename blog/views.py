from django.shortcuts import render
from .models import Post


def accueil(request):
	return render(request, "blog/accueil.html", {})
# Create your views here.

def liste_post(request):
	tous_les_postes = Post.objects.all()
	return render(request, "blog/accueil.html" , {"tous_les_postes":tous_les_postes})