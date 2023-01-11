from django.contrib import admin
from .models import *


class DescriptionsInline(admin.TabularInline):
	model = ProfessionDescriptionBlock
	verbose_name = 'Описание'
	verbose_name_plural = 'Описания'

	extra = 0


class YearDiagramInline(admin.TabularInline):
	model = YearDiagram
	max_num = 1


class VacanciesDiagramInline(admin.TabularInline):
	model = VacanciesDiagram
	max_num = 1


class CitiesDiagramInline(admin.TabularInline):
	model = CitiesDiagram
	max_num = 1


class CitiesVacanciesDiagramInline(admin.TabularInline):
	model = CitiesVacanciesDiagram
	max_num = 1


class YearsInline(admin.TabularInline):
	model = Year
	max_num = 1
	show_change_link = True


class SkillsInline(admin.TabularInline):
	model = Skill
	extra = 1


# Register your models here.
@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'is_visible',)
	list_filter = ('is_visible',)
	list_display_links = ('id',)
	exclude = ('description_blocks',)
	inlines = (DescriptionsInline, YearDiagramInline, VacanciesDiagramInline,
	           CitiesDiagramInline, CitiesVacanciesDiagramInline, YearsInline)
	list_editable = ('name', 'is_visible')
	search_fields = ('id', 'name')
	search_help_text = 'Поиск по id или названию'


@admin.register(ProfessionDescriptionBlock)
class ProfessionDescriptionBlockAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'profession')
	list_editable = ('title', )
	list_select_related = ('profession', )
	search_fields = ('id', 'title', 'profession__name', 'profession__id')
	search_help_text = 'Поиск по id, заголовку, названию професии и id професиии'


@admin.register(YearDiagram)
class YearDiagramAdmin(admin.ModelAdmin):
	list_display = ('id', 'diagram_title', 'profession')
	list_editable = ('diagram_title',)
	list_select_related = ('profession', )
	search_fields = ('id', 'diagram_title', 'profession__name', 'profession__id')
	search_help_text = 'Поиск по id, заголовку, названию професии и id професиии'


@admin.register(CitiesDiagram)
class CitiesDiagramAdmin(admin.ModelAdmin):
	list_display = ('id', 'diagram_title', 'profession')
	list_editable = ('diagram_title',)
	list_select_related = ('profession',)
	search_fields = ('id', 'diagram_title', 'profession__name', 'profession__id')
	search_help_text = 'Поиск по id, заголовку, названию професии и id професиии'


@admin.register(CitiesVacanciesDiagram)
class CitiesVacanciesDiagramAdmin(admin.ModelAdmin):
	list_display = ('id', 'diagram_title', 'profession')
	list_editable = ('diagram_title',)
	list_select_related = ('profession',)
	search_fields = ('id', 'diagram_title', 'profession__name', 'profession__id')
	search_help_text = 'Поиск по id, заголовку, названию професии и id професиии'


@admin.register(VacanciesDiagram)
class VacanciesDiagramAdmin(admin.ModelAdmin):
	list_display = ('id', 'diagram_title', 'profession')
	list_editable = ('diagram_title',)
	list_select_related = ('profession',)
	search_fields = ('id', 'diagram_title', 'profession__name', 'profession__id')
	search_help_text = 'Поиск по id, заголовку, названию професии и id професиии'


@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
	list_display = ('id', 'year', 'is_visible', 'profession')
	list_filter = ('is_visible', )
	list_editable = ('year', 'is_visible')
	list_select_related = ('profession',)
	search_fields = ('id', 'year', 'profession__name', 'profession__id')
	search_help_text = 'Поиск по id, году, названию професии и id професиии'
	inlines = (SkillsInline, )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'weight', 'year')
	list_editable = ('name', 'weight')
	list_select_related = ('year',)
	search_fields = ('id', 'year__year', 'year__profession__name', 'year__profession__id')
	search_help_text = 'Поиск по id, году, названию професии и id професиии'
