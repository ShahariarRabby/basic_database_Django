import os
import django
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_app.settings')
django.setup()
from first_project.models import Topic, AccessRecord, Webpage, User

fakegen = Faker()
topics = ['search', 'Social', 'Market', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entrry in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.name()
        fake_first_name = fake_name.split()[0]
        fake_last_name = fake_name.split()[1]
        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name=fake_first_name,
                                          last_name=fake_last_name,
                                          email=fake_email)[0]
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print("Start populate....")
    populate(N=20)
    print("Populating Done")
