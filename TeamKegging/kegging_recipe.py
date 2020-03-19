class Recipe:
    def __init__(self, recipe_id, recipe_volume, recipe_bitter_units, recipe_keg_style, recipe_carbonation):
        self.recipe_id = recipe_id
        self.recipe_volume = recipe_volume
        self.recipe_bitter_units = recipe_bitter_units
        self.recipe_keg_style = recipe_keg_style
        self.recipe_carbonation = recipe_carbonation

    def __str__(self):
        return self.name