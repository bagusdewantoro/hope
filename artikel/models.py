from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe # menampilkan gambar di admin
import uuid # untuk generate id


#=====================================================================
class Size(models.Model):
    size_name = models.CharField(max_length=5)

    class Meta:
        ordering = ['size_name']
        verbose_name = 'Size'
        verbose_name_plural = 'Size'

    def __str__(self):
        return self.size_name

#=====================================================================
class Type(models.Model):
    type_name = models.CharField(max_length=20)

    class Meta:
        ordering = ['type_name']
        verbose_name = 'Type'
        verbose_name_plural = 'Type'

    def __str__(self):
        return self.type_name

#=====================================================================
class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=100, help_text='(max = 100 character)')
    figure1 = models.ImageField(upload_to='static/img', null=True, blank=True)
    figure2 = models.ImageField(upload_to='static/img', null=True, blank=True)
    size = models.ManyToManyField(Size)
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)

    # tampilkan gambar di admin:
    @property
    def figure1_preview(self):
        if self.figure1:
            return mark_safe('<img src="{}" width="auto" height="100" />'.format(self.figure1.url))
        return ''

    @property
    def figure2_preview(self):
        if self.figure2:
            return mark_safe('<img src="{}" width="auto" height="100" />'.format(self.figure2.url))
        return ''

    class Meta:
        ordering = ['name', 'type']
        verbose_name = 'Name'
        verbose_name_plural = 'Name'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail-product', args=[str(self.id)])

    # tambahan method untuk ManyToManyField = size
    def product_size(self):
        return ', '.join(size.size_name for size in self.size.all()[:5])

    product_size.short_description = 'Size'

#=====================================================================
class StockLog(models.Model):
    id = models.UUIDField('Code', primary_key=True, default=uuid.uuid4)
    product = models.ForeignKey('Product', verbose_name='Name', on_delete=models.SET_NULL, null=True)
    production_date = models.DateField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)

    class Meta:
        ordering = ['production_date', 'product', 'quantity', 'price', 'sold']
        verbose_name = 'Stock Log'
        verbose_name_plural = 'Stock Log'

    def __str__(self):
        return f'{self.product.name} ({self.id})'

    # method untuk mendapatkan sisa produk:
    def remaining(self):
        return self.quantity - self.sold

    # method untuk mendapatkan revenue:
    def revenue(self):
        return self.quantity * self.price
