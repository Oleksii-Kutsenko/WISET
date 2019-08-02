from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64, unique=True, db_index=True, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    category = models.CharField(max_length=64, db_index=True, null=False)
    in_fridge = models.BooleanField(null=False)
    season_start = models.DateField(db_index=True, null=False)
    season_end = models.DateField(db_index=True, null=False)

    def __repr__(self):
        return "<Product {} {} {} {} {} {}>".format(self.name,
                                                    self.price,
                                                    self.category,
                                                    self.in_fridge,
                                                    self.season_start,
                                                    self.season_end)

    def __str__(self):
        return self.__repr__()
