import os
import django
from faker import Faker
import random
from events.models import Event, Participant, Category

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "event_management.settings")
django.setup()


def populate_db():
    fake = Faker()

    # Create Categories
    categories = [
        Category.objects.create(
            name=fake.word().capitalize(),
            description=fake.sentence(),
        )
        for _ in range(5)
    ]
    print(f"Created {len(categories)} categories.")

    # Create Participants
    participants = [
        Participant.objects.create(
            name=fake.name(),
            email=fake.unique.email(),
        )
        for _ in range(20)
    ]
    print(f"Created {len(participants)} participants.")

    # Create Events
    events = []
    for _ in range(10):
        event = Event.objects.create(
            name=fake.catch_phrase(),
            description=fake.paragraph(),
            date=fake.date_this_year(),
            time=fake.time(),
            location=fake.city(),
            category=random.choice(categories),
        )
        # Assign 1 to 5 random participants
        selected_participants = random.sample(participants, random.randint(1, 5))
        event.participants.set(selected_participants)
        events.append(event)
    print(f"Created {len(events)} events.")

    print("Database populated successfully!")


if __name__ == "__main__":
    populate_db()
