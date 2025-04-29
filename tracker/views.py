from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Count
from .models import QuestionCollection, Question, UserProgress, Topic

def home(request):
    collections = QuestionCollection.objects.all()
    return render(request, 'tracker/home.html', {'collections': collections})

# def collection_questions(request, collection_id):
    collection = get_object_or_404(QuestionCollection, id=collection_id)
    topics = collection.topics.all().prefetch_related('questions')
    
    # Get all questions for this collection
    questions = collection.questions.all()
    
    # If user is authenticated, get their progress
    if request.user.is_authenticated:
        user_progress = UserProgress.objects.filter(
            user=request.user,
            question__collection=collection
        ).select_related('question')
        
        # Create a dict for quick lookup
        progress_dict = {p.question_id: p for p in user_progress}
        
        # Attach progress data to questions
        for question in questions:
            if question.id in progress_dict:
                progress = progress_dict[question.id]
                question.is_solved = progress.is_solved
                question.review_count = progress.review_count
            else:
                question.is_solved = False
                question.review_count = 0
    
    # Group questions by topic
    topics_with_questions = []
    for topic in topics:
        topic_questions = [q for q in questions if q.topic_id == topic.id]
        if topic_questions:
            topics_with_questions.append({
                'topic': topic,
                'questions': topic_questions
            })
    
    # Handle questions without a topic
    uncategorized = [q for q in questions if q.topic_id is None]
    if uncategorized:
        topics_with_questions.append({
            'topic': None,
            'questions': uncategorized
        })
    
    return render(request, 'tracker/questions.html', {
        'collection': collection,
        'topics_with_questions': topics_with_questions
    })

def collection_questions(request, collection_id):
    collection = get_object_or_404(QuestionCollection, id=collection_id)
    topics = collection.topics.all().prefetch_related('questions')
    
    # Get all questions for this collection using the many-to-many relationship
    questions = Question.objects.filter(collections=collection)
    
    # If user is authenticated, get their progress
    if request.user.is_authenticated:
        user_progress = UserProgress.objects.filter(
            user=request.user,
            question__in=questions
        ).select_related('question')
        
        # Create a dict for quick lookup
        progress_dict = {p.question_id: p for p in user_progress}
        
        # Attach progress data to questions
        for question in questions:
            if question.id in progress_dict:
                progress = progress_dict[question.id]
                question.is_solved = progress.is_solved
                question.review_count = progress.review_count
            else:
                question.is_solved = False
                question.review_count = 0
    
    # Group questions by topic
    topics_with_questions = []
    for topic in topics:
        topic_questions = [q for q in questions if q.topic_id == topic.id]
        if topic_questions:
            topics_with_questions.append({
                'topic': topic,
                'questions': topic_questions
            })
    
    # Handle questions without a topic
    uncategorized = [q for q in questions if q.topic_id is None]
    if uncategorized:
        topics_with_questions.append({
            'topic': None,
            'questions': uncategorized
        })
    
    return render(request, 'tracker/questions.html', {
        'collection': collection,
        'topics_with_questions': topics_with_questions
    })


@login_required
def toggle_solved(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    progress, created = UserProgress.objects.get_or_create(
        user=request.user,
        question=question,
        defaults={'is_solved': False, 'review_count': 0}
    )
    
    progress.is_solved = not progress.is_solved
    progress.save()
    
    return JsonResponse({
        'is_solved': progress.is_solved
    })

@login_required
def increment_review(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    progress, created = UserProgress.objects.get_or_create(
        user=request.user,
        question=question,
        defaults={'is_solved': False, 'review_count': 0}
    )
    
    progress.review_count += 1
    progress.save()
    
    return JsonResponse({
        'review_count': progress.review_count
    })

@login_required
def decrement_review(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    progress, created = UserProgress.objects.get_or_create(
        user=request.user,
        question=question,
        defaults={'is_solved': False, 'review_count': 0}
    )
    
    # Ensure count doesn't go below 0
    if progress.review_count > 0:
        progress.review_count -= 1
        progress.save()
    
    return JsonResponse({
        'review_count': progress.review_count
    })

@login_required
def reset_review(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    progress, created = UserProgress.objects.get_or_create(
        user=request.user,
        question=question,
        defaults={'is_solved': False, 'review_count': 0}
    )
    
    progress.review_count = 0
    progress.save()
    
    return JsonResponse({
        'review_count': progress.review_count
    })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home page after logout