from django.db import models

# Create your models here.

choices=(
    ('AVAILABLE', 'Item ready to purchased'),
    ('SOLD', 'Item Sold'),
    ('RESTOCK', 'Item restock few days'),
)

class Base(models.Model):
	name = models.CharField(max_length=20, blank=False)
	price = models.IntegerField()
	status=models.CharField(max_length=20, choices=choices, default="SOLD")

	class Meta:
		abstract=True

	def __str__(self):
		return self.name

class Laptop(Base):
	pass

class Phone(Base):
	pass
   