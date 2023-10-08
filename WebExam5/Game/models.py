from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Game(models.Model):
    ACTION_GAME = "Action"
    ADVEMTURE_GAME = "Adventure"
    PUZZLE_GAME = "Puzzle"
    STRATEGY_GAME = "Strategy"
    SPORTS_GAME = "Sports"
    BOARD_CARD_GAME = "Board/Card Game"
    OTHER_GAME = "Other"

    GAME_TYPES = (
        (ACTION_GAME, ACTION_GAME),
        (ADVEMTURE_GAME, ADVEMTURE_GAME),
        (PUZZLE_GAME, PUZZLE_GAME),
        (STRATEGY_GAME, STRATEGY_GAME),
        (SPORTS_GAME, SPORTS_GAME),
        (BOARD_CARD_GAME, BOARD_CARD_GAME),
        (OTHER_GAME, OTHER_GAME),
    )
    title = models.CharField(
        max_length=30,
        unique=True,
    )

    category = models.CharField(
        max_length=15,
        choices=GAME_TYPES,
    )

    # The rating can be between 0.1 and 5.0 (both inclusive).
    rating = models.FloatField(
        validators=(
            MaxValueValidator(5.0,),
            MinValueValidator(0.1,),
        ),
    )

    # The max level cannot be below 1.
    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=(MinValueValidator(1,),),
        verbose_name='Max Level',
    )

    image_url = models.URLField(
        verbose_name='Image URL',
    )

    summary = models.TextField(
        null=True,
        blank=True,
    )

# Note: the validations will be examined only by the user side, not the admin side.
