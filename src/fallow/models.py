from django.db import models


class Crop(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE, verbose_name='Parent')
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return self.name


class Declare(models.Model):
    member = models.ForeignKey('household.Member', on_delete=models.CASCADE, verbose_name='Member')
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return self.member


class RiceArea(models.Model):
    declare = models.ForeignKey('fallow.Declare', on_delete=models.CASCADE, verbose_name='Declare')
    crop = models.ForeignKey('fallow.Crop', on_delete=models.CASCADE, verbose_name='Crop')
    area = models.FloatField(null=True, verbose_name='Area')
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return str(self.area)


class FallowTransfer(models.Model):
    member = models.ForeignKey('household.Member', on_delete=models.CASCADE, verbose_name='Member')
    crop = models.ForeignKey('fallow.Crop', on_delete=models.CASCADE, verbose_name='Crop')
    subsidy = models.IntegerField(null=True, verbose_name='Subsidy')
    period = models.CharField(max_length=1, null=True, verbose_name='Period')
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return "{}, {}, {}, {}".format(self.member, self.crop, self.subsidy, self.period)


class TransferCrop(models.Model):
    rice_area = models.ForeignKey('fallow.RiceArea', on_delete=models.CASCADE, verbose_name='Rice Area')
    crop = models.ForeignKey('fallow.Crop', on_delete=models.CASCADE, verbose_name='Crop')
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, verbose_name='Updated')

    def __str__(self):
        return "{}, {}".format(self.rice_area, self.crop)
