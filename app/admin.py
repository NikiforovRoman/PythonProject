from django.contrib import admin
from .models import *


class DescriptionsInline(admin.TabularInline):
	model = Profession.description_blocks.through


# Register your models here.
@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'is_visible', )
	list_filter = ('is_visible', )
	list_display_links = ('id', 'name')
	exclude = ('description_blocks', )
	inlines = (DescriptionsInline,)


@admin.register(ProfessionDescriptionBlock)
class ProfessionDescriptionBlockAdmin(admin.ModelAdmin):
	pass


@admin.register(YearDiagram)
class YearDiagramAdmin(admin.ModelAdmin):
	pass


@admin.register(CitiesDiagram)
class CitiesDiagramAdmin(admin.ModelAdmin):
	pass


@admin.register(CitiesVacanciesDiagram)
class CitiesVacanciesDiagramAdmin(admin.ModelAdmin):
	pass


@admin.register(VacanciesDiagram)
class VacanciesDiagramAdmin(admin.ModelAdmin):
	pass


@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
	pass


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
	pass

