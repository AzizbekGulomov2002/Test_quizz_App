from django.contrib import admin

# Register your models here.
from .models import *
class AnswerTabular(admin.TabularInline):
    model = Answers
    fields = ['answer','status']
class QuestionTabular(admin.TabularInline):
    model = Questions
    fields = ['test','question']
@admin.register(TestCode)
class TestCodeAdmin(admin.ModelAdmin):
    list_display = ['test_code']
@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['question','updated']
    list_per_page = 10
    inlines = [AnswerTabular]
    fields =  ['test','question']
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user=request.user)
@admin.register(Answers)
class AnswerAdmin(admin.ModelAdmin):


    list_display =['answer','status','question']
    list_per_page = 10
    search_fields = ['answer']

    