from django.core.management.base import BaseCommand
from tracker.models import QuestionCollection, Topic, Question

class Command(BaseCommand):
    help = 'Import Striver191 questions'

    def handle(self, *args, **kwargs):
        # Create or get the Striver191 collection
        striver191, created = QuestionCollection.objects.get_or_create(
            name='Striver191',
            defaults={'description': 'A comprehensive list of 191 questions curated by Striver for coding interview preparation.'}
        )
        
        # Import topics and their questions
        self.import_arrays(striver191)
        # Add more topic import methods as needed:
        # self.import_strings(striver191)
        # self.import_linked_lists(striver191)
        # etc.
        
    def import_arrays(self, striver191):
        # Create or get the Arrays topic
        arrays_topic, _ = Topic.objects.get_or_create(
            name='Arrays',
            collection=striver191
        )
        
        # Add array questions
        arrays_questions = [
            # Add your questions in format: ('Question Title', 'URL Link')
            # Example:
            # ('Set Matrix Zeroes', 'https://leetcode.com/problems/set-matrix-zeroes/'),
            # ('Pascal Triangle', 'https://leetcode.com/problems/pascals-triangle/'),
        ]
        
        count = 0
        for title, link in arrays_questions:
            question, created = Question.objects.get_or_create(
                title=title,
                link=link,
                collection=striver191,
                topic=arrays_topic
            )
            if created:
                count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} Arrays questions for Striver191'))
    
    # Add more topic methods here as needed, e.g.:
    # def import_strings(self, striver191):
    #     strings_topic, _ = Topic.objects.get_or_create(
    #         name='Strings',
    #         collection=striver191
    #     )
    #     
    #     # Add strings questions...