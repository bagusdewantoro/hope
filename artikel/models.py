from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe # menampilkan gambar di admin
import uuid # untuk generate id

#=====================================================================
class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=100, help_text='(max = 100 character)')
    figure1 = ImageField(upload_to='static/img', null=True, blank=True)
    figure2 = ImageField(upload_to='static/img', null=True, blank=True)
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
        ordering = ['name']
        verbose_name = 'Name'
        verbose_name_plural = 'Name'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail-product', args=[str(self.id)])

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
class InstanceProduct(models.Model):
    id = models.UUIDField('Code', primary_key=True, default=uuid.uuid4)
    product = models.ForeignKey('Product', verbose_name='Name', on_delete=models.SET_NULL, null=True)
    production_date = models.DateField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)
    # PR = CARI TENTANG STOCKLOG https://community.simpleisbetterthancomplex.com/t/how-to-add-and-substract-item-form-a-product-model/198
    # setelah dapet di atas, bikin perkalian antara sold dan quantity

    class Meta:
        ordering = ['production_date']
        verbose_name = 'Stock Log'
        verbose_name_plural = 'Stock Log'

    def __str__(self):
        return f'{self.id} ({self.product.name})'

#=====================================================================
    
