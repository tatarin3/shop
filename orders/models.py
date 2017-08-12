from django.db import models

# Create your models here.
class Order(models.Model):
	customer_name = models.CharField(max_length=128, blank=True, null=True, default=None)
	customer_email = models.EmailField(blank=True, null=True, default=None)
	customer_phone = models.CharField(max_length=32, blank=True, null=True, default=None)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "Заказ %s" % self.id

	class Meta:
		verbose_name = "Заказ"
		verbose_name_plural = "Заказы"

class ProductOrder(models.Model):
	order = models.ForeignKey(Order, blank=True, null=True, default=None)
	order = models.ForeignKey(Product, blank=True, null=True, default=None)
	comments = models.TextField(blank=True, null=True, default=None)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "%s" % self.product.name

	class Meta:
		verbose_name = "Товар"
		verbose_name_plural = "Товары"