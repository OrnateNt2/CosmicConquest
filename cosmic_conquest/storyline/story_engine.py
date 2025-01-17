# cosmic_conquest/storyline/story_engine.py

from .story_data import STORY_ARCS
from .dialogues import DIALOGUES

class StoryEngine:
    def __init__(self):
        self.current_arc = "start"

    def check_story_triggers(self, game_instance):
        arc_data = STORY_ARCS.get(self.current_arc)
        if not arc_data:
            return None

        triggers = arc_data.get("triggers", {})
        # Демонстрация проверки, есть ли у кого-либо из игроков карта id=5 (Матрица Предков)
        if "if_has_card_5" in triggers:
            has_artifact = any(
                any(card["id"] == 5 for card in p.hand) 
                for p in game_instance.players
            )
            if has_artifact:
                self.current_arc = triggers["if_has_card_5"]
            else:
                self.current_arc = triggers["else"]
            return self.get_current_story_segment()

        if "next" in triggers:
            self.current_arc = triggers["next"]
            return self.get_current_story_segment()

        return None

    def get_current_story_segment(self):
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
        arc_data = STORY_ARCS.get(self.current_arc, {})
        triggers = arc_data.get("triggers", {})
        if choice in triggers:
            self.current_arc = triggers[choice]
            return self.get_current_story_segment()
        return None
