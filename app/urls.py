from django.urls import path

from .views import *

urlpatterns = [
	path('', index),
	path('professions/', profs),
	path('professions/<int:prof_id>/overview/', prof_overview),
	path('professions/<int:prof_id>/vostr/', prof_view_vostr),
	path('professions/<int:prof_id>/geo/', prof_view_geo),
	path('year/', years_view),
	path('year/<int:year>/', skills_year_view),
	path('last_vacancies/', last_vacancies)
]