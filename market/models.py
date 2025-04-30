from django.db import models
from django.contrib.auth import get_user_model
from django.db.utils import OperationalError
# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.IntegerField(default=0)
    market_name = models.CharField(max_length=100, default='Walmart')
    image = models.ImageField(upload_to='items/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


def create_admin():
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        try:
            User.objects.create_superuser('admin', 'admin@example.com', 'admin12345')
            print("Superuser 'admin' created.")
        except OperationalError:
            pass  # migration öncesi hata olmasın

create_admin()