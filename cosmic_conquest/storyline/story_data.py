# cosmic_conquest/storyline/story_data.py

STORY_ARCS = {
    "start": {
        "description": (
            "В далёком уголке галактики ваш флот наткнулся на сигналы древней цивилизации. "
            "Учёные подтверждают, что это может быть маяк Предков, о которых ходит множество легенд. "
            "Говорят, их технологии опережали современный уровень на тысячелетия."
        ),
        "triggers": {
            "next": "ancient_ruins"
        },
        "dialogue_id": "dialogue_1"
    },
    "ancient_ruins": {
        "description": (
            "Высадка на безымянную планету прошла успешно. "
            "Руины покрыты непонятными символами, а аномальные поля искажают сигналы. "
            "На горизонте виднеются силуэты чужих форм жизни."
        ),
        "triggers": {
            "if_has_card_5": "artifact_discovery",
            "else": "enemy_encounter"
        },
        "dialogue_id": "dialogue_2"
    },
    "artifact_discovery": {
        "description": (
            "В глубине руин вы находите светящийся кристалл – один из Фрагментов Матрицы Предков. "
            "Это потенциальный ключ к колоссальной силе. Однако здесь же просыпается нечто..."
        ),
        "triggers": {
            "next": "awakening_guardian"
        },
        "dialogue_id": "dialogue_3"
    },
    "enemy_encounter": {
        "description": (
            "Не успели вы подойти ближе к центральным залам, как из тени вынырнули жуткие ксенопаразиты. "
            "Их передвигающиеся щупальца и кислотный яд смертельно опасны. "
            "Вам придётся либо отступить, либо принять бой."
        ),
        "triggers": {
            "next": "combat_scenario"
        },
        "dialogue_id": "dialogue_4"
    },
    "awakening_guardian": {
        "description": (
            "Хранитель руин, огромный механический конструкт, активируется и медленно поднимается. "
            "Его металлические глаза загораются синим пламенем. "
            "Он издаёт грохочущий звук, напоминающий древний язык Предков."
        ),
        "triggers": {
            "choice_a": "guardian_fight",
            "choice_b": "guardian_parley"
        },
        "dialogue_id": "dialogue_5"
    },
    "guardian_fight": {
        "description": (
            "Вы решаете атаковать хранителя. Грохочущие выстрелы эхом летят по залу, "
            "но его броня оказывается крепче, чем вы ожидали..."
        ),
        "triggers": {
            "next": "post_guardian_fight"
        },
        "dialogue_id": "dialogue_fight_guardian"
    },
    "guardian_parley": {
        "description": (
            "Вы пытаетесь установить контакт с конструктом. "
            "При упоминании Матрицы Предков, он замолкает, будто пытается понять, "
            "кто вы и достойны ли вы знаний его создателей..."
        ),
        "triggers": {
            "next": "post_guardian_parley"
        },
        "dialogue_id": "dialogue_parley_guardian"
    },
    "post_guardian_fight": {
        "description": (
            "Несмотря на суровое сопротивление, хранитель пал. Но цена победы высока, "
            "и руины начали рушиться. Возможно, вы упустили шанс получить истинное знание."
        ),
        "triggers": {
            "next": "cosmic_decision"
        },
        "dialogue_id": "dialogue_post_fight"
    },
    "post_guardian_parley": {
        "description": (
            "Конструкт сканирует ваши войска и освобождает проход к Центральному Хранилищу. "
            "Возможно, теперь вы сможете получить доступ к глубинной памяти Предков."
        ),
        "triggers": {
            "next": "cosmic_decision"
        },
        "dialogue_id": "dialogue_post_parley"
    },
    "combat_scenario": {
        "description": (
            "Сражение с ксенопаразитами требует быстрых решений: "
            "либо вы отступаете и теряете часть отряда, либо идёте ва-банк."
        ),
        "triggers": {
            "next": "cosmic_decision"
        },
        "dialogue_id": "dialogue_combat"
    },
    "cosmic_decision": {
        "description": (
            "Теперь, когда ваша экспедиция прошла через опасности, вы стоите на распутье. "
            "Что дальше? Вернуться на базу с тем, что узнали? Продолжить поиски остальных фрагментов? "
            "Или вступить в союз с другой расой, чтобы вместе расшифровать данные?"
        ),
        "triggers": {
            "choice_a": "share_knowledge",
            "choice_b": "go_alone"
        },
        "dialogue_id": "dialogue_decision"
    },
    "share_knowledge": {
        "description": (
            "Вы решаете поделиться открытиями с союзниками, надеясь на совместное будущее. "
            "Новый альянс может укрепиться, но будьте готовы к политическим интригам..."
        ),
        "triggers": {},
        "dialogue_id": "dialogue_share"
    },
    "go_alone": {
        "description": (
            "Вы храните знания при себе, боясь предательства. "
            "Теперь ваша раса обладает большим потенциалом, но союзники могут отвернуться от вас..."
        ),
        "triggers": {},
        "dialogue_id": "dialogue_alone"
    },
}
