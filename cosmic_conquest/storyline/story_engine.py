# cosmic_conquest/storyline/story_engine.py

from .story_data import STORY_ARCS
from .dialogues import DIALOGUES

class StoryEngine:
    def __init__(self):
        self.current_arc = "start"

    def check_story_triggers(self, game_instance):
        """
        Проверяем, нужно ли переключиться на новую ветку сюжета,
        исходя из событий в игре (например, какие карты есть у игроков).
        """
        arc_data = STORY_ARCS.get(self.current_arc)
        if not arc_data:
            return None

        triggers = arc_data.get("triggers", {})
        # Пример простейшей логики:
        if "if_has_card_5" in triggers:
            # Проверяем, у кого-нибудь есть карта с id=5 (Фрагмент Матрицы Предков)
            for player in game_instance.players:
                if any(card["id"] == 5 for card in player.hand):
                    self.current_arc = triggers["if_has_card_5"]
                    return self.get_current_story_segment()
            # Иначе
            self.current_arc = triggers["else"]
            return self.get_current_story_segment()

        # Если есть 'next', то просто переходим
        if "next" in triggers:
            self.current_arc = triggers["next"]
            return self.get_current_story_segment()

        return None

    def get_current_story_segment(self):
        """
        Возвращает описание и диалоги текущей ветки сюжета
        """
        arc_data = STORY_ARCS.get(self.current_arc, {})
        description = arc_data.get("description", "")
        dialogue_id = arc_data.get("dialogue_id", "")
        dialogue_text = DIALOGUES.get(dialogue_id, [])
        return {
            "arc_id": self.current_arc,
            "description": description,
            "dialogue": dialogue_text
        }

    def choose_branch(self, choice):
        """
        Вызывается, когда игрок выбирает развилку (choice_a / choice_b и т.д.).
        """
        arc_data = STORY_ARCS.get(self.current_arc, {})
        triggers = arc_data.get("triggers", {})
        if choice in triggers:
            self.current_arc = triggers[choice]
            return self.get_current_story_segment()
        return None
