from django.contrib import admin
from .models import QuestionCollection, Topic, Question, UserProgress

class QuestionCollectionInline(admin.TabularInline):
    model = Question.collections.through
    extra = 1
    verbose_name = "Question"
    verbose_name_plural = "Questions"

@admin.register(QuestionCollection)
class QuestionCollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'question_count')
    
    def question_count(self, obj):
        return obj.questions.count()
    question_count.short_description = 'Number of Questions'
    
    # We can't use the old inline because the relationship is reversed
    # Instead we'll use the custom page for the collection to see its questions

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'collection')
    list_filter = ('collection',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_collections', 'link')
    list_filter = ('collections', 'topic')  # Changed from 'collection'
    search_fields = ('title',)
    filter_horizontal = ('collections',)  # Adds a nice widget for managing many-to-many
    
    def get_collections(self, obj):
        """Return comma-separated list of collection names"""
        return ", ".join([c.name for c in obj.collections.all()])
    get_collections.short_description = 'Collections'

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'is_solved', 'review_count')
    list_filter = ('user', 'is_solved')
    search_fields = ('user__username', 'question__title')
    
    # Custom filter for collections through the question
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user', 'question')
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "question":
            kwargs["queryset"] = Question.objects.select_related('topic')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)