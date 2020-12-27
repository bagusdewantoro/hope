from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe # menampilkan gambar di admin


class Produk(models.Model):
    nama = models.CharField(max_length=20)
    deskripsi = models.TextField(max_length=100, help_text='tulis deskripsi singkat untuk produk ini')
    foto1 = ImageField(upload_to='static/img', null=True, blank=True)
    foto2 = ImageField(upload_to='static/img', null=True, blank=True)

    # tampilkan gambar di admin:
    @property
    def foto1_preview(self):
        if self.foto1:
            return mark_safe('<img src="{}" width="auto" height="100" />'.format(self.foto1.url))
        return ''

    @property
    def foto2_preview(self):
        if self.foto2:
            return mark_safe('<img src="{}" width="auto" height="100" />'.format(self.foto2.url))
        return ''

    price = models.CharField(max_length=20)
    size = models.ManyToManyField(Size)
    tipe = models.ForeignKey('Tipe', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['nama']
        verbose_name = 'Produk'
        verbose_name_plural = 'Produk'

    def __str__(self):
        return self.nama

    def get_absolute_url(self):
        return reverse('detail-produk', args=[str(self.id)])


class Size(models.Model):
    
