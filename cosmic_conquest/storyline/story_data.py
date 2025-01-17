# cosmic_conquest/storyline/story_data.py

"""
Хранит основные сюжетные ветки и условия их активации.
Предположим, что это словарь, где ключ - ID сцены, а значение - данные:
- короткое описание
- условия перехода (triggers)
- список вариантов ответа
"""

STORY_ARCS = {
    "start": {
        "description": "Вы обнаружили древний маяк Предков. Ваши учёные пытаются понять его назначение...",
        "triggers": {
            "next": "ancient_ruins"
        },
        "dialogue_id": "dialogue_1"
    },
    "ancient_ruins": {
        "description": "Команда исследователей высадилась на затерянную планету, где находятся руины.",
        "triggers": {
            "if_has_card_5": "artifact_discovery",
            "else": "enemy_encounter"
        },
        "dialogue_id": "dialogue_2"
    },
    "artifact_discovery": {
        "description": "Вы нашли Фрагмент Матрицы Предков! Это может стать ключом к победе.",
        "triggers": {
            "next": "cosmic_decision"
        },
        "dialogue_id": "dialogue_3"
    },
    "enemy_encounter": {
        "description": "На подлёте к руинам корабль атакован ксенопаразитами!",
        "triggers": {
            "next": "combat_scenario"
        },
        "dialogue_id": "dialogue_4"
    },
    "cosmic_decision": {
        "description": "Теперь у вас есть выбор — сохранить артефакт или поделиться им с союзником?",
        "triggers": {
            "choice_a": "share_artifact",
            "choice_b": "keep_artifact"
        },
        "dialogue_id": "dialogue_5"
    },
    # ... и так далее ...
}
