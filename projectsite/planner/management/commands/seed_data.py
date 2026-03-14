from django.core.management.base import BaseCommand
from faker import Faker
import random
from django.utils import timezone

from planner.models import Task, SubTask, Note, Category, Priority


class Command(BaseCommand):
    help = "Generate fake data for Hangarin Task Manager"

    def handle(self, *args, **kwargs):

        fake = Faker()

        categories = list(Category.objects.all())
        priorities = list(Priority.objects.all())

        for _ in range(20):

            task = Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                status=fake.random_element(
                    elements=["Pending", "In Progress", "Completed"]
                ),
                category=random.choice(categories),
                priority=random.choice(priorities),
            )

            # create subtasks
            for _ in range(random.randint(1, 3)):
                SubTask.objects.create(
                    parent_task=task,
                    title=fake.sentence(nb_words=4),
                    status=fake.random_element(
                        elements=["Pending", "In Progress", "Completed"]
                    ),
                )

            # create notes
            for _ in range(random.randint(1, 2)):
                Note.objects.create(
                    task=task,
                    content=fake.paragraph(nb_sentences=2),
                )

        self.stdout.write(self.style.SUCCESS("Fake data generated successfully!"))