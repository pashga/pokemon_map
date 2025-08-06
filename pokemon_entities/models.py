from django.db import models  # noqa F401

class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200,
                                verbose_name="Название на русском"
                                )
    image = models.ImageField(null=True, verbose_name="Изображение")
    description = models.TextField(verbose_name="Описание")
    title_en = models.CharField(max_length=200,
                                verbose_name="Название на английском"
                                )
    title_jp = models.CharField(max_length=200,
                                verbose_name="Название на японском"
                                )
    previous_evolution = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="next_evolutions",
        verbose_name="Из кого эволюционирует"
    )

    def __str__(self):
        return f"{self.title_ru}"


class PokemonEntity(models.Model):
    lat = models.FloatField(verbose_name="Широта")
    lon = models.FloatField(verbose_name="Долгота")
    appeared_at = models.DateTimeField(verbose_name="Появляется")
    disappeared_at = models.DateTimeField(verbose_name="Исчезает")
    pokemon = models.ForeignKey(Pokemon,
                                on_delete=models.CASCADE,
                                verbose_name="Название",
                                )
    level = models.IntegerField(verbose_name="Уровень")
    health = models.IntegerField(verbose_name="Здоровье")
    strength = models.IntegerField(verbose_name="Сила")
    defence = models.IntegerField(verbose_name="Защита")
    stamina = models.IntegerField(verbose_name="Выносливость")

    def __str__(self):
        return f"{self.pokemon}"
