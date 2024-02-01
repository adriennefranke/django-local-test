from django.db import models

from django.db.models import Q


class Cake(models.Model):
    cake_flavor = models.CharField(max_length=256)
    filling_flavor = models.CharField(max_length=256)
    slices = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=6)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=~Q(cake_flavor="Peanut Butter"),
                name="no_peanut_butter_flavor",
                violation_error_message="We cannot have Peanut Butter as a flavor due to allergies",
            ),
            models.UniqueConstraint(
                fields=("cake_flavor", "filling_flavor"),
                name="uniq_cake_flavor_filling_flavor",
                condition=Q(slices=8),
                violation_error_message="Oh no! We already have this cake in 8 slices.",
            ),
        ]
