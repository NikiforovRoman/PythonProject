from django.urls import path

from .views import *

urlpatterns = [
	path('', index),
	path('professions/', profs),
	path('professions/<int:prof_id>/overview/', prof_overview),
	path('professions/<int:prof_id>/vostr/', prof_view_vostr),
	path('professions/<int:prof_id>/geo/', prof_view_geo),
	path('professions/<int:prof_id>/year/', years_view),
	path('professions/<int:prof_id>/year/<int:year>/', skills_year_view),
	path('professions/<int:prof_id>/csv/', download_csv),
	path('professions/<int:prof_id>/pdf/', download_pdf),
	path('last_vacancies/', last_vacancies)
]