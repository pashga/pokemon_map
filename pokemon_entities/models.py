from django.db import models  # noqa F401

class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200)
    image = models.ImageField(null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title_ru}"


class PokemonEntity(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField()
    disappeared_at = models.DateTimeField()
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    level = models.IntegerField()
    health = models.IntegerField()
    strength = models.IntegerField()
    defence = models.IntegerField()
    stamina = models.IntegerField()

    def __str__(self):
        return f"{self.pokemon}"
