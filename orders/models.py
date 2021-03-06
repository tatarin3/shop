from django.db import models
from products.models import Product
# Create your models here.
class Status(models.Model):
	name = models.CharField(max_length=24, blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "Статус %s" % self.name

	class Meta:
		verbose_name = "Статус"
		verbose_name_plural = "Статусы"

class Order(models.Model):
	customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
	customer_email = models.EmailField(blank=True, null=True, default=None)
	customer_phone = models.CharField(max_length=32, blank=True, null=True, default=None)
	comments = models.TextField(blank=True, null=True, default=None)
	status = models.ForeignKey(Status)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "Заказ %s %s" % (self.id, self.status.name)

	class Meta:
		verbose_name = "Заказ"
		verbose_name_plural = "Заказы"

class ProductOrder(models.Model):
	order = models.ForeignKey(Order, blank=True, null=True, default=None)
	product = models.ForeignKey(Product, blank=True, null=True, default=None)

	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "%s" % self.product.name

	class Meta:
		verbose_name = "Товар"
		verbose_name_plural = "Товары"
