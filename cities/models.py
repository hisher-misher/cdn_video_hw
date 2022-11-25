from django.db import models
from cities.utils import cities_df


class Point(models.Model):
    x_coord = models.FloatField(blank=True, null=True)
    y_coord = models.FloatField(blank=True, null=True)


class City(models.Model):
    name = models.CharField(max_length=50)
    x_coord = models.FloatField(blank=True, null=True)
    y_coord = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        def get_first(lat, lng):
            """ В базе может быть несколько городов с одинаковым именем, берем первый """
            res_lat = res_lng = None
            if len(lat.to_list()) > 0:
                res_lat = lat.to_list()[0]
            if len(lng.to_list()) > 0:
                res_lng = lng.to_list()[0]
            return res_lat, res_lng

        if self.pk is None:  # при создании ставим координаты из файла.
            city_name = self.name
            lat = cities_df[cities_df['city_ascii'] == city_name]['lat']
            lng = cities_df[cities_df['city_ascii'] == city_name]['lng']

            lat, lng = get_first(lat, lng)

            if all([lat, lng]):
                self.x_coord = lat
                self.y_coord = lng

        else:  # при обновлении ничего не делаем
            pass

        super(City, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
        ordering = ["name"]