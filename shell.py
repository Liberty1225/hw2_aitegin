from random import randint

from credit.models import Client, Account, Credit


a = Client.objects.create(name='Бердиев Н.Д.', birth_year='1994-12-12', work_place='Codify')
b = Client.objects.create(name='Кубатбекова А.К.', birth_year='1995-06-07', work_place='Freelance')


a1 = Account.objects.create(number=randint(1000000000000000,9999999999999999,), client=a)
a2 = Account.objects.create(number=randint(1000000000000000,9999999999999999,), client=a)
a3 = Account.objects.create(number=randint(1000000000000000,9999999999999999,), client=b)
a4 = Account.objects.create(number=randint(1000000000000000,9999999999999999,), client=b)

a1.credits.create(sum=1000)
a2.credits.create(sum=2000)
a3.credits.create(sum=3000)
a4.credits.create(sum=4000)

