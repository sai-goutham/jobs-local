import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','gjproject.settings')
import django
django.setup()


from testap.models import *
from faker import Faker
from  random import *
fake=Faker()
def phoneNumbergen():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Project Manager','TeamLead','software Engineers'))
        feligibility=fake.random_element(elements=('Btech','MSc','Mtech','phd'))
        faddress=fake.address()
        femail=fake.email()
        fphone=phoneNumbergen()
        hydjobs_record=hydjobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,
        email=femail,phoneNumber=fphone)
        punejobs_record=punejobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,
        email=femail,phoneNumber=fphone)
        bangjobs_record=bangjobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,
        email=femail,phoneNumber=fphone)
        ndljobs_record=ndljobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,
        email=femail,phoneNumber=fphone)
populate(30)
