import datetime

import requests
from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseBadRequest, HttpResponse
from django.utils import timezone

from .models import *

ua = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36'}
NO_IMAGE_LINK = 'media/default/no_image.png'
HH_ENDPOINT = 'https://api.hh.ru/vacancies/'
last_fetch = timezone.now() - datetime.timedelta(days=333)
cache = []


# Create your views here.
def index(request):
	return render(request, 'app/index.html')


def profs(request):
	profession_list = Profession.objects.filter(is_visible=True).all().values_list('id', 'name', named=True)
	payload = {
		'profs': profession_list
	}
	return render(request, 'app/prof.html', payload)


def prof_overview(request, prof_id):
	if not (profession := Profession.objects.filter(id=prof_id).first()):
		return HttpResponseNotFound()
	prof_descriptions = profession.description_blocks.all().values_list('title', 'description', named=True)
	payload = {
		'prof': profession,
		'prof_descs': prof_descriptions
	}
	return render(request, 'app/prof_detail_overview.html', payload)


def prof_view_vostr(request, prof_id):
	if not (profession := Profession.objects.filter(id=prof_id).first()):
		return HttpResponseNotFound()
	year_diagram = YearDiagram.objects.filter(profession=profession).first()
	vacancies_diagram = VacanciesDiagram.objects.filter(profession=profession).first()
	if year_diagram:
		link = f'media/year_diagram/{year_diagram.id}.jpg'
		try:
			with open(link, 'wb') as file:
				file.write(year_diagram.image)
		except:
			link = NO_IMAGE_LINK
		year_diagram = {
			'title': year_diagram.diagram_title,
			'image': '/' + link
		}
	else:
		year_diagram = {
			'title': 'Диаграмма зарплат по годам не добавлена',
			'image': '/' + NO_IMAGE_LINK
		}
	if vacancies_diagram:
		link = f'media/vacancies_diagram/{vacancies_diagram.id}.jpg'
		try:
			with open(link, 'wb') as file:
				file.write(vacancies_diagram.image)
		except:
			link = NO_IMAGE_LINK
		vacancies_diagram = {
			'title': vacancies_diagram.diagram_title,
			'image': '/' + link
		}
	else:
		vacancies_diagram = {
			'title': 'Диаграмма количества вакансий по годам не добавлена',
			'image': '/' + NO_IMAGE_LINK
		}
	payload = {
		'prof': profession,
		'diag_1': year_diagram,
		'diag_2': vacancies_diagram,
	}
	return render(request, 'app/prof_detail_diagram.html', payload)


def prof_view_geo(request, prof_id):
	if not (profession := Profession.objects.filter(id=prof_id).first()):
		return HttpResponseNotFound()
	cities_diagram = CitiesDiagram.objects.filter(profession=profession).first()
	cities_vacancies_diagram = CitiesVacanciesDiagram.objects.filter(profession=profession).first()
	if cities_diagram:
		link = f'media/year_diagram/{cities_diagram.id}.jpg'
		try:
			with open(link, 'wb') as file:
				file.write(cities_diagram.image)
		except:
			link = NO_IMAGE_LINK
		cities_diagram = {
			'title': cities_diagram.diagram_title,
			'image': '/' + link
		}
	else:
		cities_diagram = {
			'title': 'Диаграмма зарплат по городам не добавлена',
			'image': '/' + NO_IMAGE_LINK
		}
	if cities_vacancies_diagram:
		link = f'media/vacancies_diagram/{cities_vacancies_diagram.id}.jpg'
		try:
			with open(link, 'wb') as file:
				file.write(cities_vacancies_diagram.image)
		except:
			link = NO_IMAGE_LINK
		cities_vacancies_diagram = {
			'title': cities_vacancies_diagram.diagram_title,
			'image': '/' + link
		}
	else:
		cities_vacancies_diagram = {
			'title': 'Диаграмма количества вакансий по городам не добавлена',
			'image': '/' + NO_IMAGE_LINK
		}
	payload = {
		'prof': profession,
		'diag_1': cities_diagram,
		'diag_2': cities_vacancies_diagram,
	}
	return render(request, 'app/prof_detail_diagram.html', payload)


def years_view(request):
	years = Year.objects.filter(is_visible=True).all().values_list('year', named=True)
	return render(request, 'app/years.html', {'years': years})


def skills_year_view(request, year):
	if not (year := Year.objects.filter(year=year).first()):
		return HttpResponseNotFound()
	year_skills = Skill.objects.filter(year=year).order_by('-weight').values_list('name', 'weight', named=True)
	return render(request, 'app/year_skills.html', {'year': year, 'skills': year_skills})


def last_vacancies(request):
	global cache, last_fetch
	if last_fetch > timezone.now() - datetime.timedelta(minutes=5):
		return render(request, 'app/last_vacancies.html', {'content': cache})
	response = requests.get(HH_ENDPOINT + '?per_page=10', headers=ua)
	if response.status_code != 200:
		return HttpResponseBadRequest()
	last_fetch = timezone.now()
	ids = [item.get('id') for item in response.json()['items']]
	cache = []
	for _id in ids:
		resp = requests.get(HH_ENDPOINT + f'{_id}/', headers=ua)
		if resp.status_code == 200:
			cache.append(resp.json())
	return render(request, 'app/last_vacancies.html', {'content': cache})
