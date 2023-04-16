from django.db import models

# Create your models here.
class Audi(models.Model):
    name = models.CharField(max_length=255,verbose_name='Nomi', help_text='Mashina nomi')
    date = models.DateTimeField()
    model = models.ForeignKey('Audi',verbose_name='madel',on_delete=models.CASCADE, null=True,blank=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Audi'
        verbose_name_plural = 'Audi'

