# cosmic_conquest/engine/models/race.py

class Race:
    def __init__(self, name="Human"):
        self.name = name
        if name == "Human":
            self.description = "Универсальная раса с балансом в науке и дипломатии."
        elif name == "Zorgon":
            self.description = "Агрессивные воины, сильны в бою."
        elif name == "Aphaen":
            self.description = "Мастера технологий, быстрые исследования, слабый флот."
        else:
            self.description = "Неизвестная раса..."

    def __repr__(self):
        return f"{self.name}"
