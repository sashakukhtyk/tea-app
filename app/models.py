from django.db import models

# Create your models here.
# Categories of Products
class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


# Customers
class Customer(models.Model):
	username = models.CharField(max_length=50)
	email = models.EmailField(max_length=100)
	password = models.CharField(max_length=100)

	def __str__(self):
		return self.username



# All of our Products
class Product(models.Model):
	name = models.CharField(max_length=100)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
	description = models.CharField(max_length=250, default='', blank=True, null=True)
	image = models.ImageField(upload_to='uploads/product/')

	def __str__(self):
		return self.name


class Rewiev(models.Model):
        user = models.ForeignKey(Customer, on_delete=models.CASCADE)
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        comment = models.CharField(max_length=250)
        rate = models.IntegerField(default=0)

        def __str__(self):
	        return str(self.id)