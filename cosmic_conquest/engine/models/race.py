# cosmic_conquest/engine/models/race.py

class Race:
    def __init__(self, name="Human"):
        self.name = name
        # Можно задать расовые бонусы
        if name == "Human":
            self.description = "Универсальная раса с балансом в науке и дипломатии."
        elif name == "Zorgon":
            self.description = "Агрессивные воины, сильны в бою, но слабы в дипломатии."
        # и т.д.

    def __repr__(self):
        return f"{self.name}"
