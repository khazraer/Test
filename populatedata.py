import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','locallibrary.settings')
import django
django.setup()
from faker import Faker

from catalog.models import *
fake = Faker()
for i in range(3):
    Author.first_name = fake.name()

    print(fake.name())

def populate(N=3):
    for entry in range(N):
        f_first_name = fake.first_name()
        f_last_name = fake.last_name()
        f_date_of_birth = fake.date_of_birth()
        author = Author.objects.create(first_name = f_first_name, last_name = f_last_name , date_of_birth = f_date_of_birth)

        # Book
        f_title = fake.sentence()
        f_summary =fake.text()
        book =Book.objects.create(title=f_title ,author = author , summary = f_summary )


if __name__ =='__main__':
    print("populating data" )
    populate()
    print("pupulated data ")
