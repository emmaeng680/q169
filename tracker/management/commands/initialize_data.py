from django.core.management.base import BaseCommand
from tracker.models import QuestionCollection

class Command(BaseCommand):
    help = 'Initialize question collections'

    def handle(self, *args, **kwargs):
        # Create the collections
        grind169, created = QuestionCollection.objects.get_or_create(
            name='Grind169',
            defaults={
                'description': 'A curated list of 169 leetcode questions to help you ace the coding interviews.'
            }
        )
        
        striver191, created = QuestionCollection.objects.get_or_create(
            name='Striver191',
            defaults={
                'description': 'SDE Sheet: Striver\'s 191 selected interview problems.'
            }
        )

        blind75, created = QuestionCollection.objects.get_or_create(
            name='Blind75',
            defaults={
                'description': 'A list of 75 essential coding interview questions commonly referred to as Blind 75.'
            }
        )

        neetcode150, created = QuestionCollection.objects.get_or_create(
            name='NeetCode150',
            defaults={
                'description': 'A collection of 150 LeetCode questions handpicked by NeetCode, covering essential patterns and concepts for technical interviews.'
            }
        )
        
        self.stdout.write(self.style.SUCCESS('Successfully initialized question collections'))