from django.db import models

# Create your models here.

class BMW(models.Model):
    model = models.ForeignKey('BMW', verbose_name='madel', on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=255,verbose_name='Nomi', help_text='Mashina nomi')



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'BMW'
        verbose_name_plural = 'BMW'




class Captiva(models.Model):
    name = models.CharField(max_length=255,verbose_name='Nomi', help_text='Mashina nomi')
    model = models.ForeignKey('BMW', verbose_name='madel',on_delete=models.PROTECT, null=True,blank=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Captiva'
        verbose_name_plural = 'Captiva'
