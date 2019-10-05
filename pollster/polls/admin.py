from django.contrib import admin

from .models import Question, Choice

# To Change the labels of django admin
admin.site.site_header = "Pollster Admin"
admin.site.site_title = 'Pollster Admin Area'
admin.site.index_title = 'Welcome to the Pollster admin area'

# Purpose of doing this is to not show Choice in Polls,
# but rather inside Question

# Tabular inline method
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # A tuple
    fieldsets = [
        (None, {
            'fields': ['question_text']
        }), 
        ('Date information', {
            'fields': ['publish_date'], 
            'classes': ['collapse']
        }),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)