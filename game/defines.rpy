### Audio/Sound system definitions

define corridor_ambience_sfx = [
        {"file": sfx_tree_rustle, "tags": ["tree"], "vol": 0.2},
        {"file": sfx_tree_rustle_intense, "tags": ["tree"], "vol": 0.1},
        {"file": sfx_tree_rustle_soft, "tags": ["tree"], "vol": 0.2},
        {"file": sfx_wind_howl_1, "tags": ["wind"],   "vol": 0.3},
        {"file": sfx_wind_howl_2, "tags": ["wind"],   "vol": 0.3}
]

### IMPORTANT STORY DEFINITIONS/DEFAULTS
### Character Thoughts / Personality

default mc_personality = ["Ren is calm, introspective, and observes before acting. He avoids emotional confrontation and rarely reveals his feelings. He lives with an internal conflict between what he feels and what he believes he should feel."]

default miya_personality = ["Miya is quietly cheerful and outgoing, sometimes impulsive. She values friendship and loyalty, even to the point of stubbornness. Her energetic nature can both uplift and overwhelm those around her. She speaks her mind when comfortable, but can also retreat into silence when she feels unsure."]

### Choices dictionaries

define routes_corridorA = {
        "opt1": "corridors_Aa",
        "opt2": "corridors_Ab",
        "opt3": "corridors_Ac",
}

define routes_corridorB = {
        "opt1": "corridors_Ba",
        "opt2": "corridors_Bb",
        "opt3": "corridors_Bc",
}