from django.db import models

class UserProfile(models.Model):
    # Campos que coinciden con tu tabla 'users'
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, default='user')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Importante para usar tu tabla existente
        db_table = 'users'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.email

class Product(models.Model):
    # Campos que coinciden con tu tabla 'products'
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    stock = models.IntegerField(default=0)
    category = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'products'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name
