from django.db import models


class City(models.Model):
    name = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default=None)

    def __str__(self):
        return f"{self.name}"


class RestaurantAdress(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    city = models.CharField(max_length=50, default=None)
    postal = models.SlugField(max_length=6, default="00-000")
    street = models.CharField(max_length=100, default=None)
    building = models.SlugField(max_length=4, default=None)

    def __str__(self):
        return f"{self.street} {self.building}, {self.postal} {self.city}"


class FoodType(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    food_type = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.food_type

    def __hash__(self):
        return hash(self.food_type)


class Meal(models.Model):
    food_type = models.ForeignKey(FoodType, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default=None)
    price = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.food_type} - {self.name}"


# todo: Add one more table with images for each meal, connect it with Foreignkey relations to Meal.name
