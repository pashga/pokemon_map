from django.db import models  # noqa F401

class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200,
                                verbose_name="Название на русском",
                                blank=True
                                )
    image = models.ImageField(blank=True,
                              null=True,
                              upload_to="pokemons_images",
                              verbose_name="Изображение",
                              )
    description = models.TextField(blank=True, verbose_name="Описание")
    title_en = models.CharField(max_length=200,
                                verbose_name="Название на английском",
                                blank=True,
                                )
    title_jp = models.CharField(max_length=200,
                                verbose_name="Название на японском",
                                blank=True,
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
    lat = models.FloatField(verbose_name="Широта",)
    lon = models.FloatField(verbose_name="Долгота")
    appeared_at = models.DateTimeField(verbose_name="Появляется",
                                       blank=True,
                                       null=True,
                                       )
    disappeared_at = models.DateTimeField(verbose_name="Исчезает",
                                          blank=True,
                                          null=True,
                                          )
    pokemon = models.ForeignKey(Pokemon,
                                on_delete=models.CASCADE,
                                verbose_name="Название",
                                )
    level = models.IntegerField(verbose_name="Уровень",
                                blank=True,
                                null=True,
                                )
    health = models.IntegerField(verbose_name="Здоровье",
                                 blank=True,
                                 null=True,
                                 )
    strength = models.IntegerField(verbose_name="Сила",
                                   blank=True,
                                   null=True,
                                   )
    defence = models.IntegerField(verbose_name="Защита",
                                  blank=True,
                                  null=True,
                                  )
    stamina = models.IntegerField(verbose_name="Выносливость",
                                  blank=True,
                                  null=True,
                                  )

    def __str__(self):
        return f"{self.pokemon}"
