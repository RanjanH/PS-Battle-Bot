move_list = {
    "absorb": {
        "accuracy": 100,
        "basePower": 20,
        "category": "special",
        "drain": [
            1,
            2
        ],
        "flags": {
            "heal": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "absorb",
        "name": "Absorb",
        "pp": 25,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass"
    },
    "accelerock": {
        "accuracy": 100,
        "basePower": 40,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "accelerock",
        "name": "Accelerock",
        "pp": 20,
        "priority": 1,
        "secondary": None,
        "target": "normal",
        "type": "rock"
    },
    "acid": {
        "accuracy": 100,
        "basePower": 40,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "acid",
        "name": "Acid",
        "pp": 30,
        "priority": 0,
        "secondary": {
            "boosts": {
                "special-defense": -1
            },
            "chance": 10
        },
        "target": "allAdjacentFoes",
        "type": "poison"
    },
    "acidarmor": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "defense": 2
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "acidarmor",
        "name": "Acid Armor",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "poison"
    },
    "acidspray": {
        "accuracy": 100,
        "basePower": 40,
        "category": "special",
        "flags": {
            "bullet": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "acidspray",
        "name": "Acid Spray",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "boosts": {
                "special-defense": -2
            },
            "chance": 100
        },
        "target": "normal",
        "type": "poison"
    },
    "acrobatics": {
        "accuracy": 100,
        "basePower": 110,
        "category": "physical",
        "flags": {
            "contact": 1,
            "distance": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "acrobatics",
        "name": "Acrobatics",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "any",
        "type": "flying"
    },
    "acupressure": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {},
        "id": "acupressure",
        "name": "Acupressure",
        "pp": 30,
        "priority": 0,
        "secondary": None,
        "target": "adjacentAllyOrSelf",
        "type": "normal"
    },
    "aerialace": {
        "accuracy": True,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "contact": 1,
            "distance": 1,
            "mirror": 1,
            "protect": 1,
            "slicing": 1
        },
        "id": "aerialace",
        "name": "Aerial Ace",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "any",
        "type": "flying"
    },
    "aeroblast": {
        "accuracy": 95,
        "basePower": 100,
        "category": "special",
        "flags": {
            "distance": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "aeroblast",
        "name": "Aeroblast",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "any",
        "type": "flying"
    },
    "afteryou": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "bypasssub": 1
        },
        "id": "afteryou",
        "name": "After You",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "agility": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "speed": 2
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "agility",
        "name": "Agility",
        "pp": 30,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "psychic"
    },
    "aircutter": {
        "accuracy": 95,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "slicing": 1,
            "wind": 1
        },
        "id": "aircutter",
        "name": "Air Cutter",
        "pp": 25,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "flying"
    },
    "airslash": {
        "accuracy": 95,
        "basePower": 75,
        "category": "special",
        "flags": {
            "distance": 1,
            "mirror": 1,
            "protect": 1,
            "slicing": 1
        },
        "id": "airslash",
        "name": "Air Slash",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "volatileStatus": "flinch"
        },
        "target": "any",
        "type": "flying"
    },
    "allyswitch": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {},
        "id": "allyswitch",
        "name": "Ally Switch",
        "pp": 15,
        "priority": 2,
        "secondary": None,
        "target": "self",
        "type": "psychic"
    },
    "amnesia": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "special-defense": 2
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "amnesia",
        "name": "Amnesia",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "psychic"
    },
    "anchorshot": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "anchorshot",
        "name": "Anchor Shot",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "steel"
    },
    "ancientpower": {
        "accuracy": 100,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "ancientpower",
        "name": "Ancient Power",
        "pp": 5,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "self": {
                "boosts": {
                    "attack": 1,
                    "defense": 1,
                    "special-attack": 1,
                    "special-defense": 1,
                    "speed": 1
                }
            }
        },
        "target": "normal",
        "type": "rock"
    },
    "appleacid": {
        "accuracy": 100,
        "basePower": 80,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "appleacid",
        "name": "Apple Acid",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "special-defense": -1
            },
            "chance": 100
        },
        "target": "normal",
        "type": "grass"
    },
    "aquacutter": {
        "accuracy": 100,
        "basePower": 70,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "slicing": 1
        },
        "id": "aquacutter",
        "name": "Aqua Cutter",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "water"
    },
    "aquajet": {
        "accuracy": 100,
        "basePower": 40,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "aquajet",
        "name": "Aqua Jet",
        "pp": 20,
        "priority": 1,
        "secondary": None,
        "target": "normal",
        "type": "water"
    },
    "aquaring": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "aquaring",
        "name": "Aqua Ring",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "water",
        "volatileStatus": "aquaring"
    },
    "aquastep": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "contact": 1,
            "dance": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "aquastep",
        "name": "Aqua Step",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 100,
            "self": {
                "boosts": {
                    "speed": 1
                }
            }
        },
        "target": "normal",
        "type": "water"
    },
    "aquatail": {
        "accuracy": 90,
        "basePower": 90,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "aquatail",
        "name": "Aqua Tail",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "water"
    },
    "armorcannon": {
        "accuracy": 100,
        "basePower": 120,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "armorcannon",
        "name": "Armor Cannon",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {
            "boosts": {
                "defense": -1,
                "special-defense": -1
            }
        },
        "target": "normal",
        "type": "fire"
    },
    "armthrust": {
        "accuracy": 100,
        "basePower": 15,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "armthrust",
        "multihit": [
            2,
            5
        ],
        "name": "Arm Thrust",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "aromatherapy": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "distance": 1,
            "snatch": 1
        },
        "id": "aromatherapy",
        "name": "Aromatherapy",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "allyTeam",
        "type": "grass"
    },
    "aromaticmist": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "special-defense": 1
        },
        "category": "status",
        "flags": {
            "bypasssub": 1
        },
        "id": "aromaticmist",
        "name": "Aromatic Mist",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "adjacentAlly",
        "type": "fairy"
    },
    "assist": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "failcopycat": 1,
            "failencore": 1,
            "failinstruct": 1,
            "failmimic": 1,
            "noassist": 1,
            "nosleeptalk": 1
        },
        "id": "assist",
        "name": "Assist",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "assurance": {
        "accuracy": 100,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "assurance",
        "name": "Assurance",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark"
    },
    "astonish": {
        "accuracy": 100,
        "basePower": 30,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "astonish",
        "name": "Astonish",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "volatileStatus": "flinch"
        },
        "target": "normal",
        "type": "ghost"
    },
    "astralbarrage": {
        "accuracy": 100,
        "basePower": 120,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "astralbarrage",
        "name": "Astral Barrage",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "ghost"
    },
    "attackorder": {
        "accuracy": 100,
        "basePower": 90,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "attackorder",
        "name": "Attack Order",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "bug"
    },
    "attract": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "attract",
        "name": "Attract",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal",
        "volatileStatus": "attract"
    },
    "aurasphere": {
        "accuracy": True,
        "basePower": 80,
        "category": "special",
        "flags": {
            "bullet": 1,
            "distance": 1,
            "mirror": 1,
            "protect": 1,
            "pulse": 1
        },
        "id": "aurasphere",
        "name": "Aura Sphere",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "any",
        "type": "fighting"
    },
    "aurawheel": {
        "accuracy": 100,
        "basePower": 110,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "aurawheel",
        "name": "Aura Wheel",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 100,
            "self": {
                "boosts": {
                    "speed": 1
                }
            }
        },
        "target": "normal",
        "type": "electric"
    },
    "aurorabeam": {
        "accuracy": 100,
        "basePower": 65,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "aurorabeam",
        "name": "Aurora Beam",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "boosts": {
                "attack": -1
            },
            "chance": 10
        },
        "target": "normal",
        "type": "ice"
    },
    "auroraveil": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "auroraveil",
        "name": "Aurora Veil",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "side_conditions": "auroraveil",
        "target": "allySide",
        "type": "ice"
    },
    "autotomize": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "speed": 2
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "autotomize",
        "name": "Autotomize",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "steel"
    },
    "avalanche": {
        "accuracy": 100,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "avalanche",
        "name": "Avalanche",
        "pp": 10,
        "priority": -4,
        "secondary": None,
        "target": "normal",
        "type": "ice"
    },
    "axekick": {
        "accuracy": 90,
        "basePower": 120,
        "category": "physical",
        "crash": [
            1,
            2
        ],
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "axekick",
        "name": "Axe Kick",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "volatileStatus": "confusion"
        },
        "target": "normal",
        "type": "fighting"
    },
    "babydolleyes": {
        "accuracy": 100,
        "basePower": 0,
        "boosts": {
            "attack": -1
        },
        "category": "status",
        "flags": {
            "allyanim": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "babydolleyes",
        "name": "Baby-Doll Eyes",
        "pp": 30,
        "priority": 1,
        "secondary": None,
        "target": "normal",
        "type": "fairy"
    },
    "baddybad": {
        "accuracy": 95,
        "basePower": 80,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "baddybad",
        "name": "Baddy Bad",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "self": {
            "sideCondition": "reflect"
        },
        "target": "normal",
        "type": "dark"
    },
    "banefulbunker": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "failcopycat": 1,
            "noassist": 1
        },
        "id": "banefulbunker",
        "name": "Baneful Bunker",
        "pp": 10,
        "priority": 4,
        "secondary": None,
        "target": "self",
        "type": "poison",
        "volatileStatus": "banefulbunker"
    },
    "barbbarrage": {
        "accuracy": 100,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "barbbarrage",
        "name": "Barb Barrage",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 50,
            "status": "psn"
        },
        "target": "normal",
        "type": "poison"
    },
    "barrage": {
        "accuracy": 85,
        "basePower": 15,
        "category": "physical",
        "flags": {
            "bullet": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "barrage",
        "multihit": [
            2,
            5
        ],
        "name": "Barrage",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "barrier": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "defense": 2
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "barrier",
        "name": "Barrier",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "psychic"
    },
    "batonpass": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {},
        "id": "batonpass",
        "name": "Baton Pass",
        "pp": 40,
        "priority": 0,
        "secondary": None,
        "self": {},
        "target": "self",
        "type": "normal"
    },
    "beakblast": {
        "accuracy": 100,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "bullet": 1,
            "failcopycat": 1,
            "failinstruct": 1,
            "failmefirst": 1,
            "noassist": 1,
            "nosleeptalk": 1,
            "protect": 1
        },
        "id": "beakblast",
        "name": "Beak Blast",
        "pp": 15,
        "priority": -3,
        "secondary": None,
        "target": "normal",
        "type": "flying"
    },
    "beatup": {
        "accuracy": 100,
        "basePower": 0,
        "category": "physical",
        "flags": {
            "allyanim": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "beatup",
        "name": "Beat Up",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark"
    },
    "behemothbash": {
        "accuracy": 100,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "contact": 1,
            "failcopycat": 1,
            "failmimic": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "behemothbash",
        "name": "Behemoth Bash",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "steel"
    },
    "behemothblade": {
        "accuracy": 100,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "contact": 1,
            "failcopycat": 1,
            "failmimic": 1,
            "mirror": 1,
            "protect": 1,
            "slicing": 1
        },
        "id": "behemothblade",
        "name": "Behemoth Blade",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "steel"
    },
    "belch": {
        "accuracy": 90,
        "basePower": 120,
        "category": "special",
        "flags": {
            "failcopycat": 1,
            "failinstruct": 1,
            "failmefirst": 1,
            "failmimic": 1,
            "noassist": 1,
            "nosleeptalk": 1,
            "protect": 1
        },
        "id": "belch",
        "name": "Belch",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "poison"
    },
    "bellydrum": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "attack": 6
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "heal": [
            -1,
            2
        ],
        "heal_target": "self",
        "id": "bellydrum",
        "name": "Belly Drum",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "bestow": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "bypasssub": 1,
            "failcopycat": 1,
            "mirror": 1,
            "noassist": 1
        },
        "id": "bestow",
        "name": "Bestow",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "bide": {
        "accuracy": True,
        "basePower": 0,
        "category": "physical",
        "flags": {
            "contact": 1,
            "failinstruct": 1,
            "nosleeptalk": 1,
            "protect": 1
        },
        "id": "bide",
        "name": "Bide",
        "pp": 10,
        "priority": 1,
        "secondary": None,
        "target": "self",
        "type": "normal",
        "volatileStatus": "bide"
    },
    "bind": {
        "accuracy": 85,
        "basePower": 15,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "bind",
        "name": "Bind",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal",
        "volatileStatus": "partiallytrapped"
    },
    "bite": {
        "accuracy": 100,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "bite": 1,
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "bite",
        "name": "Bite",
        "pp": 25,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "volatileStatus": "flinch"
        },
        "target": "normal",
        "type": "dark"
    },
    "bitterblade": {
        "accuracy": 100,
        "basePower": 90,
        "category": "physical",
        "drain": [
            1,
            2
        ],
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "slicing": 1
        },
        "id": "bitterblade",
        "name": "Bitter Blade",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fire"
    },
    "bittermalice": {
        "accuracy": 100,
        "basePower": 75,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "bittermalice",
        "name": "Bitter Malice",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "attack": -1
            },
            "chance": 100
        },
        "target": "normal",
        "type": "ghost"
    },
    "blastburn": {
        "accuracy": 90,
        "basePower": 150,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "recharge": 1
        },
        "id": "blastburn",
        "name": "Blast Burn",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {
            "volatileStatus": "mustrecharge"
        },
        "target": "normal",
        "type": "fire"
    },
    "blazekick": {
        "accuracy": 90,
        "basePower": 85,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "blazekick",
        "name": "Blaze Kick",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "status": "brn"
        },
        "target": "normal",
        "type": "fire"
    },
    "blazingtorque": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "failcopycat": 1,
            "failencore": 1,
            "failinstruct": 1,
            "failmefirst": 1,
            "failmimic": 1,
            "noassist": 1,
            "nosleeptalk": 1,
            "protect": 1
        },
        "id": "blazingtorque",
        "name": "Blazing Torque",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "status": "brn"
        },
        "target": "normal",
        "type": "fire"
    },
    "bleakwindstorm": {
        "accuracy": 80,
        "basePower": 100,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "wind": 1
        },
        "id": "bleakwindstorm",
        "name": "Bleakwind Storm",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "speed": -1
            },
            "chance": 30
        },
        "target": "allAdjacentFoes",
        "type": "flying"
    },
    "blizzard": {
        "accuracy": 70,
        "basePower": 110,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "wind": 1
        },
        "id": "blizzard",
        "name": "Blizzard",
        "pp": 5,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "status": "frz"
        },
        "target": "allAdjacentFoes",
        "type": "ice"
    },
    "block": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "reflectable": 1
        },
        "id": "block",
        "name": "Block",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "blueflare": {
        "accuracy": 85,
        "basePower": 130,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "blueflare",
        "name": "Blue Flare",
        "pp": 5,
        "priority": 0,
        "secondary": {
            "chance": 20,
            "status": "brn"
        },
        "target": "normal",
        "type": "fire"
    },
    "bodypress": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "bodypress",
        "name": "Body Press",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "bodyslam": {
        "accuracy": 100,
        "basePower": 85,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "nonsky": 1,
            "protect": 1
        },
        "id": "bodyslam",
        "name": "Body Slam",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "status": "par"
        },
        "target": "normal",
        "type": "normal"
    },
    "boltbeak": {
        "accuracy": 100,
        "basePower": 85,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "boltbeak",
        "name": "Bolt Beak",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "electric"
    },
    "boltstrike": {
        "accuracy": 85,
        "basePower": 130,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "boltstrike",
        "name": "Bolt Strike",
        "pp": 5,
        "priority": 0,
        "secondary": {
            "chance": 20,
            "status": "par"
        },
        "target": "normal",
        "type": "electric"
    },
    "boneclub": {
        "accuracy": 85,
        "basePower": 65,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "boneclub",
        "name": "Bone Club",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "volatileStatus": "flinch"
        },
        "target": "normal",
        "type": "ground"
    },
    "bonemerang": {
        "accuracy": 90,
        "basePower": 50,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "bonemerang",
        "multihit": 2,
        "name": "Bonemerang",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ground"
    },
    "bonerush": {
        "accuracy": 90,
        "basePower": 25,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "bonerush",
        "multihit": [
            2,
            5
        ],
        "name": "Bone Rush",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ground"
    },
    "boomburst": {
        "accuracy": 100,
        "basePower": 140,
        "category": "special",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "sound": 1
        },
        "id": "boomburst",
        "name": "Boomburst",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacent",
        "type": "normal"
    },
    "bounce": {
        "accuracy": 85,
        "basePower": 85,
        "category": "physical",
        "flags": {
            "charge": 1,
            "contact": 1,
            "distance": 1,
            "failinstruct": 1,
            "gravity": 1,
            "mirror": 1,
            "noassist": 1,
            "nosleeptalk": 1,
            "protect": 1
        },
        "id": "bounce",
        "name": "Bounce",
        "pp": 5,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "status": "par"
        },
        "target": "any",
        "type": "flying"
    },
    "bouncybubble": {
        "accuracy": 100,
        "basePower": 60,
        "category": "special",
        "drain": [
            1,
            2
        ],
        "flags": {
            "heal": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "bouncybubble",
        "name": "Bouncy Bubble",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "water"
    },
    "branchpoke": {
        "accuracy": 100,
        "basePower": 40,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "branchpoke",
        "name": "Branch Poke",
        "pp": 40,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass"
    },
    "bravebird": {
        "accuracy": 100,
        "basePower": 120,
        "category": "physical",
        "flags": {
            "contact": 1,
            "distance": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "bravebird",
        "name": "Brave Bird",
        "pp": 15,
        "priority": 0,
        "recoil": [
            33,
            100
        ],
        "secondary": None,
        "target": "any",
        "type": "flying"
    },
    "breakingswipe": {
        "accuracy": 100,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "breakingswipe",
        "name": "Breaking Swipe",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "boosts": {
                "attack": -1
            },
            "chance": 100
        },
        "target": "allAdjacentFoes",
        "type": "dragon"
    },
    "brickbreak": {
        "accuracy": 100,
        "basePower": 75,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "brickbreak",
        "name": "Brick Break",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "brine": {
        "accuracy": 100,
        "basePower": 65,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "brine",
        "name": "Brine",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "water"
    },
    "brutalswing": {
        "accuracy": 100,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "brutalswing",
        "name": "Brutal Swing",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacent",
        "type": "dark"
    },
    "bubble": {
        "accuracy": 100,
        "basePower": 40,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "bubble",
        "name": "Bubble",
        "pp": 30,
        "priority": 0,
        "secondary": {
            "boosts": {
                "speed": -1
            },
            "chance": 10
        },
        "target": "allAdjacentFoes",
        "type": "water"
    },
    "bubblebeam": {
        "accuracy": 100,
        "basePower": 65,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "bubblebeam",
        "name": "Bubble Beam",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "boosts": {
                "speed": -1
            },
            "chance": 10
        },
        "target": "normal",
        "type": "water"
    },
    "bugbite": {
        "accuracy": 100,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "bugbite",
        "name": "Bug Bite",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "bug"
    },
    "bugbuzz": {
        "accuracy": 100,
        "basePower": 90,
        "category": "special",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "sound": 1
        },
        "id": "bugbuzz",
        "name": "Bug Buzz",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "special-defense": -1
            },
            "chance": 10
        },
        "target": "normal",
        "type": "bug"
    },
    "bulkup": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "attack": 1,
            "defense": 1
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "bulkup",
        "name": "Bulk Up",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "fighting"
    },
    "bulldoze": {
        "accuracy": 100,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "nonsky": 1,
            "protect": 1
        },
        "id": "bulldoze",
        "name": "Bulldoze",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "boosts": {
                "speed": -1
            },
            "chance": 100
        },
        "target": "allAdjacent",
        "type": "ground"
    },
    "bulletpunch": {
        "accuracy": 100,
        "basePower": 40,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "punch": 1
        },
        "id": "bulletpunch",
        "name": "Bullet Punch",
        "pp": 30,
        "priority": 1,
        "secondary": None,
        "target": "normal",
        "type": "steel"
    },
    "bulletseed": {
        "accuracy": 100,
        "basePower": 25,
        "category": "physical",
        "flags": {
            "bullet": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "bulletseed",
        "multihit": [
            2,
            5
        ],
        "name": "Bullet Seed",
        "pp": 30,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass"
    },
    "burningjealousy": {
        "accuracy": 100,
        "basePower": 70,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "burningjealousy",
        "name": "Burning Jealousy",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "fire"
    },
    "burnup": {
        "accuracy": 100,
        "basePower": 130,
        "category": "special",
        "flags": {
            "defrost": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "burnup",
        "name": "Burn Up",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {},
        "target": "normal",
        "type": "fire"
    },
    "buzzybuzz": {
        "accuracy": 100,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "buzzybuzz",
        "name": "Buzzy Buzz",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "chance": 100,
            "status": "par"
        },
        "target": "normal",
        "type": "electric"
    },
    "calmmind": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "special-attack": 1,
            "special-defense": 1
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "calmmind",
        "name": "Calm Mind",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "psychic"
    },
    "camouflage": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "camouflage",
        "name": "Camouflage",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "captivate": {
        "accuracy": 100,
        "basePower": 0,
        "boosts": {
            "special-attack": -2
        },
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "captivate",
        "name": "Captivate",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "normal"
    },
    "ceaselessedge": {
        "accuracy": 90,
        "basePower": 65,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "slicing": 1
        },
        "id": "ceaselessedge",
        "name": "Ceaseless Edge",
        "pp": 15,
        "priority": 0,
        "secondary": {},
        "side_conditions": "spikes",
        "target": "normal",
        "type": "dark"
    },
    "celebrate": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "failcopycat": 1,
            "failinstruct": 1,
            "failmimic": 1,
            "noassist": 1,
            "nosleeptalk": 1
        },
        "id": "celebrate",
        "name": "Celebrate",
        "pp": 40,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "charge": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "special-defense": 1
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "charge",
        "name": "Charge",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "electric",
        "volatileStatus": "charge"
    },
    "chargebeam": {
        "accuracy": 90,
        "basePower": 50,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "chargebeam",
        "name": "Charge Beam",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 70,
            "self": {
                "boosts": {
                    "special-attack": 1
                }
            }
        },
        "target": "normal",
        "type": "electric"
    },
    "charm": {
        "accuracy": 100,
        "basePower": 0,
        "boosts": {
            "attack": -2
        },
        "category": "status",
        "flags": {
            "allyanim": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "charm",
        "name": "Charm",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fairy"
    },
    "chatter": {
        "accuracy": 100,
        "basePower": 65,
        "category": "special",
        "flags": {
            "bypasssub": 1,
            "distance": 1,
            "failcopycat": 1,
            "failinstruct": 1,
            "failmimic": 1,
            "mirror": 1,
            "noassist": 1,
            "nosleeptalk": 1,
            "protect": 1,
            "sound": 1
        },
        "id": "chatter",
        "name": "Chatter",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "chance": 100,
            "volatileStatus": "confusion"
        },
        "target": "any",
        "type": "flying"
    },
    "chillingwater": {
        "accuracy": 100,
        "basePower": 50,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "chillingwater",
        "name": "Chilling Water",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "boosts": {
                "attack": -1
            },
            "chance": 100
        },
        "target": "normal",
        "type": "water"
    },
    "chillyreception": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {},
        "id": "chillyreception",
        "name": "Chilly Reception",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "all",
        "type": "ice",
        "weather": "snow"
    },
    "chipaway": {
        "accuracy": 100,
        "basePower": 70,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "chipaway",
        "name": "Chip Away",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "chloroblast": {
        "accuracy": 95,
        "basePower": 150,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "heal": [
            -1,
            2
        ],
        "heal_target": "self",
        "id": "chloroblast",
        "name": "Chloroblast",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass"
    },
    "circlethrow": {
        "accuracy": 90,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "contact": 1,
            "drag": 1,
            "failcopycat": 1,
            "mirror": 1,
            "noassist": 1,
            "protect": 1
        },
        "id": "circlethrow",
        "name": "Circle Throw",
        "pp": 10,
        "priority": -6,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "clamp": {
        "accuracy": 85,
        "basePower": 35,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "clamp",
        "name": "Clamp",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "water",
        "volatileStatus": "partiallytrapped"
    },
    "clangingscales": {
        "accuracy": 100,
        "basePower": 110,
        "category": "special",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "sound": 1
        },
        "id": "clangingscales",
        "name": "Clanging Scales",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {
            "boosts": {
                "defense": -1
            }
        },
        "target": "allAdjacentFoes",
        "type": "dragon"
    },
    "clangoroussoul": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "dance": 1,
            "snatch": 1,
            "sound": 1
        },
        "id": "clangoroussoul",
        "name": "Clangorous Soul",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "dragon"
    },
    "clearsmog": {
        "accuracy": True,
        "basePower": 50,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "clearsmog",
        "name": "Clear Smog",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "poison"
    },
    "closecombat": {
        "accuracy": 100,
        "basePower": 120,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "closecombat",
        "name": "Close Combat",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {
            "boosts": {
                "defense": -1,
                "special-defense": -1
            }
        },
        "target": "normal",
        "type": "fighting"
    },
    "coaching": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "attack": 1,
            "defense": 1
        },
        "category": "status",
        "flags": {
            "allyanim": 1,
            "bypasssub": 1
        },
        "id": "coaching",
        "name": "Coaching",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "adjacentAlly",
        "type": "fighting"
    },
    "coil": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "accuracy": 1,
            "attack": 1,
            "defense": 1
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "coil",
        "name": "Coil",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "poison"
    },
    "collisioncourse": {
        "accuracy": 100,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "collisioncourse",
        "name": "Collision Course",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "combattorque": {
        "accuracy": 100,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "failcopycat": 1,
            "failencore": 1,
            "failinstruct": 1,
            "failmefirst": 1,
            "failmimic": 1,
            "noassist": 1,
            "nosleeptalk": 1,
            "protect": 1
        },
        "id": "combattorque",
        "name": "Combat Torque",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "status": "par"
        },
        "target": "normal",
        "type": "fighting"
    },
    "cometpunch": {
        "accuracy": 85,
        "basePower": 18,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "punch": 1
        },
        "id": "cometpunch",
        "multihit": [
            2,
            5
        ],
        "name": "Comet Punch",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "comeuppance": {
        "accuracy": 100,
        "basePower": 0,
        "category": "physical",
        "flags": {
            "contact": 1,
            "failmefirst": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "comeuppance",
        "name": "Comeuppance",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "scripted",
        "type": "dark"
    },
    "confide": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "special-attack": -1
        },
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "reflectable": 1,
            "sound": 1
        },
        "id": "confide",
        "name": "Confide",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "confuseray": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "confuseray",
        "name": "Confuse Ray",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ghost",
        "volatileStatus": "confusion"
    },
    "confusion": {
        "accuracy": 100,
        "basePower": 50,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "confusion",
        "name": "Confusion",
        "pp": 25,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "volatileStatus": "confusion"
        },
        "target": "normal",
        "type": "psychic"
    },
    "constrict": {
        "accuracy": 100,
        "basePower": 10,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "constrict",
        "name": "Constrict",
        "pp": 35,
        "priority": 0,
        "secondary": {
            "boosts": {
                "speed": -1
            },
            "chance": 10
        },
        "target": "normal",
        "type": "normal"
    },
    "conversion": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "conversion",
        "name": "Conversion",
        "pp": 30,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "conversion2": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1
        },
        "id": "conversion2",
        "name": "Conversion 2",
        "pp": 30,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "copycat": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "failcopycat": 1,
            "failencore": 1,
            "failinstruct": 1,
            "failmimic": 1,
            "noassist": 1,
            "nosleeptalk": 1
        },
        "id": "copycat",
        "name": "Copycat",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "coreenforcer": {
        "accuracy": 100,
        "basePower": 100,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "coreenforcer",
        "name": "Core Enforcer",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "dragon"
    },
    "corrosivegas": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "corrosivegas",
        "name": "Corrosive Gas",
        "pp": 40,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacent",
        "type": "poison"
    },
    "cosmicpower": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "defense": 1,
            "special-defense": 1
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "cosmicpower",
        "name": "Cosmic Power",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "psychic"
    },
    "cottonguard": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "defense": 3
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "cottonguard",
        "name": "Cotton Guard",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "grass"
    },
    "cottonspore": {
        "accuracy": 100,
        "basePower": 0,
        "boosts": {
            "speed": -2
        },
        "category": "status",
        "flags": {
            "mirror": 1,
            "powder": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "cottonspore",
        "name": "Cotton Spore",
        "pp": 40,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "grass"
    },
    "counter": {
        "accuracy": 100,
        "basePower": 0,
        "category": "physical",
        "flags": {
            "contact": 1,
            "failcopycat": 1,
            "failmefirst": 1,
            "noassist": 1,
            "protect": 1
        },
        "id": "counter",
        "name": "Counter",
        "pp": 20,
        "priority": -5,
        "secondary": None,
        "target": "scripted",
        "type": "fighting"
    },
    "courtchange": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1
        },
        "id": "courtchange",
        "name": "Court Change",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "all",
        "type": "normal"
    },
    "covet": {
        "accuracy": 100,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "contact": 1,
            "failcopycat": 1,
            "failmefirst": 1,
            "mirror": 1,
            "noassist": 1,
            "protect": 1
        },
        "id": "covet",
        "name": "Covet",
        "pp": 25,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "crabhammer": {
        "accuracy": 90,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "crabhammer",
        "name": "Crabhammer",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "water"
    },
    "craftyshield": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {},
        "id": "craftyshield",
        "name": "Crafty Shield",
        "pp": 10,
        "priority": 3,
        "secondary": None,
        "side_conditions": "craftyshield",
        "target": "allySide",
        "type": "fairy"
    },
    "crosschop": {
        "accuracy": 80,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "crosschop",
        "name": "Cross Chop",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "crosspoison": {
        "accuracy": 100,
        "basePower": 70,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "slicing": 1
        },
        "id": "crosspoison",
        "name": "Cross Poison",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "status": "psn"
        },
        "target": "normal",
        "type": "poison"
    },
    "crunch": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "bite": 1,
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "crunch",
        "name": "Crunch",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "boosts": {
                "defense": -1
            },
            "chance": 20
        },
        "target": "normal",
        "type": "dark"
    },
    "crushclaw": {
        "accuracy": 95,
        "basePower": 75,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "crushclaw",
        "name": "Crush Claw",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "defense": -1
            },
            "chance": 50
        },
        "target": "normal",
        "type": "normal"
    },
    "crushgrip": {
        "accuracy": 100,
        "basePower": 0,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "crushgrip",
        "name": "Crush Grip",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "curse": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "attack": 1,
            "defense": 1,
            "speed": -1
        },
        "category": "status",
        "flags": {
            "bypasssub": 1
        },
        "id": "curse",
        "name": "Curse",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ghost",
        "volatileStatus": "curse"
    },
    "cut": {
        "accuracy": 95,
        "basePower": 50,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "slicing": 1
        },
        "id": "cut",
        "name": "Cut",
        "pp": 30,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "darkestlariat": {
        "accuracy": 100,
        "basePower": 85,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "darkestlariat",
        "name": "Darkest Lariat",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark"
    },
    "darkpulse": {
        "accuracy": 100,
        "basePower": 80,
        "category": "special",
        "flags": {
            "distance": 1,
            "mirror": 1,
            "protect": 1,
            "pulse": 1
        },
        "id": "darkpulse",
        "name": "Dark Pulse",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "chance": 20,
            "volatileStatus": "flinch"
        },
        "target": "any",
        "type": "dark"
    },
    "darkvoid": {
        "accuracy": 50,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "darkvoid",
        "name": "Dark Void",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "status": "slp",
        "target": "allAdjacentFoes",
        "type": "dark"
    },
    "dazzlinggleam": {
        "accuracy": 100,
        "basePower": 80,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "dazzlinggleam",
        "name": "Dazzling Gleam",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "fairy"
    },
    "decorate": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "attack": 2,
            "special-attack": 2
        },
        "category": "status",
        "flags": {
            "allyanim": 1
        },
        "id": "decorate",
        "name": "Decorate",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fairy"
    },
    "defendorder": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "defense": 1,
            "special-defense": 1
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "defendorder",
        "name": "Defend Order",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "bug"
    },
    "defensecurl": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "defense": 1
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "defensecurl",
        "name": "Defense Curl",
        "pp": 40,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal",
        "volatileStatus": "defensecurl"
    },
    "defog": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "evasion": -1
        },
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "defog",
        "name": "Defog",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "flying"
    },
    "destinybond": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "failcopycat": 1,
            "noassist": 1
        },
        "id": "destinybond",
        "name": "Destiny Bond",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "ghost",
        "volatileStatus": "destinybond"
    },
    "detect": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "failcopycat": 1,
            "noassist": 1
        },
        "id": "detect",
        "name": "Detect",
        "pp": 5,
        "priority": 4,
        "secondary": None,
        "target": "self",
        "type": "fighting",
        "volatileStatus": "protect"
    },
    "diamondstorm": {
        "accuracy": 95,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "diamondstorm",
        "name": "Diamond Storm",
        "pp": 5,
        "priority": 0,
        "secondary": {
            "chance": 50,
            "self": {
                "boosts": {
                    "defense": 2
                }
            }
        },
        "target": "allAdjacentFoes",
        "type": "rock"
    },
    "dig": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "charge": 1,
            "contact": 1,
            "failinstruct": 1,
            "mirror": 1,
            "noassist": 1,
            "nonsky": 1,
            "nosleeptalk": 1,
            "protect": 1
        },
        "id": "dig",
        "name": "Dig",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ground"
    },
    "direclaw": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "direclaw",
        "name": "Dire Claw",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "poison"
    },
    "disable": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "disable",
        "name": "Disable",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal",
        "volatileStatus": "disable"
    },
    "disarmingvoice": {
        "accuracy": True,
        "basePower": 40,
        "category": "special",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "sound": 1
        },
        "id": "disarmingvoice",
        "name": "Disarming Voice",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "fairy"
    },
    "discharge": {
        "accuracy": 100,
        "basePower": 80,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "discharge",
        "name": "Discharge",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "status": "par"
        },
        "target": "allAdjacent",
        "type": "electric"
    },
    "dive": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "allyanim": 1,
            "charge": 1,
            "contact": 1,
            "failinstruct": 1,
            "mirror": 1,
            "noassist": 1,
            "nonsky": 1,
            "nosleeptalk": 1,
            "protect": 1
        },
        "id": "dive",
        "name": "Dive",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "water"
    },
    "dizzypunch": {
        "accuracy": 100,
        "basePower": 70,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "punch": 1
        },
        "id": "dizzypunch",
        "name": "Dizzy Punch",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 20,
            "volatileStatus": "confusion"
        },
        "target": "normal",
        "type": "normal"
    },
    "doodle": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {},
        "id": "doodle",
        "name": "Doodle",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "adjacentFoe",
        "type": "normal"
    },
    "doomdesire": {
        "accuracy": 100,
        "basePower": 140,
        "category": "special",
        "flags": {
            "futuremove": 1
        },
        "id": "doomdesire",
        "name": "Doom Desire",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "steel"
    },
    "doubleedge": {
        "accuracy": 100,
        "basePower": 120,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "doubleedge",
        "name": "Double-Edge",
        "pp": 15,
        "priority": 0,
        "recoil": [
            1,
            3
        ],
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "doublehit": {
        "accuracy": 90,
        "basePower": 35,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "doublehit",
        "multihit": 2,
        "name": "Double Hit",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "doubleironbash": {
        "accuracy": 100,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "punch": 1
        },
        "id": "doubleironbash",
        "multihit": 2,
        "name": "Double Iron Bash",
        "pp": 5,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "volatileStatus": "flinch"
        },
        "target": "normal",
        "type": "steel"
    },
    "doublekick": {
        "accuracy": 100,
        "basePower": 30,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "doublekick",
        "multihit": 2,
        "name": "Double Kick",
        "pp": 30,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "doubleshock": {
        "accuracy": 100,
        "basePower": 120,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "doubleshock",
        "name": "Double Shock",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {},
        "target": "normal",
        "type": "electric"
    },
    "doubleslap": {
        "accuracy": 85,
        "basePower": 15,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "doubleslap",
        "multihit": [
            2,
            5
        ],
        "name": "Double Slap",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "doubleteam": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "evasion": 1
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "doubleteam",
        "name": "Double Team",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "dracometeor": {
        "accuracy": 90,
        "basePower": 130,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "dracometeor",
        "name": "Draco Meteor",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {
            "boosts": {
                "special-attack": -2
            }
        },
        "target": "normal",
        "type": "dragon"
    },
    "dragonascent": {
        "accuracy": 100,
        "basePower": 120,
        "category": "physical",
        "flags": {
            "contact": 1,
            "distance": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "dragonascent",
        "name": "Dragon Ascent",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {
            "boosts": {
                "defense": -1,
                "special-defense": -1
            }
        },
        "target": "any",
        "type": "flying"
    },
    "dragonbreath": {
        "accuracy": 100,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "dragonbreath",
        "name": "Dragon Breath",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "status": "par"
        },
        "target": "normal",
        "type": "dragon"
    },
    "dragonclaw": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "dragonclaw",
        "name": "Dragon Claw",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dragon"
    },
    "dragondance": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "attack": 1,
            "speed": 1
        },
        "category": "status",
        "flags": {
            "dance": 1,
            "snatch": 1
        },
        "id": "dragondance",
        "name": "Dragon Dance",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "dragon"
    },
    "dragondarts": {
        "accuracy": 100,
        "basePower": 50,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "noparentalbond": 1,
            "protect": 1
        },
        "id": "dragondarts",
        "multihit": 2,
        "name": "Dragon Darts",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dragon"
    },
    "dragonenergy": {
        "accuracy": 100,
        "basePower": 150,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "dragonenergy",
        "name": "Dragon Energy",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "dragon"
    },
    "dragonhammer": {
        "accuracy": 100,
        "basePower": 90,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "dragonhammer",
        "name": "Dragon Hammer",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dragon"
    },
    "dragonpulse": {
        "accuracy": 100,
        "basePower": 85,
        "category": "special",
        "flags": {
            "distance": 1,
            "mirror": 1,
            "protect": 1,
            "pulse": 1
        },
        "id": "dragonpulse",
        "name": "Dragon Pulse",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "any",
        "type": "dragon"
    },
    "dragonrage": {
        "accuracy": 100,
        "basePower": 0,
        "category": "special",
        "damage": 40,
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "dragonrage",
        "name": "Dragon Rage",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dragon"
    },
    "dragonrush": {
        "accuracy": 75,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "dragonrush",
        "name": "Dragon Rush",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 20,
            "volatileStatus": "flinch"
        },
        "target": "normal",
        "type": "dragon"
    },
    "dragontail": {
        "accuracy": 90,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "contact": 1,
            "drag": 1,
            "failcopycat": 1,
            "mirror": 1,
            "noassist": 1,
            "protect": 1
        },
        "id": "dragontail",
        "name": "Dragon Tail",
        "pp": 10,
        "priority": -6,
        "secondary": None,
        "target": "normal",
        "type": "dragon"
    },
    "drainingkiss": {
        "accuracy": 100,
        "basePower": 50,
        "category": "special",
        "drain": [
            3,
            4
        ],
        "flags": {
            "contact": 1,
            "heal": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "drainingkiss",
        "name": "Draining Kiss",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fairy"
    },
    "drainpunch": {
        "accuracy": 100,
        "basePower": 75,
        "category": "physical",
        "drain": [
            1,
            2
        ],
        "flags": {
            "contact": 1,
            "heal": 1,
            "mirror": 1,
            "protect": 1,
            "punch": 1
        },
        "id": "drainpunch",
        "name": "Drain Punch",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "dreameater": {
        "accuracy": 100,
        "basePower": 100,
        "category": "special",
        "drain": [
            1,
            2
        ],
        "flags": {
            "heal": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "dreameater",
        "name": "Dream Eater",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "drillpeck": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "contact": 1,
            "distance": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "drillpeck",
        "name": "Drill Peck",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "any",
        "type": "flying"
    },
    "drillrun": {
        "accuracy": 95,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "drillrun",
        "name": "Drill Run",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ground"
    },
    "drumbeating": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "drumbeating",
        "name": "Drum Beating",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "speed": -1
            },
            "chance": 100
        },
        "target": "normal",
        "type": "grass"
    },
    "dualchop": {
        "accuracy": 90,
        "basePower": 40,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "dualchop",
        "multihit": 2,
        "name": "Dual Chop",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dragon"
    },
    "dualwingbeat": {
        "accuracy": 90,
        "basePower": 40,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "dualwingbeat",
        "multihit": 2,
        "name": "Dual Wingbeat",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "flying"
    },
    "dynamaxcannon": {
        "accuracy": 100,
        "basePower": 100,
        "category": "special",
        "flags": {
            "failcopycat": 1,
            "failencore": 1,
            "failinstruct": 1,
            "failmimic": 1,
            "noparentalbond": 1,
            "nosleeptalk": 1,
            "protect": 1
        },
        "id": "dynamaxcannon",
        "name": "Dynamax Cannon",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dragon"
    },
    "dynamicpunch": {
        "accuracy": 50,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "punch": 1
        },
        "id": "dynamicpunch",
        "name": "Dynamic Punch",
        "pp": 5,
        "priority": 0,
        "secondary": {
            "chance": 100,
            "volatileStatus": "confusion"
        },
        "target": "normal",
        "type": "fighting"
    },
    "earthpower": {
        "accuracy": 100,
        "basePower": 90,
        "category": "special",
        "flags": {
            "mirror": 1,
            "nonsky": 1,
            "protect": 1
        },
        "id": "earthpower",
        "name": "Earth Power",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "special-defense": -1
            },
            "chance": 10
        },
        "target": "normal",
        "type": "ground"
    },
    "earthquake": {
        "accuracy": 100,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "nonsky": 1,
            "protect": 1
        },
        "id": "earthquake",
        "name": "Earthquake",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacent",
        "type": "ground"
    },
    "echoedvoice": {
        "accuracy": 100,
        "basePower": 40,
        "category": "special",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "sound": 1
        },
        "id": "echoedvoice",
        "name": "Echoed Voice",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "eerieimpulse": {
        "accuracy": 100,
        "basePower": 0,
        "boosts": {
            "special-attack": -2
        },
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "eerieimpulse",
        "name": "Eerie Impulse",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "electric"
    },
    "eeriespell": {
        "accuracy": 100,
        "basePower": 80,
        "category": "special",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "sound": 1
        },
        "id": "eeriespell",
        "name": "Eerie Spell",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "eggbomb": {
        "accuracy": 75,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "bullet": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "eggbomb",
        "name": "Egg Bomb",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "electricterrain": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "nonsky": 1
        },
        "id": "electricterrain",
        "name": "Electric Terrain",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "all",
        "terrain": "electricterrain",
        "type": "electric"
    },
    "electrify": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "electrify",
        "name": "Electrify",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "electric",
        "volatileStatus": "electrify"
    },
    "electroball": {
        "accuracy": 100,
        "basePower": 0,
        "category": "special",
        "flags": {
            "bullet": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "electroball",
        "name": "Electro Ball",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "electric"
    },
    "electrodrift": {
        "accuracy": 100,
        "basePower": 100,
        "category": "special",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "electrodrift",
        "name": "Electro Drift",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "electric"
    },
    "electroweb": {
        "accuracy": 95,
        "basePower": 55,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "electroweb",
        "name": "Electroweb",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "boosts": {
                "speed": -1
            },
            "chance": 100
        },
        "target": "allAdjacentFoes",
        "type": "electric"
    },
    "embargo": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "embargo",
        "name": "Embargo",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark",
        "volatileStatus": "embargo"
    },
    "ember": {
        "accuracy": 100,
        "basePower": 40,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "ember",
        "name": "Ember",
        "pp": 25,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "status": "brn"
        },
        "target": "normal",
        "type": "fire"
    },
    "encore": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "failencore": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "encore",
        "name": "Encore",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal",
        "volatileStatus": "encore"
    },
    "endeavor": {
        "accuracy": 100,
        "basePower": 0,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "noparentalbond": 1,
            "protect": 1
        },
        "id": "endeavor",
        "name": "Endeavor",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "endure": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "failcopycat": 1,
            "noassist": 1
        },
        "id": "endure",
        "name": "Endure",
        "pp": 10,
        "priority": 4,
        "secondary": None,
        "target": "self",
        "type": "normal",
        "volatileStatus": "endure"
    },
    "energyball": {
        "accuracy": 100,
        "basePower": 90,
        "category": "special",
        "flags": {
            "bullet": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "energyball",
        "name": "Energy Ball",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "special-defense": -1
            },
            "chance": 10
        },
        "target": "normal",
        "type": "grass"
    },
    "entrainment": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "entrainment",
        "name": "Entrainment",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "eruption": {
        "accuracy": 100,
        "basePower": 150,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "eruption",
        "name": "Eruption",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "fire"
    },
    "esperwing": {
        "accuracy": 100,
        "basePower": 80,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "esperwing",
        "name": "Esper Wing",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 100,
            "self": {
                "boosts": {
                    "speed": 1
                }
            }
        },
        "target": "normal",
        "type": "psychic"
    },
    "eternabeam": {
        "accuracy": 90,
        "basePower": 160,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "recharge": 1
        },
        "id": "eternabeam",
        "name": "Eternabeam",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {
            "volatileStatus": "mustrecharge"
        },
        "target": "normal",
        "type": "dragon"
    },
    "expandingforce": {
        "accuracy": 100,
        "basePower": 80,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "expandingforce",
        "name": "Expanding Force",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "explosion": {
        "accuracy": 100,
        "basePower": 250,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "noparentalbond": 1,
            "protect": 1
        },
        "heal": [
            -1,
            1
        ],
        "heal_target": "self",
        "id": "explosion",
        "name": "Explosion",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacent",
        "type": "normal"
    },
    "extrasensory": {
        "accuracy": 100,
        "basePower": 80,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "extrasensory",
        "name": "Extrasensory",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "volatileStatus": "flinch"
        },
        "target": "normal",
        "type": "psychic"
    },
    "extremespeed": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "extremespeed",
        "name": "Extreme Speed",
        "pp": 5,
        "priority": 2,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "facade": {
        "accuracy": 100,
        "basePower": 70,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "facade",
        "name": "Facade",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "fairylock": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "mirror": 1
        },
        "id": "fairylock",
        "name": "Fairy Lock",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "all",
        "type": "fairy"
    },
    "fairywind": {
        "accuracy": 100,
        "basePower": 40,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "wind": 1
        },
        "id": "fairywind",
        "name": "Fairy Wind",
        "pp": 30,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fairy"
    },
    "fakeout": {
        "accuracy": 100,
        "basePower": 40,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "fakeout",
        "name": "Fake Out",
        "pp": 10,
        "priority": 3,
        "secondary": {
            "chance": 0,
            "volatileStatus": "flinch"
        },
        "target": "normal",
        "type": "normal"
    },
    "faketears": {
        "accuracy": 100,
        "basePower": 0,
        "boosts": {
            "special-defense": -2
        },
        "category": "status",
        "flags": {
            "allyanim": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "faketears",
        "name": "Fake Tears",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark"
    },
    "falsesurrender": {
        "accuracy": True,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "falsesurrender",
        "name": "False Surrender",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark"
    },
    "falseswipe": {
        "accuracy": 100,
        "basePower": 40,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "falseswipe",
        "name": "False Swipe",
        "pp": 40,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "featherdance": {
        "accuracy": 100,
        "basePower": 0,
        "boosts": {
            "attack": -2
        },
        "category": "status",
        "flags": {
            "allyanim": 1,
            "dance": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "featherdance",
        "name": "Feather Dance",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "flying"
    },
    "feint": {
        "accuracy": 100,
        "basePower": 30,
        "category": "physical",
        "flags": {
            "failcopycat": 1,
            "mirror": 1,
            "noassist": 1
        },
        "id": "feint",
        "name": "Feint",
        "pp": 10,
        "priority": 2,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "feintattack": {
        "accuracy": True,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "feintattack",
        "name": "Feint Attack",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark"
    },
    "fellstinger": {
        "accuracy": 100,
        "basePower": 50,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "fellstinger",
        "name": "Fell Stinger",
        "pp": 25,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "bug"
    },
    "fierydance": {
        "accuracy": 100,
        "basePower": 80,
        "category": "special",
        "flags": {
            "dance": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "fierydance",
        "name": "Fiery Dance",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 50,
            "self": {
                "boosts": {
                    "special-attack": 1
                }
            }
        },
        "target": "normal",
        "type": "fire"
    },
    "fierywrath": {
        "accuracy": 100,
        "basePower": 90,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "fierywrath",
        "name": "Fiery Wrath",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 20,
            "volatileStatus": "flinch"
        },
        "target": "allAdjacentFoes",
        "type": "dark"
    },
    "filletaway": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "filletaway",
        "name": "Fillet Away",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "finalgambit": {
        "accuracy": 100,
        "basePower": 0,
        "category": "special",
        "flags": {
            "noparentalbond": 1,
            "protect": 1
        },
        "heal": [
            -1,
            1
        ],
        "heal_target": "self",
        "id": "finalgambit",
        "name": "Final Gambit",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "fireblast": {
        "accuracy": 85,
        "basePower": 110,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "fireblast",
        "name": "Fire Blast",
        "pp": 5,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "status": "brn"
        },
        "target": "normal",
        "type": "fire"
    },
    "firefang": {
        "accuracy": 95,
        "basePower": 65,
        "category": "physical",
        "flags": {
            "bite": 1,
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "firefang",
        "name": "Fire Fang",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fire"
    },
    "firelash": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "firelash",
        "name": "Fire Lash",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "boosts": {
                "defense": -1
            },
            "chance": 100
        },
        "target": "normal",
        "type": "fire"
    },
    "firepledge": {
        "accuracy": 100,
        "basePower": 80,
        "category": "special",
        "flags": {
            "mirror": 1,
            "nonsky": 1,
            "pledgecombo": 1,
            "protect": 1
        },
        "id": "firepledge",
        "name": "Fire Pledge",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fire"
    },
    "firepunch": {
        "accuracy": 100,
        "basePower": 75,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "punch": 1
        },
        "id": "firepunch",
        "name": "Fire Punch",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "status": "brn"
        },
        "target": "normal",
        "type": "fire"
    },
    "firespin": {
        "accuracy": 85,
        "basePower": 35,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "firespin",
        "name": "Fire Spin",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fire",
        "volatileStatus": "partiallytrapped"
    },
    "firstimpression": {
        "accuracy": 100,
        "basePower": 90,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "firstimpression",
        "name": "First Impression",
        "pp": 10,
        "priority": 2,
        "secondary": None,
        "target": "normal",
        "type": "bug"
    },
    "fishiousrend": {
        "accuracy": 100,
        "basePower": 85,
        "category": "physical",
        "flags": {
            "bite": 1,
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "fishiousrend",
        "name": "Fishious Rend",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "water"
    },
    "fissure": {
        "accuracy": 30,
        "basePower": 0,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "nonsky": 1,
            "protect": 1
        },
        "id": "fissure",
        "name": "Fissure",
        "ohko": True,
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ground"
    },
    "flail": {
        "accuracy": 100,
        "basePower": 0,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "flail",
        "name": "Flail",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "flameburst": {
        "accuracy": 100,
        "basePower": 70,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "flameburst",
        "name": "Flame Burst",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fire"
    },
    "flamecharge": {
        "accuracy": 100,
        "basePower": 50,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "flamecharge",
        "name": "Flame Charge",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "chance": 100,
            "self": {
                "boosts": {
                    "speed": 1
                }
            }
        },
        "target": "normal",
        "type": "fire"
    },
    "flamethrower": {
        "accuracy": 100,
        "basePower": 90,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "flamethrower",
        "name": "Flamethrower",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "status": "brn"
        },
        "target": "normal",
        "type": "fire"
    },
    "flamewheel": {
        "accuracy": 100,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "contact": 1,
            "defrost": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "flamewheel",
        "name": "Flame Wheel",
        "pp": 25,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "status": "brn"
        },
        "target": "normal",
        "type": "fire"
    },
    "flareblitz": {
        "accuracy": 100,
        "basePower": 120,
        "category": "physical",
        "flags": {
            "contact": 1,
            "defrost": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "flareblitz",
        "name": "Flare Blitz",
        "pp": 15,
        "priority": 0,
        "recoil": [
            1,
            3
        ],
        "secondary": {
            "chance": 10,
            "status": "brn"
        },
        "target": "normal",
        "type": "fire"
    },
    "flash": {
        "accuracy": 100,
        "basePower": 0,
        "boosts": {
            "accuracy": -1
        },
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "flash",
        "name": "Flash",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "flashcannon": {
        "accuracy": 100,
        "basePower": 80,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "flashcannon",
        "name": "Flash Cannon",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "special-defense": -1
            },
            "chance": 10
        },
        "target": "normal",
        "type": "steel"
    },
    "flatter": {
        "accuracy": 100,
        "basePower": 0,
        "boosts": {
            "special-attack": 1
        },
        "category": "status",
        "flags": {
            "allyanim": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "flatter",
        "name": "Flatter",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark",
        "volatileStatus": "confusion"
    },
    "fleurcannon": {
        "accuracy": 90,
        "basePower": 130,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "fleurcannon",
        "name": "Fleur Cannon",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {
            "boosts": {
                "special-attack": -2
            }
        },
        "target": "normal",
        "type": "fairy"
    },
    "fling": {
        "accuracy": 100,
        "basePower": 0,
        "category": "physical",
        "flags": {
            "allyanim": 1,
            "mirror": 1,
            "noparentalbond": 1,
            "protect": 1
        },
        "id": "fling",
        "name": "Fling",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark"
    },
    "flipturn": {
        "accuracy": 100,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "flipturn",
        "name": "Flip Turn",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "water"
    },
    "floatyfall": {
        "accuracy": 95,
        "basePower": 90,
        "category": "physical",
        "flags": {
            "contact": 1,
            "gravity": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "floatyfall",
        "name": "Floaty Fall",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "volatileStatus": "flinch"
        },
        "target": "normal",
        "type": "flying"
    },
    "floralhealing": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "heal": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "floralhealing",
        "name": "Floral Healing",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fairy"
    },
    "flowershield": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "distance": 1
        },
        "id": "flowershield",
        "name": "Flower Shield",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "all",
        "type": "fairy"
    },
    "flowertrick": {
        "accuracy": True,
        "basePower": 70,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "flowertrick",
        "name": "Flower Trick",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass",
        "willCrit": True
    },
    "fly": {
        "accuracy": 95,
        "basePower": 90,
        "category": "physical",
        "flags": {
            "charge": 1,
            "contact": 1,
            "distance": 1,
            "failinstruct": 1,
            "gravity": 1,
            "mirror": 1,
            "noassist": 1,
            "nosleeptalk": 1,
            "protect": 1
        },
        "id": "fly",
        "name": "Fly",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "any",
        "type": "flying"
    },
    "flyingpress": {
        "accuracy": 95,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "contact": 1,
            "distance": 1,
            "gravity": 1,
            "mirror": 1,
            "nonsky": 1,
            "protect": 1
        },
        "id": "flyingpress",
        "name": "Flying Press",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "any",
        "type": "fighting"
    },
    "focusblast": {
        "accuracy": 70,
        "basePower": 120,
        "category": "special",
        "flags": {
            "bullet": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "focusblast",
        "name": "Focus Blast",
        "pp": 5,
        "priority": 0,
        "secondary": {
            "boosts": {
                "special-defense": -1
            },
            "chance": 10
        },
        "target": "normal",
        "type": "fighting"
    },
    "focusenergy": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "focusenergy",
        "name": "Focus Energy",
        "pp": 30,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal",
        "volatileStatus": "focusenergy"
    },
    "focuspunch": {
        "accuracy": 100,
        "basePower": 150,
        "category": "physical",
        "flags": {
            "contact": 1,
            "failcopycat": 1,
            "failinstruct": 1,
            "failmefirst": 1,
            "noassist": 1,
            "nosleeptalk": 1,
            "protect": 1,
            "punch": 1
        },
        "id": "focuspunch",
        "name": "Focus Punch",
        "pp": 20,
        "priority": -3,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "followme": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "failcopycat": 1,
            "noassist": 1
        },
        "id": "followme",
        "name": "Follow Me",
        "pp": 20,
        "priority": 2,
        "secondary": None,
        "target": "self",
        "type": "normal",
        "volatileStatus": "followme"
    },
    "forcepalm": {
        "accuracy": 100,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "forcepalm",
        "name": "Force Palm",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "status": "par"
        },
        "target": "normal",
        "type": "fighting"
    },
    "foresight": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "foresight",
        "name": "Foresight",
        "pp": 40,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal",
        "volatileStatus": "foresight"
    },
    "forestscurse": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "forestscurse",
        "name": "Forest's Curse",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass"
    },
    "foulplay": {
        "accuracy": 100,
        "basePower": 95,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "foulplay",
        "name": "Foul Play",
        "overrideOffensivePokemon": "target",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark"
    },
    "freezedry": {
        "accuracy": 100,
        "basePower": 70,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "freezedry",
        "name": "Freeze-Dry",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "status": "frz"
        },
        "target": "normal",
        "type": "ice"
    },
    "freezeshock": {
        "accuracy": 90,
        "basePower": 140,
        "category": "physical",
        "flags": {
            "charge": 1,
            "failinstruct": 1,
            "mirror": 1,
            "nosleeptalk": 1,
            "protect": 1
        },
        "id": "freezeshock",
        "name": "Freeze Shock",
        "pp": 5,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "status": "par"
        },
        "target": "normal",
        "type": "ice"
    },
    "freezingglare": {
        "accuracy": 100,
        "basePower": 90,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "freezingglare",
        "name": "Freezing Glare",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "status": "frz"
        },
        "target": "normal",
        "type": "psychic"
    },
    "freezyfrost": {
        "accuracy": 90,
        "basePower": 100,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "freezyfrost",
        "name": "Freezy Frost",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ice"
    },
    "frenzyplant": {
        "accuracy": 90,
        "basePower": 150,
        "category": "special",
        "flags": {
            "mirror": 1,
            "nonsky": 1,
            "protect": 1,
            "recharge": 1
        },
        "id": "frenzyplant",
        "name": "Frenzy Plant",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {
            "volatileStatus": "mustrecharge"
        },
        "target": "normal",
        "type": "grass"
    },
    "frostbreath": {
        "accuracy": 90,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "frostbreath",
        "name": "Frost Breath",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ice",
        "willCrit": True
    },
    "frustration": {
        "accuracy": 100,
        "basePower": 0,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "frustration",
        "name": "Frustration",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "furyattack": {
        "accuracy": 85,
        "basePower": 15,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "furyattack",
        "multihit": [
            2,
            5
        ],
        "name": "Fury Attack",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "furycutter": {
        "accuracy": 95,
        "basePower": 40,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "slicing": 1
        },
        "id": "furycutter",
        "name": "Fury Cutter",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "bug"
    },
    "furyswipes": {
        "accuracy": 80,
        "basePower": 18,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "furyswipes",
        "multihit": [
            2,
            5
        ],
        "name": "Fury Swipes",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "fusionbolt": {
        "accuracy": 100,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "fusionbolt",
        "name": "Fusion Bolt",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "electric"
    },
    "fusionflare": {
        "accuracy": 100,
        "basePower": 100,
        "category": "special",
        "flags": {
            "defrost": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "fusionflare",
        "name": "Fusion Flare",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fire"
    },
    "futuresight": {
        "accuracy": 100,
        "basePower": 120,
        "category": "special",
        "flags": {
            "allyanim": 1,
            "futuremove": 1
        },
        "id": "futuresight",
        "name": "Future Sight",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "gastroacid": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "gastroacid",
        "name": "Gastro Acid",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "poison",
        "volatileStatus": "gastroacid"
    },
    "geargrind": {
        "accuracy": 85,
        "basePower": 50,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "geargrind",
        "multihit": 2,
        "name": "Gear Grind",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "steel"
    },
    "gearup": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "snatch": 1
        },
        "id": "gearup",
        "name": "Gear Up",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "allySide",
        "type": "steel"
    },
    "geomancy": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "special-attack": 2,
            "special-defense": 2,
            "speed": 2
        },
        "category": "status",
        "flags": {
            "charge": 1,
            "failinstruct": 1,
            "nonsky": 1,
            "nosleeptalk": 1
        },
        "id": "geomancy",
        "name": "Geomancy",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "fairy"
    },
    "gigadrain": {
        "accuracy": 100,
        "basePower": 75,
        "category": "special",
        "drain": [
            1,
            2
        ],
        "flags": {
            "heal": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "gigadrain",
        "name": "Giga Drain",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass"
    },
    "gigaimpact": {
        "accuracy": 90,
        "basePower": 150,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "recharge": 1
        },
        "id": "gigaimpact",
        "name": "Giga Impact",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {
            "volatileStatus": "mustrecharge"
        },
        "target": "normal",
        "type": "normal"
    },
    "gigatonhammer": {
        "accuracy": 100,
        "basePower": 160,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "gigatonhammer",
        "name": "Gigaton Hammer",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "steel"
    },
    "glaciallance": {
        "accuracy": 100,
        "basePower": 120,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "glaciallance",
        "name": "Glacial Lance",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "ice"
    },
    "glaciate": {
        "accuracy": 95,
        "basePower": 65,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "glaciate",
        "name": "Glaciate",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "speed": -1
            },
            "chance": 100
        },
        "target": "allAdjacentFoes",
        "type": "ice"
    },
    "glaiverush": {
        "accuracy": 100,
        "basePower": 120,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "glaiverush",
        "name": "Glaive Rush",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {
            "volatileStatus": "glaiverush"
        },
        "target": "normal",
        "type": "dragon"
    },
    "glare": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "glare",
        "name": "Glare",
        "pp": 30,
        "priority": 0,
        "secondary": None,
        "status": "par",
        "target": "normal",
        "type": "normal"
    },
    "glitzyglow": {
        "accuracy": 95,
        "basePower": 80,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "glitzyglow",
        "name": "Glitzy Glow",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "self": {
            "sideCondition": "lightscreen"
        },
        "target": "normal",
        "type": "psychic"
    },
    "grassknot": {
        "accuracy": 100,
        "basePower": 0,
        "category": "special",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "nonsky": 1,
            "protect": 1
        },
        "id": "grassknot",
        "name": "Grass Knot",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass"
    },
    "grasspledge": {
        "accuracy": 100,
        "basePower": 80,
        "category": "special",
        "flags": {
            "mirror": 1,
            "nonsky": 1,
            "pledgecombo": 1,
            "protect": 1
        },
        "id": "grasspledge",
        "name": "Grass Pledge",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass"
    },
    "grasswhistle": {
        "accuracy": 55,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1,
            "sound": 1
        },
        "id": "grasswhistle",
        "name": "Grass Whistle",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "status": "slp",
        "target": "normal",
        "type": "grass"
    },
    "grassyglide": {
        "accuracy": 100,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "grassyglide",
        "name": "Grassy Glide",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass"
    },
    "grassyterrain": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "nonsky": 1
        },
        "id": "grassyterrain",
        "name": "Grassy Terrain",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "all",
        "terrain": "grassyterrain",
        "type": "grass"
    },
    "gravapple": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "gravapple",
        "name": "Grav Apple",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "defense": -1
            },
            "chance": 100
        },
        "target": "normal",
        "type": "grass"
    },
    "gravity": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "nonsky": 1
        },
        "id": "gravity",
        "name": "Gravity",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "all",
        "type": "psychic"
    },
    "growl": {
        "accuracy": 100,
        "basePower": 0,
        "boosts": {
            "attack": -1
        },
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1,
            "sound": 1
        },
        "id": "growl",
        "name": "Growl",
        "pp": 40,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "normal"
    },
    "growth": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "attack": 1,
            "special-attack": 1
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "growth",
        "name": "Growth",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "grudge": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1
        },
        "id": "grudge",
        "name": "Grudge",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "ghost",
        "volatileStatus": "grudge"
    },
    "guardsplit": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "protect": 1
        },
        "id": "guardsplit",
        "name": "Guard Split",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "guardswap": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "guardswap",
        "name": "Guard Swap",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "guillotine": {
        "accuracy": 30,
        "basePower": 0,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "guillotine",
        "name": "Guillotine",
        "ohko": True,
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "gunkshot": {
        "accuracy": 80,
        "basePower": 120,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "gunkshot",
        "name": "Gunk Shot",
        "pp": 5,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "status": "psn"
        },
        "target": "normal",
        "type": "poison"
    },
    "gust": {
        "accuracy": 100,
        "basePower": 40,
        "category": "special",
        "flags": {
            "distance": 1,
            "mirror": 1,
            "protect": 1,
            "wind": 1
        },
        "id": "gust",
        "name": "Gust",
        "pp": 35,
        "priority": 0,
        "secondary": None,
        "target": "any",
        "type": "flying"
    },
    "gyroball": {
        "accuracy": 100,
        "basePower": 0,
        "category": "physical",
        "flags": {
            "bullet": 1,
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "gyroball",
        "name": "Gyro Ball",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "steel"
    },
    "hail": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {},
        "id": "hail",
        "name": "Hail",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "all",
        "type": "ice",
        "weather": "hail"
    },
    "hammerarm": {
        "accuracy": 90,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "punch": 1
        },
        "id": "hammerarm",
        "name": "Hammer Arm",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "self": {
            "boosts": {
                "speed": -1
            }
        },
        "target": "normal",
        "type": "fighting"
    },
    "happyhour": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {},
        "id": "happyhour",
        "name": "Happy Hour",
        "pp": 30,
        "priority": 0,
        "secondary": None,
        "target": "allySide",
        "type": "normal"
    },
    "harden": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "defense": 1
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "harden",
        "name": "Harden",
        "pp": 30,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "haze": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1
        },
        "id": "haze",
        "name": "Haze",
        "pp": 30,
        "priority": 0,
        "secondary": None,
        "target": "all",
        "type": "ice"
    },
    "headbutt": {
        "accuracy": 100,
        "basePower": 70,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "headbutt",
        "name": "Headbutt",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "volatileStatus": "flinch"
        },
        "target": "normal",
        "type": "normal"
    },
    "headcharge": {
        "accuracy": 100,
        "basePower": 120,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "headcharge",
        "name": "Head Charge",
        "pp": 15,
        "priority": 0,
        "recoil": [
            1,
            4
        ],
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "headlongrush": {
        "accuracy": 100,
        "basePower": 120,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "punch": 1
        },
        "id": "headlongrush",
        "name": "Headlong Rush",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {
            "boosts": {
                "defense": -1,
                "special-defense": -1
            }
        },
        "target": "normal",
        "type": "ground"
    },
    "headsmash": {
        "accuracy": 80,
        "basePower": 150,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "headsmash",
        "name": "Head Smash",
        "pp": 5,
        "priority": 0,
        "recoil": [
            1,
            2
        ],
        "secondary": None,
        "target": "normal",
        "type": "rock"
    },
    "healbell": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "distance": 1,
            "snatch": 1,
            "sound": 1
        },
        "id": "healbell",
        "name": "Heal Bell",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "allyTeam",
        "type": "normal"
    },
    "healblock": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "healblock",
        "name": "Heal Block",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "psychic",
        "volatileStatus": "healblock"
    },
    "healingwish": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "heal": 1,
            "snatch": 1
        },
        "heal": [
            -1,
            1
        ],
        "heal_target": "self",
        "id": "healingwish",
        "name": "Healing Wish",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "side_conditions": "healingwish",
        "target": "self",
        "type": "psychic"
    },
    "healorder": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "heal": 1,
            "snatch": 1
        },
        "heal": [
            1,
            2
        ],
        "heal_target": "self",
        "id": "healorder",
        "name": "Heal Order",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "bug"
    },
    "healpulse": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "distance": 1,
            "heal": 1,
            "protect": 1,
            "pulse": 1,
            "reflectable": 1
        },
        "id": "healpulse",
        "name": "Heal Pulse",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "any",
        "type": "psychic"
    },
    "heartstamp": {
        "accuracy": 100,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "heartstamp",
        "name": "Heart Stamp",
        "pp": 25,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "volatileStatus": "flinch"
        },
        "target": "normal",
        "type": "psychic"
    },
    "heartswap": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "heartswap",
        "name": "Heart Swap",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "heatcrash": {
        "accuracy": 100,
        "basePower": 0,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "nonsky": 1,
            "protect": 1
        },
        "id": "heatcrash",
        "name": "Heat Crash",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fire"
    },
    "heatwave": {
        "accuracy": 90,
        "basePower": 95,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "wind": 1
        },
        "id": "heatwave",
        "name": "Heat Wave",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "status": "brn"
        },
        "target": "allAdjacentFoes",
        "type": "fire"
    },
    "heavyslam": {
        "accuracy": 100,
        "basePower": 0,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "nonsky": 1,
            "protect": 1
        },
        "id": "heavyslam",
        "name": "Heavy Slam",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "steel"
    },
    "helpinghand": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "failcopycat": 1,
            "noassist": 1
        },
        "id": "helpinghand",
        "name": "Helping Hand",
        "pp": 20,
        "priority": 5,
        "secondary": None,
        "target": "adjacentAlly",
        "type": "normal",
        "volatileStatus": "helpinghand"
    },
    "hex": {
        "accuracy": 100,
        "basePower": 65,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hex",
        "name": "Hex",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ghost"
    },
    "hiddenpower": {
        "accuracy": 100,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpower",
        "name": "Hidden Power",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "hiddenpowerbug60": {
        "accuracy": 100,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerbug60",
        "name": "Hidden Power Bug",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "bug"
    },
    "hiddenpowerbug70": {
        "accuracy": 100,
        "basePower": 70,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerbug70",
        "name": "Hidden Power Bug",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "bug"
    },
    "hiddenpowerdark60": {
        "accuracy": 100,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerdark60",
        "name": "Hidden Power Dark",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark"
    },
    "hiddenpowerdark70": {
        "accuracy": 100,
        "basePower": 70,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerdark70",
        "name": "Hidden Power Dark",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark"
    },
    "hiddenpowerdragon60": {
        "accuracy": 100,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerdragon60",
        "name": "Hidden Power Dragon",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dragon"
    },
    "hiddenpowerdragon70": {
        "accuracy": 100,
        "basePower": 70,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerdragon70",
        "name": "Hidden Power Dragon",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dragon"
    },
    "hiddenpowerelectric60": {
        "accuracy": 100,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerelectric60",
        "name": "Hidden Power Electric",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "electric"
    },
    "hiddenpowerelectric70": {
        "accuracy": 100,
        "basePower": 70,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerelectric70",
        "name": "Hidden Power Electric",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "electric"
    },
    "hiddenpowerfighting60": {
        "accuracy": 100,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerfighting60",
        "name": "Hidden Power Fighting",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "hiddenpowerfighting70": {
        "accuracy": 100,
        "basePower": 70,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerfighting70",
        "name": "Hidden Power Fighting",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "hiddenpowerfire60": {
        "accuracy": 100,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerfire60",
        "name": "Hidden Power Fire",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fire"
    },
    "hiddenpowerfire70": {
        "accuracy": 100,
        "basePower": 70,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerfire70",
        "name": "Hidden Power Fire",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fire"
    },
    "hiddenpowerflying60": {
        "accuracy": 100,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerflying60",
        "name": "Hidden Power Flying",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "flying"
    },
    "hiddenpowerflying70": {
        "accuracy": 100,
        "basePower": 70,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerflying70",
        "name": "Hidden Power Flying",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "flying"
    },
    "hiddenpowerghost60": {
        "accuracy": 100,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerghost60",
        "name": "Hidden Power Ghost",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ghost"
    },
    "hiddenpowerghost70": {
        "accuracy": 100,
        "basePower": 70,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerghost70",
        "name": "Hidden Power Ghost",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ghost"
    },
    "hiddenpowergrass60": {
        "accuracy": 100,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowergrass60",
        "name": "Hidden Power Grass",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass"
    },
    "hiddenpowergrass70": {
        "accuracy": 100,
        "basePower": 70,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowergrass70",
        "name": "Hidden Power Grass",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass"
    },
    "hiddenpowerground60": {
        "accuracy": 100,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerground60",
        "name": "Hidden Power Ground",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ground"
    },
    "hiddenpowerground70": {
        "accuracy": 100,
        "basePower": 70,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerground70",
        "name": "Hidden Power Ground",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ground"
    },
    "hiddenpowerice60": {
        "accuracy": 100,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerice60",
        "name": "Hidden Power Ice",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ice"
    },
    "hiddenpowerice70": {
        "accuracy": 100,
        "basePower": 70,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerice70",
        "name": "Hidden Power Ice",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ice"
    },
    "hiddenpowerpoison60": {
        "accuracy": 100,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerpoison60",
        "name": "Hidden Power Poison",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "poison"
    },
    "hiddenpowerpoison70": {
        "accuracy": 100,
        "basePower": 70,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerpoison70",
        "name": "Hidden Power Poison",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "poison"
    },
    "hiddenpowerpsychic60": {
        "accuracy": 100,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerpsychic60",
        "name": "Hidden Power Psychic",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "hiddenpowerpsychic70": {
        "accuracy": 100,
        "basePower": 70,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerpsychic70",
        "name": "Hidden Power Psychic",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "hiddenpowerrock60": {
        "accuracy": 100,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerrock60",
        "name": "Hidden Power Rock",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "rock"
    },
    "hiddenpowerrock70": {
        "accuracy": 100,
        "basePower": 70,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerrock70",
        "name": "Hidden Power Rock",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "rock"
    },
    "hiddenpowersteel60": {
        "accuracy": 100,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowersteel60",
        "name": "Hidden Power Steel",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "steel"
    },
    "hiddenpowersteel70": {
        "accuracy": 100,
        "basePower": 70,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowersteel70",
        "name": "Hidden Power Steel",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "steel"
    },
    "hiddenpowerwater60": {
        "accuracy": 100,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerwater60",
        "name": "Hidden Power Water",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "water"
    },
    "hiddenpowerwater70": {
        "accuracy": 100,
        "basePower": 70,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hiddenpowerwater70",
        "name": "Hidden Power Water",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "water"
    },
    "highhorsepower": {
        "accuracy": 95,
        "basePower": 95,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "highhorsepower",
        "name": "High Horsepower",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ground"
    },
    "highjumpkick": {
        "accuracy": 90,
        "basePower": 130,
        "category": "physical",
        "crash": [
            1,
            2
        ],
        "flags": {
            "contact": 1,
            "gravity": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "highjumpkick",
        "name": "High Jump Kick",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "holdback": {
        "accuracy": 100,
        "basePower": 40,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "holdback",
        "name": "Hold Back",
        "pp": 40,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "holdhands": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "failcopycat": 1,
            "failinstruct": 1,
            "failmimic": 1,
            "noassist": 1,
            "nosleeptalk": 1
        },
        "id": "holdhands",
        "name": "Hold Hands",
        "pp": 40,
        "priority": 0,
        "secondary": None,
        "target": "adjacentAlly",
        "type": "normal"
    },
    "honeclaws": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "accuracy": 1,
            "attack": 1
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "honeclaws",
        "name": "Hone Claws",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "dark"
    },
    "hornattack": {
        "accuracy": 100,
        "basePower": 65,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "hornattack",
        "name": "Horn Attack",
        "pp": 25,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "horndrill": {
        "accuracy": 30,
        "basePower": 0,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "horndrill",
        "name": "Horn Drill",
        "ohko": True,
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "hornleech": {
        "accuracy": 100,
        "basePower": 75,
        "category": "physical",
        "drain": [
            1,
            2
        ],
        "flags": {
            "contact": 1,
            "heal": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "hornleech",
        "name": "Horn Leech",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass"
    },
    "howl": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "attack": 1
        },
        "category": "status",
        "flags": {
            "snatch": 1,
            "sound": 1
        },
        "id": "howl",
        "name": "Howl",
        "pp": 40,
        "priority": 0,
        "secondary": None,
        "target": "allies",
        "type": "normal"
    },
    "hurricane": {
        "accuracy": 70,
        "basePower": 110,
        "category": "special",
        "flags": {
            "distance": 1,
            "mirror": 1,
            "protect": 1,
            "wind": 1
        },
        "id": "hurricane",
        "name": "Hurricane",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "volatileStatus": "confusion"
        },
        "target": "any",
        "type": "flying"
    },
    "hydrocannon": {
        "accuracy": 90,
        "basePower": 150,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "recharge": 1
        },
        "id": "hydrocannon",
        "name": "Hydro Cannon",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {
            "volatileStatus": "mustrecharge"
        },
        "target": "normal",
        "type": "water"
    },
    "hydropump": {
        "accuracy": 80,
        "basePower": 110,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "hydropump",
        "name": "Hydro Pump",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "water"
    },
    "hydrosteam": {
        "accuracy": 100,
        "basePower": 80,
        "category": "special",
        "flags": {
            "defrost": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "hydrosteam",
        "name": "Hydro Steam",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "thawsTarget": True,
        "type": "water"
    },
    "hyperbeam": {
        "accuracy": 90,
        "basePower": 150,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "recharge": 1
        },
        "id": "hyperbeam",
        "name": "Hyper Beam",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {
            "volatileStatus": "mustrecharge"
        },
        "target": "normal",
        "type": "normal"
    },
    "hyperdrill": {
        "accuracy": 100,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1
        },
        "id": "hyperdrill",
        "name": "Hyper Drill",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "hyperfang": {
        "accuracy": 90,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "bite": 1,
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "hyperfang",
        "name": "Hyper Fang",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "volatileStatus": "flinch"
        },
        "target": "normal",
        "type": "normal"
    },
    "hyperspacefury": {
        "accuracy": True,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "bypasssub": 1,
            "mirror": 1
        },
        "id": "hyperspacefury",
        "name": "Hyperspace Fury",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {
            "boosts": {
                "defense": -1
            }
        },
        "target": "normal",
        "type": "dark"
    },
    "hyperspacehole": {
        "accuracy": True,
        "basePower": 80,
        "category": "special",
        "flags": {
            "bypasssub": 1,
            "mirror": 1
        },
        "id": "hyperspacehole",
        "name": "Hyperspace Hole",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "hypervoice": {
        "accuracy": 100,
        "basePower": 90,
        "category": "special",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "sound": 1
        },
        "id": "hypervoice",
        "name": "Hyper Voice",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "normal"
    },
    "hypnosis": {
        "accuracy": 60,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "hypnosis",
        "name": "Hypnosis",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "status": "slp",
        "target": "normal",
        "type": "psychic"
    },
    "iceball": {
        "accuracy": 90,
        "basePower": 30,
        "category": "physical",
        "flags": {
            "bullet": 1,
            "contact": 1,
            "failinstruct": 1,
            "mirror": 1,
            "noparentalbond": 1,
            "protect": 1
        },
        "id": "iceball",
        "name": "Ice Ball",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ice"
    },
    "icebeam": {
        "accuracy": 100,
        "basePower": 90,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "icebeam",
        "name": "Ice Beam",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "status": "frz"
        },
        "target": "normal",
        "type": "ice"
    },
    "iceburn": {
        "accuracy": 90,
        "basePower": 140,
        "category": "special",
        "flags": {
            "charge": 1,
            "failinstruct": 1,
            "mirror": 1,
            "nosleeptalk": 1,
            "protect": 1
        },
        "id": "iceburn",
        "name": "Ice Burn",
        "pp": 5,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "status": "brn"
        },
        "target": "normal",
        "type": "ice"
    },
    "icefang": {
        "accuracy": 95,
        "basePower": 65,
        "category": "physical",
        "flags": {
            "bite": 1,
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "icefang",
        "name": "Ice Fang",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ice"
    },
    "icehammer": {
        "accuracy": 90,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "punch": 1
        },
        "id": "icehammer",
        "name": "Ice Hammer",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "self": {
            "boosts": {
                "speed": -1
            }
        },
        "target": "normal",
        "type": "ice"
    },
    "icepunch": {
        "accuracy": 100,
        "basePower": 75,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "punch": 1
        },
        "id": "icepunch",
        "name": "Ice Punch",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "status": "frz"
        },
        "target": "normal",
        "type": "ice"
    },
    "iceshard": {
        "accuracy": 100,
        "basePower": 40,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "iceshard",
        "name": "Ice Shard",
        "pp": 30,
        "priority": 1,
        "secondary": None,
        "target": "normal",
        "type": "ice"
    },
    "icespinner": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "icespinner",
        "name": "Ice Spinner",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ice"
    },
    "iciclecrash": {
        "accuracy": 90,
        "basePower": 85,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "iciclecrash",
        "name": "Icicle Crash",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "volatileStatus": "flinch"
        },
        "target": "normal",
        "type": "ice"
    },
    "iciclespear": {
        "accuracy": 100,
        "basePower": 25,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "iciclespear",
        "multihit": [
            2,
            5
        ],
        "name": "Icicle Spear",
        "pp": 30,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ice"
    },
    "icywind": {
        "accuracy": 95,
        "basePower": 55,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "wind": 1
        },
        "id": "icywind",
        "name": "Icy Wind",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "boosts": {
                "speed": -1
            },
            "chance": 100
        },
        "target": "allAdjacentFoes",
        "type": "ice"
    },
    "imprison": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "mustpressure": 1,
            "snatch": 1
        },
        "id": "imprison",
        "name": "Imprison",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "psychic",
        "volatileStatus": "imprison"
    },
    "incinerate": {
        "accuracy": 100,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "incinerate",
        "name": "Incinerate",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "fire"
    },
    "infernalparade": {
        "accuracy": 100,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "infernalparade",
        "name": "Infernal Parade",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "status": "brn"
        },
        "target": "normal",
        "type": "ghost"
    },
    "inferno": {
        "accuracy": 50,
        "basePower": 100,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "inferno",
        "name": "Inferno",
        "pp": 5,
        "priority": 0,
        "secondary": {
            "chance": 100,
            "status": "brn"
        },
        "target": "normal",
        "type": "fire"
    },
    "infestation": {
        "accuracy": 100,
        "basePower": 20,
        "category": "special",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "infestation",
        "name": "Infestation",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "bug",
        "volatileStatus": "partiallytrapped"
    },
    "ingrain": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "nonsky": 1,
            "snatch": 1
        },
        "id": "ingrain",
        "name": "Ingrain",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "grass",
        "volatileStatus": "ingrain"
    },
    "instruct": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "bypasssub": 1,
            "failinstruct": 1,
            "protect": 1
        },
        "id": "instruct",
        "name": "Instruct",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "iondeluge": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {},
        "id": "iondeluge",
        "name": "Ion Deluge",
        "pp": 25,
        "priority": 1,
        "secondary": None,
        "target": "all",
        "type": "electric"
    },
    "irondefense": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "defense": 2
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "irondefense",
        "name": "Iron Defense",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "steel"
    },
    "ironhead": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "ironhead",
        "name": "Iron Head",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "volatileStatus": "flinch"
        },
        "target": "normal",
        "type": "steel"
    },
    "irontail": {
        "accuracy": 75,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "irontail",
        "name": "Iron Tail",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "boosts": {
                "defense": -1
            },
            "chance": 30
        },
        "target": "normal",
        "type": "steel"
    },
    "jawlock": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "bite": 1,
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "jawlock",
        "name": "Jaw Lock",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark"
    },
    "jetpunch": {
        "accuracy": 100,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "punch": 1
        },
        "hasSheerForce": True,
        "id": "jetpunch",
        "name": "Jet Punch",
        "pp": 15,
        "priority": 1,
        "secondary": None,
        "target": "normal",
        "type": "water"
    },
    "judgment": {
        "accuracy": 100,
        "basePower": 100,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "judgment",
        "name": "Judgment",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "jumpkick": {
        "accuracy": 95,
        "basePower": 100,
        "category": "physical",
        "crash": [
            1,
            2
        ],
        "flags": {
            "contact": 1,
            "gravity": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "jumpkick",
        "name": "Jump Kick",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "junglehealing": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "bypasssub": 1,
            "heal": 1
        },
        "heal": [
            1,
            4
        ],
        "heal_target": "self",
        "id": "junglehealing",
        "name": "Jungle Healing",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "allies",
        "type": "grass"
    },
    "karatechop": {
        "accuracy": 100,
        "basePower": 50,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "karatechop",
        "name": "Karate Chop",
        "pp": 25,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "kinesis": {
        "accuracy": 80,
        "basePower": 0,
        "boosts": {
            "accuracy": -1
        },
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "kinesis",
        "name": "Kinesis",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "kingsshield": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "failcopycat": 1,
            "failinstruct": 1,
            "noassist": 1
        },
        "id": "kingsshield",
        "name": "King's Shield",
        "pp": 10,
        "priority": 4,
        "secondary": None,
        "target": "self",
        "type": "steel",
        "volatileStatus": "kingsshield"
    },
    "knockoff": {
        "accuracy": 100,
        "basePower": 65,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "knockoff",
        "name": "Knock Off",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark"
    },
    "kowtowcleave": {
        "accuracy": True,
        "basePower": 85,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "slicing": 1
        },
        "id": "kowtowcleave",
        "name": "Kowtow Cleave",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark"
    },
    "landswrath": {
        "accuracy": 100,
        "basePower": 90,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "nonsky": 1,
            "protect": 1
        },
        "id": "landswrath",
        "name": "Land's Wrath",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "ground"
    },
    "laserfocus": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "laserfocus",
        "name": "Laser Focus",
        "pp": 30,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal",
        "volatileStatus": "laserfocus"
    },
    "lashout": {
        "accuracy": 100,
        "basePower": 75,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "lashout",
        "name": "Lash Out",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark"
    },
    "lastresort": {
        "accuracy": 100,
        "basePower": 140,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "lastresort",
        "name": "Last Resort",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "lastrespects": {
        "accuracy": 100,
        "basePower": 50,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "lastrespects",
        "name": "Last Respects",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ghost"
    },
    "lavaplume": {
        "accuracy": 100,
        "basePower": 80,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "lavaplume",
        "name": "Lava Plume",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "status": "brn"
        },
        "target": "allAdjacent",
        "type": "fire"
    },
    "leafage": {
        "accuracy": 100,
        "basePower": 40,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "leafage",
        "name": "Leafage",
        "pp": 40,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass"
    },
    "leafblade": {
        "accuracy": 100,
        "basePower": 90,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "slicing": 1
        },
        "id": "leafblade",
        "name": "Leaf Blade",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass"
    },
    "leafstorm": {
        "accuracy": 90,
        "basePower": 130,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "leafstorm",
        "name": "Leaf Storm",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {
            "boosts": {
                "special-attack": -2
            }
        },
        "target": "normal",
        "type": "grass"
    },
    "leaftornado": {
        "accuracy": 90,
        "basePower": 65,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "leaftornado",
        "name": "Leaf Tornado",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "accuracy": -1
            },
            "chance": 50
        },
        "target": "normal",
        "type": "grass"
    },
    "leechlife": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "drain": [
            1,
            2
        ],
        "flags": {
            "contact": 1,
            "heal": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "leechlife",
        "name": "Leech Life",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "bug"
    },
    "leechseed": {
        "accuracy": 90,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "powder": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "leechseed",
        "name": "Leech Seed",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass",
        "volatileStatus": "leechseed"
    },
    "leer": {
        "accuracy": 100,
        "basePower": 0,
        "boosts": {
            "defense": -1
        },
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "leer",
        "name": "Leer",
        "pp": 30,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "normal"
    },
    "lick": {
        "accuracy": 100,
        "basePower": 30,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "lick",
        "name": "Lick",
        "pp": 30,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "status": "par"
        },
        "target": "normal",
        "type": "ghost"
    },
    "lifedew": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "heal": 1,
            "snatch": 1
        },
        "heal": [
            1,
            4
        ],
        "id": "lifedew",
        "name": "Life Dew",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "allies",
        "type": "water"
    },
    "lightofruin": {
        "accuracy": 90,
        "basePower": 140,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "lightofruin",
        "name": "Light of Ruin",
        "pp": 5,
        "priority": 0,
        "recoil": [
            1,
            2
        ],
        "secondary": None,
        "target": "normal",
        "type": "fairy"
    },
    "lightscreen": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "lightscreen",
        "name": "Light Screen",
        "pp": 30,
        "priority": 0,
        "secondary": None,
        "side_conditions": "lightscreen",
        "target": "allySide",
        "type": "psychic"
    },
    "liquidation": {
        "accuracy": 100,
        "basePower": 85,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "liquidation",
        "name": "Liquidation",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "defense": -1
            },
            "chance": 20
        },
        "target": "normal",
        "type": "water"
    },
    "lockon": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "lockon",
        "name": "Lock-On",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "lovelykiss": {
        "accuracy": 75,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "lovelykiss",
        "name": "Lovely Kiss",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "status": "slp",
        "target": "normal",
        "type": "normal"
    },
    "lowkick": {
        "accuracy": 100,
        "basePower": 0,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "lowkick",
        "name": "Low Kick",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "lowsweep": {
        "accuracy": 100,
        "basePower": 65,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "lowsweep",
        "name": "Low Sweep",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "boosts": {
                "speed": -1
            },
            "chance": 100
        },
        "target": "normal",
        "type": "fighting"
    },
    "luckychant": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "luckychant",
        "name": "Lucky Chant",
        "pp": 30,
        "priority": 0,
        "secondary": None,
        "side_conditions": "luckychant",
        "target": "allySide",
        "type": "normal"
    },
    "luminacrash": {
        "accuracy": 100,
        "basePower": 80,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "luminacrash",
        "name": "Lumina Crash",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "special-defense": -2
            },
            "chance": 100
        },
        "target": "normal",
        "type": "psychic"
    },
    "lunarblessing": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "heal": 1,
            "snatch": 1
        },
        "heal": [
            1,
            4
        ],
        "heal_target": "self",
        "id": "lunarblessing",
        "name": "Lunar Blessing",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "allies",
        "type": "psychic"
    },
    "lunardance": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "dance": 1,
            "heal": 1,
            "snatch": 1
        },
        "id": "lunardance",
        "name": "Lunar Dance",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "psychic"
    },
    "lunge": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "lunge",
        "name": "Lunge",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "boosts": {
                "attack": -1
            },
            "chance": 100
        },
        "target": "normal",
        "type": "bug"
    },
    "lusterpurge": {
        "accuracy": 100,
        "basePower": 70,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "lusterpurge",
        "name": "Luster Purge",
        "pp": 5,
        "priority": 0,
        "secondary": {
            "boosts": {
                "special-defense": -1
            },
            "chance": 50
        },
        "target": "normal",
        "type": "psychic"
    },
    "machpunch": {
        "accuracy": 100,
        "basePower": 40,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "punch": 1
        },
        "id": "machpunch",
        "name": "Mach Punch",
        "pp": 30,
        "priority": 1,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "magicalleaf": {
        "accuracy": True,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "magicalleaf",
        "name": "Magical Leaf",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass"
    },
    "magicaltorque": {
        "accuracy": 100,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "failcopycat": 1,
            "failencore": 1,
            "failinstruct": 1,
            "failmefirst": 1,
            "failmimic": 1,
            "noassist": 1,
            "nosleeptalk": 1,
            "protect": 1
        },
        "id": "magicaltorque",
        "name": "Magical Torque",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "volatileStatus": "confusion"
        },
        "target": "normal",
        "type": "fairy"
    },
    "magiccoat": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {},
        "id": "magiccoat",
        "name": "Magic Coat",
        "pp": 15,
        "priority": 4,
        "secondary": None,
        "target": "self",
        "type": "psychic",
        "volatileStatus": "magiccoat"
    },
    "magicpowder": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "mirror": 1,
            "powder": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "magicpowder",
        "name": "Magic Powder",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "magicroom": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1
        },
        "id": "magicroom",
        "name": "Magic Room",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "all",
        "type": "psychic"
    },
    "magmastorm": {
        "accuracy": 75,
        "basePower": 100,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "magmastorm",
        "name": "Magma Storm",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fire",
        "volatileStatus": "partiallytrapped"
    },
    "magnetbomb": {
        "accuracy": True,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "bullet": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "magnetbomb",
        "name": "Magnet Bomb",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "steel"
    },
    "magneticflux": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "distance": 1,
            "snatch": 1
        },
        "id": "magneticflux",
        "name": "Magnetic Flux",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "allySide",
        "type": "electric"
    },
    "magnetrise": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "gravity": 1,
            "snatch": 1
        },
        "id": "magnetrise",
        "name": "Magnet Rise",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "electric",
        "volatileStatus": "magnetrise"
    },
    "magnitude": {
        "accuracy": 100,
        "basePower": 0,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "nonsky": 1,
            "protect": 1
        },
        "id": "magnitude",
        "name": "Magnitude",
        "pp": 30,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacent",
        "type": "ground"
    },
    "makeitrain": {
        "accuracy": 100,
        "basePower": 120,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "makeitrain",
        "name": "Make It Rain",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {
            "boosts": {
                "special-attack": -1
            }
        },
        "target": "allAdjacentFoes",
        "type": "steel"
    },
    "matblock": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "failcopycat": 1,
            "noassist": 1,
            "nonsky": 1,
            "snatch": 1
        },
        "id": "matblock",
        "name": "Mat Block",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "side_conditions": "matblock",
        "target": "allySide",
        "type": "fighting"
    },
    "meanlook": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "reflectable": 1
        },
        "id": "meanlook",
        "name": "Mean Look",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "meditate": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "attack": 1
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "meditate",
        "name": "Meditate",
        "pp": 40,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "psychic"
    },
    "mefirst": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "failcopycat": 1,
            "failencore": 1,
            "failinstruct": 1,
            "failmefirst": 1,
            "failmimic": 1,
            "noassist": 1,
            "nosleeptalk": 1,
            "protect": 1
        },
        "id": "mefirst",
        "name": "Me First",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "adjacentFoe",
        "type": "normal"
    },
    "megadrain": {
        "accuracy": 100,
        "basePower": 40,
        "category": "special",
        "drain": [
            1,
            2
        ],
        "flags": {
            "heal": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "megadrain",
        "name": "Mega Drain",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass"
    },
    "megahorn": {
        "accuracy": 85,
        "basePower": 120,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "megahorn",
        "name": "Megahorn",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "bug"
    },
    "megakick": {
        "accuracy": 75,
        "basePower": 120,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "megakick",
        "name": "Mega Kick",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "megapunch": {
        "accuracy": 85,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "punch": 1
        },
        "id": "megapunch",
        "name": "Mega Punch",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "memento": {
        "accuracy": 100,
        "basePower": 0,
        "boosts": {
            "attack": -2,
            "special-attack": -2
        },
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "heal": [
            -1,
            1
        ],
        "heal_target": "self",
        "id": "memento",
        "name": "Memento",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark"
    },
    "metalburst": {
        "accuracy": 100,
        "basePower": 0,
        "category": "physical",
        "flags": {
            "failmefirst": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "metalburst",
        "name": "Metal Burst",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "scripted",
        "type": "steel"
    },
    "metalclaw": {
        "accuracy": 95,
        "basePower": 50,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "metalclaw",
        "name": "Metal Claw",
        "pp": 35,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "self": {
                "boosts": {
                    "attack": 1
                }
            }
        },
        "target": "normal",
        "type": "steel"
    },
    "metalsound": {
        "accuracy": 85,
        "basePower": 0,
        "boosts": {
            "special-defense": -2
        },
        "category": "status",
        "flags": {
            "allyanim": 1,
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1,
            "sound": 1
        },
        "id": "metalsound",
        "name": "Metal Sound",
        "pp": 40,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "steel"
    },
    "meteorassault": {
        "accuracy": 100,
        "basePower": 150,
        "category": "physical",
        "flags": {
            "failinstruct": 1,
            "mirror": 1,
            "protect": 1,
            "recharge": 1
        },
        "id": "meteorassault",
        "name": "Meteor Assault",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {
            "volatileStatus": "mustrecharge"
        },
        "target": "normal",
        "type": "fighting"
    },
    "meteorbeam": {
        "accuracy": 90,
        "basePower": 120,
        "category": "special",
        "flags": {
            "charge": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "meteorbeam",
        "name": "Meteor Beam",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "rock"
    },
    "meteormash": {
        "accuracy": 90,
        "basePower": 90,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "punch": 1
        },
        "id": "meteormash",
        "name": "Meteor Mash",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 20,
            "self": {
                "boosts": {
                    "attack": 1
                }
            }
        },
        "target": "normal",
        "type": "steel"
    },
    "metronome": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "failcopycat": 1,
            "failencore": 1,
            "failinstruct": 1,
            "failmimic": 1,
            "noassist": 1,
            "nosleeptalk": 1
        },
        "id": "metronome",
        "name": "Metronome",
        "noMetronome": [
            "After You",
            "Apple Acid",
            "Armor Cannon",
            "Assist",
            "Astral Barrage",
            "Aura Wheel",
            "Baneful Bunker",
            "Beak Blast",
            "Behemoth Bash",
            "Behemoth Blade",
            "Belch",
            "Bestow",
            "Blazing Torque",
            "Body Press",
            "Branch Poke",
            "Breaking Swipe",
            "Celebrate",
            "Chatter",
            "Chilling Water",
            "Chilly Reception",
            "Clangorous Soul",
            "Collision Course",
            "Combat Torque",
            "Comeuppance",
            "Copycat",
            "Counter",
            "Covet",
            "Crafty Shield",
            "Decorate",
            "Destiny Bond",
            "Detect",
            "Diamond Storm",
            "Doodle",
            "Double Iron Bash",
            "Double Shock",
            "Dragon Ascent",
            "Dragon Energy",
            "Drum Beating",
            "Dynamax Cannon",
            "Electro Drift",
            "Endure",
            "Eternabeam",
            "False Surrender",
            "Feint",
            "Fiery Wrath",
            "Fillet Away",
            "Fleur Cannon",
            "Focus Punch",
            "Follow Me",
            "Freeze Shock",
            "Freezing Glare",
            "Glacial Lance",
            "Grav Apple",
            "Helping Hand",
            "Hold Hands",
            "Hyper Drill",
            "Hyperspace Fury",
            "Hyperspace Hole",
            "Ice Burn",
            "Instruct",
            "Jet Punch",
            "Jungle Healing",
            "King's Shield",
            "Life Dew",
            "Light of Ruin",
            "Magical Torque",
            "Make It Rain",
            "Mat Block",
            "Me First",
            "Meteor Assault",
            "Metronome",
            "Mimic",
            "Mind Blown",
            "Mirror Coat",
            "Mirror Move",
            "Moongeist Beam",
            "Nature Power",
            "Nature's Madness",
            "Noxious Torque",
            "Obstruct",
            "Order Up",
            "Origin Pulse",
            "Overdrive",
            "Photon Geyser",
            "Plasma Fists",
            "Population Bomb",
            "Pounce",
            "Power Shift",
            "Precipice Blades",
            "Protect",
            "Pyro Ball",
            "Quash",
            "Quick Guard",
            "Rage Fist",
            "Rage Powder",
            "Raging Bull",
            "Raging Fury",
            "Relic Song",
            "Revival Blessing",
            "Ruination",
            "Salt Cure",
            "Secret Sword",
            "Shed Tail",
            "Shell Trap",
            "Silk Trap",
            "Sketch",
            "Sleep Talk",
            "Snap Trap",
            "Snarl",
            "Snatch",
            "Snore",
            "Snowscape",
            "Spectral Thief",
            "Spicy Extract",
            "Spiky Shield",
            "Spirit Break",
            "Spotlight",
            "Springtide Storm",
            "Steam Eruption",
            "Steel Beam",
            "Strange Steam",
            "Struggle",
            "Sunsteel Strike",
            "Surging Strikes",
            "Switcheroo",
            "Techno Blast",
            "Thief",
            "Thousand Arrows",
            "Thousand Waves",
            "Thunder Cage",
            "Thunderous Kick",
            "Tidy Up",
            "Trailblaze",
            "Transform",
            "Trick",
            "Twin Beam",
            "V-create",
            "Wicked Blow",
            "Wicked Torque",
            "Wide Guard"
        ],
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "milkdrink": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "heal": 1,
            "snatch": 1
        },
        "heal": [
            1,
            2
        ],
        "heal_target": "self",
        "id": "milkdrink",
        "name": "Milk Drink",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "mimic": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "bypasssub": 1,
            "failcopycat": 1,
            "failencore": 1,
            "failinstruct": 1,
            "failmimic": 1,
            "noassist": 1,
            "nosleeptalk": 1,
            "protect": 1
        },
        "id": "mimic",
        "name": "Mimic",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "mindblown": {
        "accuracy": 100,
        "basePower": 150,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "heal": [
            -1,
            2
        ],
        "heal_target": "self",
        "id": "mindblown",
        "name": "Mind Blown",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacent",
        "type": "fire"
    },
    "mindreader": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "mindreader",
        "name": "Mind Reader",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "minimize": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "evasion": 2
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "minimize",
        "name": "Minimize",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal",
        "volatileStatus": "minimize"
    },
    "miracleeye": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "miracleeye",
        "name": "Miracle Eye",
        "pp": 40,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic",
        "volatileStatus": "miracleeye"
    },
    "mirrorcoat": {
        "accuracy": 100,
        "basePower": 0,
        "category": "special",
        "flags": {
            "failmefirst": 1,
            "noassist": 1,
            "protect": 1
        },
        "id": "mirrorcoat",
        "name": "Mirror Coat",
        "pp": 20,
        "priority": -5,
        "secondary": None,
        "target": "scripted",
        "type": "psychic"
    },
    "mirrormove": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "failcopycat": 1,
            "failencore": 1,
            "failinstruct": 1,
            "failmimic": 1,
            "noassist": 1,
            "nosleeptalk": 1
        },
        "id": "mirrormove",
        "name": "Mirror Move",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "flying"
    },
    "mirrorshot": {
        "accuracy": 85,
        "basePower": 65,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "mirrorshot",
        "name": "Mirror Shot",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "accuracy": -1
            },
            "chance": 30
        },
        "target": "normal",
        "type": "steel"
    },
    "mist": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "mist",
        "name": "Mist",
        "pp": 30,
        "priority": 0,
        "secondary": None,
        "side_conditions": "mist",
        "target": "allySide",
        "type": "ice"
    },
    "mistball": {
        "accuracy": 100,
        "basePower": 70,
        "category": "special",
        "flags": {
            "bullet": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "mistball",
        "name": "Mist Ball",
        "pp": 5,
        "priority": 0,
        "secondary": {
            "boosts": {
                "special-attack": -1
            },
            "chance": 50
        },
        "target": "normal",
        "type": "psychic"
    },
    "mistyexplosion": {
        "accuracy": 100,
        "basePower": 100,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "heal": [
            -1,
            1
        ],
        "heal_target": "self",
        "id": "mistyexplosion",
        "name": "Misty Explosion",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacent",
        "type": "fairy"
    },
    "mistyterrain": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "nonsky": 1
        },
        "id": "mistyterrain",
        "name": "Misty Terrain",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "all",
        "terrain": "mistyterrain",
        "type": "fairy"
    },
    "moonblast": {
        "accuracy": 100,
        "basePower": 95,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "moonblast",
        "name": "Moonblast",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "boosts": {
                "special-attack": -1
            },
            "chance": 30
        },
        "target": "normal",
        "type": "fairy"
    },
    "moongeistbeam": {
        "accuracy": 100,
        "basePower": 100,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "moongeistbeam",
        "ignoreAbility": True,
        "name": "Moongeist Beam",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ghost"
    },
    "moonlight": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "heal": 1,
            "snatch": 1
        },
        "heal": [
            1,
            2
        ],
        "heal_target": "self",
        "id": "moonlight",
        "name": "Moonlight",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "fairy"
    },
    "morningsun": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "heal": 1,
            "snatch": 1
        },
        "heal": [
            1,
            2
        ],
        "heal_target": "self",
        "id": "morningsun",
        "name": "Morning Sun",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "mortalspin": {
        "accuracy": 100,
        "basePower": 30,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "mortalspin",
        "name": "Mortal Spin",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "chance": 100,
            "status": "psn"
        },
        "target": "allAdjacentFoes",
        "type": "poison"
    },
    "mountaingale": {
        "accuracy": 85,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "mountaingale",
        "name": "Mountain Gale",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "volatileStatus": "flinch"
        },
        "target": "normal",
        "type": "ice"
    },
    "mudbomb": {
        "accuracy": 85,
        "basePower": 65,
        "category": "special",
        "flags": {
            "bullet": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "mudbomb",
        "name": "Mud Bomb",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "accuracy": -1
            },
            "chance": 30
        },
        "target": "normal",
        "type": "ground"
    },
    "muddywater": {
        "accuracy": 85,
        "basePower": 90,
        "category": "special",
        "flags": {
            "mirror": 1,
            "nonsky": 1,
            "protect": 1
        },
        "id": "muddywater",
        "name": "Muddy Water",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "accuracy": -1
            },
            "chance": 30
        },
        "target": "allAdjacentFoes",
        "type": "water"
    },
    "mudshot": {
        "accuracy": 95,
        "basePower": 55,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "mudshot",
        "name": "Mud Shot",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "boosts": {
                "speed": -1
            },
            "chance": 100
        },
        "target": "normal",
        "type": "ground"
    },
    "mudslap": {
        "accuracy": 100,
        "basePower": 20,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "mudslap",
        "name": "Mud-Slap",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "accuracy": -1
            },
            "chance": 100
        },
        "target": "normal",
        "type": "ground"
    },
    "mudsport": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "nonsky": 1
        },
        "id": "mudsport",
        "name": "Mud Sport",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "all",
        "type": "ground"
    },
    "multiattack": {
        "accuracy": 100,
        "basePower": 120,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "multiattack",
        "name": "Multi-Attack",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "mysticalfire": {
        "accuracy": 100,
        "basePower": 75,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "mysticalfire",
        "name": "Mystical Fire",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "special-attack": -1
            },
            "chance": 100
        },
        "target": "normal",
        "type": "fire"
    },
    "mysticalpower": {
        "accuracy": 90,
        "basePower": 70,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "mysticalpower",
        "name": "Mystical Power",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 100,
            "self": {
                "boosts": {
                    "special-attack": 1
                }
            }
        },
        "target": "normal",
        "type": "psychic"
    },
    "nastyplot": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "special-attack": 2
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "nastyplot",
        "name": "Nasty Plot",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "dark"
    },
    "naturalgift": {
        "accuracy": 100,
        "basePower": 0,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "naturalgift",
        "name": "Natural Gift",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "naturepower": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "failcopycat": 1,
            "failencore": 1,
            "failinstruct": 1,
            "failmimic": 1,
            "noassist": 1,
            "nosleeptalk": 1
        },
        "id": "naturepower",
        "name": "Nature Power",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "naturesmadness": {
        "accuracy": 90,
        "basePower": 0,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "naturesmadness",
        "name": "Nature's Madness",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fairy"
    },
    "needlearm": {
        "accuracy": 100,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "needlearm",
        "name": "Needle Arm",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "volatileStatus": "flinch"
        },
        "target": "normal",
        "type": "grass"
    },
    "nightdaze": {
        "accuracy": 95,
        "basePower": 85,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "nightdaze",
        "name": "Night Daze",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "accuracy": -1
            },
            "chance": 40
        },
        "target": "normal",
        "type": "dark"
    },
    "nightmare": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "nightmare",
        "name": "Nightmare",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ghost",
        "volatileStatus": "nightmare"
    },
    "nightshade": {
        "accuracy": 100,
        "basePower": 0,
        "category": "special",
        "damage": "level",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "nightshade",
        "name": "Night Shade",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ghost"
    },
    "nightslash": {
        "accuracy": 100,
        "basePower": 70,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "slicing": 1
        },
        "id": "nightslash",
        "name": "Night Slash",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark"
    },
    "nobleroar": {
        "accuracy": 100,
        "basePower": 0,
        "boosts": {
            "attack": -1,
            "special-attack": -1
        },
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1,
            "sound": 1
        },
        "id": "nobleroar",
        "name": "Noble Roar",
        "pp": 30,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "noretreat": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "attack": 1,
            "defense": 1,
            "special-attack": 1,
            "special-defense": 1,
            "speed": 1
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "noretreat",
        "name": "No Retreat",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "fighting",
        "volatileStatus": "noretreat"
    },
    "nothing": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "gravity": 1
        },
        "id": "nothing",
        "name": "Splash",
        "pp": 40,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "noxioustorque": {
        "accuracy": 100,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "failcopycat": 1,
            "failencore": 1,
            "failinstruct": 1,
            "failmefirst": 1,
            "failmimic": 1,
            "noassist": 1,
            "nosleeptalk": 1,
            "protect": 1
        },
        "id": "noxioustorque",
        "name": "Noxious Torque",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "status": "psn"
        },
        "target": "normal",
        "type": "poison"
    },
    "nuzzle": {
        "accuracy": 100,
        "basePower": 20,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "nuzzle",
        "name": "Nuzzle",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "chance": 100,
            "status": "par"
        },
        "target": "normal",
        "type": "electric"
    },
    "oblivionwing": {
        "accuracy": 100,
        "basePower": 80,
        "category": "special",
        "drain": [
            3,
            4
        ],
        "flags": {
            "distance": 1,
            "heal": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "oblivionwing",
        "name": "Oblivion Wing",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "any",
        "type": "flying"
    },
    "obstruct": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "failinstruct": 1
        },
        "id": "obstruct",
        "name": "Obstruct",
        "pp": 10,
        "priority": 4,
        "secondary": None,
        "target": "self",
        "type": "dark",
        "volatileStatus": "protect"
    },
    "octazooka": {
        "accuracy": 85,
        "basePower": 65,
        "category": "special",
        "flags": {
            "bullet": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "octazooka",
        "name": "Octazooka",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "accuracy": -1
            },
            "chance": 50
        },
        "target": "normal",
        "type": "water"
    },
    "octolock": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "octolock",
        "name": "Octolock",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fighting",
        "volatileStatus": "octolock"
    },
    "odorsleuth": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "odorsleuth",
        "name": "Odor Sleuth",
        "pp": 40,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal",
        "volatileStatus": "foresight"
    },
    "ominouswind": {
        "accuracy": 100,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "ominouswind",
        "name": "Ominous Wind",
        "pp": 5,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "self": {
                "boosts": {
                    "attack": 1,
                    "defense": 1,
                    "special-attack": 1,
                    "special-defense": 1,
                    "speed": 1
                }
            }
        },
        "target": "normal",
        "type": "ghost"
    },
    "orderup": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "protect": 1
        },
        "hasSheerForce": True,
        "id": "orderup",
        "name": "Order Up",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dragon"
    },
    "originpulse": {
        "accuracy": 85,
        "basePower": 110,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "pulse": 1
        },
        "id": "originpulse",
        "name": "Origin Pulse",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "water"
    },
    "outrage": {
        "accuracy": 100,
        "basePower": 120,
        "category": "physical",
        "flags": {
            "contact": 1,
            "failinstruct": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "outrage",
        "name": "Outrage",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "self": {
            "volatileStatus": "lockedmove"
        },
        "target": "randomNormal",
        "type": "dragon"
    },
    "overdrive": {
        "accuracy": 100,
        "basePower": 80,
        "category": "special",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "sound": 1
        },
        "id": "overdrive",
        "name": "Overdrive",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "electric"
    },
    "overheat": {
        "accuracy": 90,
        "basePower": 130,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "overheat",
        "name": "Overheat",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {
            "boosts": {
                "special-attack": -2
            }
        },
        "target": "normal",
        "type": "fire"
    },
    "painsplit": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "painsplit",
        "name": "Pain Split",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "paleowave": {
        "accuracy": 100,
        "basePower": 85,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "paleowave",
        "name": "Paleo Wave",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "boosts": {
                "attack": -1
            },
            "chance": 20
        },
        "target": "normal",
        "type": "rock"
    },
    "paraboliccharge": {
        "accuracy": 100,
        "basePower": 65,
        "category": "special",
        "drain": [
            1,
            2
        ],
        "flags": {
            "heal": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "paraboliccharge",
        "name": "Parabolic Charge",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacent",
        "type": "electric"
    },
    "partingshot": {
        "accuracy": 100,
        "basePower": 0,
        "boosts": {
            "attack": -1,
            "special-attack": -1
        },
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1,
            "sound": 1
        },
        "id": "partingshot",
        "name": "Parting Shot",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark"
    },
    "payback": {
        "accuracy": 100,
        "basePower": 50,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "payback",
        "name": "Payback",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark"
    },
    "payday": {
        "accuracy": 100,
        "basePower": 40,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "payday",
        "name": "Pay Day",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "peck": {
        "accuracy": 100,
        "basePower": 35,
        "category": "physical",
        "flags": {
            "contact": 1,
            "distance": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "peck",
        "name": "Peck",
        "pp": 35,
        "priority": 0,
        "secondary": None,
        "target": "any",
        "type": "flying"
    },
    "perishsong": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "distance": 1,
            "sound": 1
        },
        "id": "perishsong",
        "name": "Perish Song",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "all",
        "type": "normal"
    },
    "petalblizzard": {
        "accuracy": 100,
        "basePower": 90,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "wind": 1
        },
        "id": "petalblizzard",
        "name": "Petal Blizzard",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacent",
        "type": "grass"
    },
    "petaldance": {
        "accuracy": 100,
        "basePower": 120,
        "category": "special",
        "flags": {
            "contact": 1,
            "dance": 1,
            "failinstruct": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "petaldance",
        "name": "Petal Dance",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "self": {
            "volatileStatus": "lockedmove"
        },
        "target": "randomNormal",
        "type": "grass"
    },
    "phantomforce": {
        "accuracy": 100,
        "basePower": 90,
        "category": "physical",
        "flags": {
            "charge": 1,
            "contact": 1,
            "failinstruct": 1,
            "mirror": 1,
            "noassist": 1,
            "nosleeptalk": 1
        },
        "id": "phantomforce",
        "name": "Phantom Force",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ghost"
    },
    "photongeyser": {
        "accuracy": 100,
        "basePower": 100,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "photongeyser",
        "ignoreAbility": True,
        "name": "Photon Geyser",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "pikapapow": {
        "accuracy": True,
        "basePower": 0,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "pikapapow",
        "name": "Pika Papow",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "electric"
    },
    "pinmissile": {
        "accuracy": 95,
        "basePower": 25,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "pinmissile",
        "multihit": [
            2,
            5
        ],
        "name": "Pin Missile",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "bug"
    },
    "plasmafists": {
        "accuracy": 100,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "punch": 1
        },
        "id": "plasmafists",
        "name": "Plasma Fists",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "electric"
    },
    "playnice": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "attack": -1
        },
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "reflectable": 1
        },
        "id": "playnice",
        "name": "Play Nice",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "playrough": {
        "accuracy": 90,
        "basePower": 90,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "playrough",
        "name": "Play Rough",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "attack": -1
            },
            "chance": 10
        },
        "target": "normal",
        "type": "fairy"
    },
    "pluck": {
        "accuracy": 100,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "contact": 1,
            "distance": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "pluck",
        "name": "Pluck",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "any",
        "type": "flying"
    },
    "poisonfang": {
        "accuracy": 100,
        "basePower": 50,
        "category": "physical",
        "flags": {
            "bite": 1,
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "poisonfang",
        "name": "Poison Fang",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "chance": 50,
            "status": "tox"
        },
        "target": "normal",
        "type": "poison"
    },
    "poisongas": {
        "accuracy": 90,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "poisongas",
        "name": "Poison Gas",
        "pp": 40,
        "priority": 0,
        "secondary": None,
        "status": "psn",
        "target": "allAdjacentFoes",
        "type": "poison"
    },
    "poisonjab": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "poisonjab",
        "name": "Poison Jab",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "status": "psn"
        },
        "target": "normal",
        "type": "poison"
    },
    "poisonpowder": {
        "accuracy": 75,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "powder": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "poisonpowder",
        "name": "Poison Powder",
        "pp": 35,
        "priority": 0,
        "secondary": None,
        "status": "psn",
        "target": "normal",
        "type": "poison"
    },
    "poisonsting": {
        "accuracy": 100,
        "basePower": 15,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "poisonsting",
        "name": "Poison Sting",
        "pp": 35,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "status": "psn"
        },
        "target": "normal",
        "type": "poison"
    },
    "poisontail": {
        "accuracy": 100,
        "basePower": 50,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "poisontail",
        "name": "Poison Tail",
        "pp": 25,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "status": "psn"
        },
        "target": "normal",
        "type": "poison"
    },
    "pollenpuff": {
        "accuracy": 100,
        "basePower": 90,
        "category": "special",
        "flags": {
            "allyanim": 1,
            "bullet": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "pollenpuff",
        "name": "Pollen Puff",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "bug"
    },
    "poltergeist": {
        "accuracy": 90,
        "basePower": 110,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "poltergeist",
        "name": "Poltergeist",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ghost"
    },
    "populationbomb": {
        "accuracy": 90,
        "basePower": 20,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "slicing": 1
        },
        "id": "populationbomb",
        "multiaccuracy": True,
        "multihit": 10,
        "name": "Population Bomb",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "pounce": {
        "accuracy": 100,
        "basePower": 50,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "pounce",
        "name": "Pounce",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "boosts": {
                "speed": -1
            },
            "chance": 100
        },
        "target": "normal",
        "type": "bug"
    },
    "pound": {
        "accuracy": 100,
        "basePower": 40,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "pound",
        "name": "Pound",
        "pp": 35,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "powder": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "powder": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "powder",
        "name": "Powder",
        "pp": 20,
        "priority": 1,
        "secondary": None,
        "target": "normal",
        "type": "bug",
        "volatileStatus": "powder"
    },
    "powdersnow": {
        "accuracy": 100,
        "basePower": 40,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "powdersnow",
        "name": "Powder Snow",
        "pp": 25,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "status": "frz"
        },
        "target": "allAdjacentFoes",
        "type": "ice"
    },
    "powergem": {
        "accuracy": 100,
        "basePower": 80,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "powergem",
        "name": "Power Gem",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "rock"
    },
    "powershift": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "powershift",
        "name": "Power Shift",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal",
        "volatileStatus": "powershift"
    },
    "powersplit": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "protect": 1
        },
        "id": "powersplit",
        "name": "Power Split",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "powerswap": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "powerswap",
        "name": "Power Swap",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "powertrick": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "powertrick",
        "name": "Power Trick",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "psychic",
        "volatileStatus": "powertrick"
    },
    "powertrip": {
        "accuracy": 100,
        "basePower": 20,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "powertrip",
        "name": "Power Trip",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark"
    },
    "poweruppunch": {
        "accuracy": 100,
        "basePower": 40,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "punch": 1
        },
        "id": "poweruppunch",
        "name": "Power-Up Punch",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "chance": 100,
            "self": {
                "boosts": {
                    "attack": 1
                }
            }
        },
        "target": "normal",
        "type": "fighting"
    },
    "powerwhip": {
        "accuracy": 85,
        "basePower": 120,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "powerwhip",
        "name": "Power Whip",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass"
    },
    "precipiceblades": {
        "accuracy": 85,
        "basePower": 120,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "nonsky": 1,
            "protect": 1
        },
        "id": "precipiceblades",
        "name": "Precipice Blades",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "ground"
    },
    "present": {
        "accuracy": 90,
        "basePower": 0,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "present",
        "name": "Present",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "prismaticlaser": {
        "accuracy": 100,
        "basePower": 160,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "recharge": 1
        },
        "id": "prismaticlaser",
        "name": "Prismatic Laser",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "self": {
            "volatileStatus": "mustrecharge"
        },
        "target": "normal",
        "type": "psychic"
    },
    "protect": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "failcopycat": 1,
            "noassist": 1
        },
        "id": "protect",
        "name": "Protect",
        "pp": 10,
        "priority": 4,
        "secondary": None,
        "target": "self",
        "type": "normal",
        "volatileStatus": "protect"
    },
    "psybeam": {
        "accuracy": 100,
        "basePower": 65,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "psybeam",
        "name": "Psybeam",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "volatileStatus": "confusion"
        },
        "target": "normal",
        "type": "psychic"
    },
    "psyblade": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "slicing": 1
        },
        "id": "psyblade",
        "name": "Psyblade",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "psychic": {
        "accuracy": 100,
        "basePower": 90,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "psychic",
        "name": "Psychic",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "special-defense": -1
            },
            "chance": 10
        },
        "target": "normal",
        "type": "psychic"
    },
    "psychicfangs": {
        "accuracy": 100,
        "basePower": 85,
        "category": "physical",
        "flags": {
            "bite": 1,
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "psychicfangs",
        "name": "Psychic Fangs",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "psychicterrain": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "nonsky": 1
        },
        "id": "psychicterrain",
        "name": "Psychic Terrain",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "all",
        "terrain": "psychicterrain",
        "type": "psychic"
    },
    "psychoboost": {
        "accuracy": 90,
        "basePower": 140,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "psychoboost",
        "name": "Psycho Boost",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {
            "boosts": {
                "special-attack": -2
            }
        },
        "target": "normal",
        "type": "psychic"
    },
    "psychocut": {
        "accuracy": 100,
        "basePower": 70,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "slicing": 1
        },
        "id": "psychocut",
        "name": "Psycho Cut",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "psychoshift": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "psychoshift",
        "name": "Psycho Shift",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "self": {},
        "target": "normal",
        "type": "psychic"
    },
    "psychup": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "bypasssub": 1
        },
        "id": "psychup",
        "name": "Psych Up",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "psyshieldbash": {
        "accuracy": 90,
        "basePower": 70,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "psyshieldbash",
        "name": "Psyshield Bash",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 100,
            "self": {
                "boosts": {
                    "defense": 1
                }
            }
        },
        "target": "normal",
        "type": "psychic"
    },
    "psyshock": {
        "accuracy": 100,
        "basePower": 80,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "psyshock",
        "name": "Psyshock",
        "overrideDefensiveStat": "defense",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "psystrike": {
        "accuracy": 100,
        "basePower": 100,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "psystrike",
        "name": "Psystrike",
        "overrideDefensiveStat": "defense",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "psywave": {
        "accuracy": 100,
        "basePower": 0,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "psywave",
        "name": "Psywave",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "punishment": {
        "accuracy": 100,
        "basePower": 0,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "punishment",
        "name": "Punishment",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark"
    },
    "purify": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "heal": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "purify",
        "name": "Purify",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "poison"
    },
    "pursuit": {
        "accuracy": 100,
        "basePower": 40,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "pursuit",
        "name": "Pursuit",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark"
    },
    "pyroball": {
        "accuracy": 90,
        "basePower": 120,
        "category": "physical",
        "flags": {
            "bullet": 1,
            "defrost": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "pyroball",
        "name": "Pyro Ball",
        "pp": 5,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "status": "brn"
        },
        "target": "normal",
        "type": "fire"
    },
    "quash": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "quash",
        "name": "Quash",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark"
    },
    "quickattack": {
        "accuracy": 100,
        "basePower": 40,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "quickattack",
        "name": "Quick Attack",
        "pp": 30,
        "priority": 1,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "quickguard": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "quickguard",
        "name": "Quick Guard",
        "pp": 15,
        "priority": 3,
        "secondary": None,
        "side_conditions": "quickguard",
        "target": "allySide",
        "type": "fighting"
    },
    "quiverdance": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "special-attack": 1,
            "special-defense": 1,
            "speed": 1
        },
        "category": "status",
        "flags": {
            "dance": 1,
            "snatch": 1
        },
        "id": "quiverdance",
        "name": "Quiver Dance",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "bug"
    },
    "rage": {
        "accuracy": 100,
        "basePower": 20,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "rage",
        "name": "Rage",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "self": {
            "volatileStatus": "rage"
        },
        "target": "normal",
        "type": "normal"
    },
    "ragefist": {
        "accuracy": 100,
        "basePower": 50,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "punch": 1
        },
        "id": "ragefist",
        "name": "Rage Fist",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ghost"
    },
    "ragepowder": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "failcopycat": 1,
            "noassist": 1,
            "powder": 1
        },
        "id": "ragepowder",
        "name": "Rage Powder",
        "pp": 20,
        "priority": 2,
        "secondary": None,
        "target": "self",
        "type": "bug",
        "volatileStatus": "ragepowder"
    },
    "ragingbull": {
        "accuracy": 100,
        "basePower": 90,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "ragingbull",
        "name": "Raging Bull",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "ragingfury": {
        "accuracy": 100,
        "basePower": 120,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "ragingfury",
        "name": "Raging Fury",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "self": {
            "volatileStatus": "lockedmove"
        },
        "target": "randomNormal",
        "type": "fire"
    },
    "raindance": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {},
        "id": "raindance",
        "name": "Rain Dance",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "all",
        "type": "water",
        "weather": "RainDance"
    },
    "rapidspin": {
        "accuracy": 100,
        "basePower": 50,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "rapidspin",
        "name": "Rapid Spin",
        "pp": 40,
        "priority": 0,
        "secondary": {
            "chance": 100,
            "self": {
                "boosts": {
                    "speed": 1
                }
            }
        },
        "target": "normal",
        "type": "normal"
    },
    "razorleaf": {
        "accuracy": 95,
        "basePower": 55,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "slicing": 1
        },
        "id": "razorleaf",
        "name": "Razor Leaf",
        "pp": 25,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "grass"
    },
    "razorshell": {
        "accuracy": 95,
        "basePower": 75,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "slicing": 1
        },
        "id": "razorshell",
        "name": "Razor Shell",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "defense": -1
            },
            "chance": 50
        },
        "target": "normal",
        "type": "water"
    },
    "razorwind": {
        "accuracy": 100,
        "basePower": 80,
        "category": "special",
        "flags": {
            "charge": 1,
            "failinstruct": 1,
            "mirror": 1,
            "nosleeptalk": 1,
            "protect": 1
        },
        "id": "razorwind",
        "name": "Razor Wind",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "normal"
    },
    "recharge": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {},
        "id": "nothing",
        "name": "Recharge",
        "pp": 40,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "recover": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "heal": 1,
            "snatch": 1
        },
        "heal": [
            1,
            2
        ],
        "heal_target": "self",
        "id": "recover",
        "name": "Recover",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "recycle": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "recycle",
        "name": "Recycle",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "reflect": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "reflect",
        "name": "Reflect",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "side_conditions": "reflect",
        "target": "allySide",
        "type": "psychic"
    },
    "reflecttype": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "bypasssub": 1,
            "protect": 1
        },
        "id": "reflecttype",
        "name": "Reflect Type",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "refresh": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "refresh",
        "name": "Refresh",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "relicsong": {
        "accuracy": 100,
        "basePower": 75,
        "category": "special",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "sound": 1
        },
        "id": "relicsong",
        "name": "Relic Song",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "status": "slp"
        },
        "target": "allAdjacentFoes",
        "type": "normal"
    },
    "rest": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "heal": 1,
            "snatch": 1
        },
        "heal": [
            1,
            1
        ],
        "heal_target": "self",
        "id": "rest",
        "name": "Rest",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "status": "slp",
        "target": "self",
        "type": "psychic"
    },
    "retaliate": {
        "accuracy": 100,
        "basePower": 70,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "retaliate",
        "name": "Retaliate",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "return": {
        "accuracy": 100,
        "basePower": 102,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "return",
        "name": "Return",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "return102": {
        "accuracy": 100,
        "basePower": 102,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "return102",
        "name": "Return",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "revelationdance": {
        "accuracy": 100,
        "basePower": 90,
        "category": "special",
        "flags": {
            "dance": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "revelationdance",
        "name": "Revelation Dance",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "revenge": {
        "accuracy": 100,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "revenge",
        "name": "Revenge",
        "pp": 10,
        "priority": -4,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "reversal": {
        "accuracy": 100,
        "basePower": 0,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "reversal",
        "name": "Reversal",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "revivalblessing": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {},
        "id": "revivalblessing",
        "name": "Revival Blessing",
        "noPPBoosts": True,
        "pp": 1,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "risingvoltage": {
        "accuracy": 100,
        "basePower": 70,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "risingvoltage",
        "name": "Rising Voltage",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "electric"
    },
    "roar": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "bypasssub": 1,
            "drag": 1,
            "failcopycat": 1,
            "mirror": 1,
            "noassist": 1,
            "reflectable": 1,
            "sound": 1
        },
        "id": "roar",
        "name": "Roar",
        "pp": 20,
        "priority": -6,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "roaroftime": {
        "accuracy": 90,
        "basePower": 150,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "recharge": 1
        },
        "id": "roaroftime",
        "name": "Roar of Time",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {
            "volatileStatus": "mustrecharge"
        },
        "target": "normal",
        "type": "dragon"
    },
    "rockblast": {
        "accuracy": 90,
        "basePower": 25,
        "category": "physical",
        "flags": {
            "bullet": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "rockblast",
        "multihit": [
            2,
            5
        ],
        "name": "Rock Blast",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "rock"
    },
    "rockclimb": {
        "accuracy": 85,
        "basePower": 90,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "rockclimb",
        "name": "Rock Climb",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "chance": 20,
            "volatileStatus": "confusion"
        },
        "target": "normal",
        "type": "normal"
    },
    "rockpolish": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "speed": 2
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "rockpolish",
        "name": "Rock Polish",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "rock"
    },
    "rockslide": {
        "accuracy": 90,
        "basePower": 75,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "rockslide",
        "name": "Rock Slide",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "volatileStatus": "flinch"
        },
        "target": "allAdjacentFoes",
        "type": "rock"
    },
    "rocksmash": {
        "accuracy": 100,
        "basePower": 40,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "rocksmash",
        "name": "Rock Smash",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "boosts": {
                "defense": -1
            },
            "chance": 50
        },
        "target": "normal",
        "type": "fighting"
    },
    "rockthrow": {
        "accuracy": 90,
        "basePower": 50,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "rockthrow",
        "name": "Rock Throw",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "rock"
    },
    "rocktomb": {
        "accuracy": 95,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "rocktomb",
        "name": "Rock Tomb",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "boosts": {
                "speed": -1
            },
            "chance": 100
        },
        "target": "normal",
        "type": "rock"
    },
    "rockwrecker": {
        "accuracy": 90,
        "basePower": 150,
        "category": "physical",
        "flags": {
            "bullet": 1,
            "mirror": 1,
            "protect": 1,
            "recharge": 1
        },
        "id": "rockwrecker",
        "name": "Rock Wrecker",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {
            "volatileStatus": "mustrecharge"
        },
        "target": "normal",
        "type": "rock"
    },
    "roleplay": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "bypasssub": 1
        },
        "id": "roleplay",
        "name": "Role Play",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "rollingkick": {
        "accuracy": 85,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "rollingkick",
        "name": "Rolling Kick",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "volatileStatus": "flinch"
        },
        "target": "normal",
        "type": "fighting"
    },
    "rollout": {
        "accuracy": 90,
        "basePower": 30,
        "category": "physical",
        "flags": {
            "contact": 1,
            "failinstruct": 1,
            "mirror": 1,
            "noparentalbond": 1,
            "protect": 1
        },
        "id": "rollout",
        "name": "Rollout",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "rock"
    },
    "roost": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "heal": 1,
            "snatch": 1
        },
        "heal": [
            1,
            2
        ],
        "heal_target": "self",
        "id": "roost",
        "name": "Roost",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {
            "volatileStatus": "roost"
        },
        "target": "self",
        "type": "flying",
        "volatileStatus": "roost"
    },
    "rototiller": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "distance": 1,
            "nonsky": 1
        },
        "id": "rototiller",
        "name": "Rototiller",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "all",
        "type": "ground"
    },
    "round": {
        "accuracy": 100,
        "basePower": 60,
        "category": "special",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "sound": 1
        },
        "id": "round",
        "name": "Round",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "ruination": {
        "accuracy": 90,
        "basePower": 0,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "ruination",
        "name": "Ruination",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark"
    },
    "sacredfire": {
        "accuracy": 95,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "defrost": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "sacredfire",
        "name": "Sacred Fire",
        "pp": 5,
        "priority": 0,
        "secondary": {
            "chance": 50,
            "status": "brn"
        },
        "target": "normal",
        "type": "fire"
    },
    "sacredsword": {
        "accuracy": 100,
        "basePower": 90,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "slicing": 1
        },
        "id": "sacredsword",
        "name": "Sacred Sword",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "safeguard": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "safeguard",
        "name": "Safeguard",
        "pp": 25,
        "priority": 0,
        "secondary": None,
        "side_conditions": "safeguard",
        "target": "allySide",
        "type": "normal"
    },
    "saltcure": {
        "accuracy": 100,
        "basePower": 40,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "saltcure",
        "name": "Salt Cure",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "rock",
        "volatileStatus": "saltcure"
    },
    "sandattack": {
        "accuracy": 100,
        "basePower": 0,
        "boosts": {
            "accuracy": -1
        },
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "sandattack",
        "name": "Sand Attack",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ground"
    },
    "sandsearstorm": {
        "accuracy": 80,
        "basePower": 100,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "wind": 1
        },
        "id": "sandsearstorm",
        "name": "Sandsear Storm",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 20,
            "status": "brn"
        },
        "target": "allAdjacentFoes",
        "type": "ground"
    },
    "sandstorm": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "wind": 1
        },
        "id": "sandstorm",
        "name": "Sandstorm",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "all",
        "type": "rock",
        "weather": "Sandstorm"
    },
    "sandtomb": {
        "accuracy": 85,
        "basePower": 35,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "sandtomb",
        "name": "Sand Tomb",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ground",
        "volatileStatus": "partiallytrapped"
    },
    "sappyseed": {
        "accuracy": 90,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "sappyseed",
        "name": "Sappy Seed",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass"
    },
    "scald": {
        "accuracy": 100,
        "basePower": 80,
        "category": "special",
        "flags": {
            "defrost": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "scald",
        "name": "Scald",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "status": "brn"
        },
        "target": "normal",
        "thawsTarget": True,
        "type": "water"
    },
    "scaleshot": {
        "accuracy": 90,
        "basePower": 25,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "scaleshot",
        "multihit": [
            2,
            5
        ],
        "name": "Scale Shot",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "self": {
            "boosts": {
                "defense": -1,
                "speed": 1
            }
        },
        "target": "normal",
        "type": "dragon"
    },
    "scaryface": {
        "accuracy": 100,
        "basePower": 0,
        "boosts": {
            "speed": -2
        },
        "category": "status",
        "flags": {
            "allyanim": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "scaryface",
        "name": "Scary Face",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "scorchingsands": {
        "accuracy": 100,
        "basePower": 70,
        "category": "special",
        "flags": {
            "defrost": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "scorchingsands",
        "name": "Scorching Sands",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "status": "brn"
        },
        "target": "normal",
        "thawsTarget": True,
        "type": "ground"
    },
    "scratch": {
        "accuracy": 100,
        "basePower": 40,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "scratch",
        "name": "Scratch",
        "pp": 35,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "screech": {
        "accuracy": 85,
        "basePower": 0,
        "boosts": {
            "defense": -2
        },
        "category": "status",
        "flags": {
            "allyanim": 1,
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1,
            "sound": 1
        },
        "id": "screech",
        "name": "Screech",
        "pp": 40,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "searingshot": {
        "accuracy": 100,
        "basePower": 100,
        "category": "special",
        "flags": {
            "bullet": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "searingshot",
        "name": "Searing Shot",
        "pp": 5,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "status": "brn"
        },
        "target": "allAdjacent",
        "type": "fire"
    },
    "secretpower": {
        "accuracy": 100,
        "basePower": 70,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "secretpower",
        "name": "Secret Power",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "status": "par"
        },
        "target": "normal",
        "type": "normal"
    },
    "secretsword": {
        "accuracy": 100,
        "basePower": 85,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "secretsword",
        "name": "Secret Sword",
        "overrideDefensiveStat": "defense",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "seedbomb": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "bullet": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "seedbomb",
        "name": "Seed Bomb",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass"
    },
    "seedflare": {
        "accuracy": 85,
        "basePower": 120,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "seedflare",
        "name": "Seed Flare",
        "pp": 5,
        "priority": 0,
        "secondary": {
            "boosts": {
                "special-defense": -2
            },
            "chance": 40
        },
        "target": "normal",
        "type": "grass"
    },
    "seismictoss": {
        "accuracy": 100,
        "basePower": 0,
        "category": "physical",
        "damage": "level",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "nonsky": 1,
            "protect": 1
        },
        "id": "seismictoss",
        "name": "Seismic Toss",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "selfdestruct": {
        "accuracy": 100,
        "basePower": 200,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "noparentalbond": 1,
            "protect": 1
        },
        "heal": [
            -1,
            1
        ],
        "heal_target": "self",
        "id": "selfdestruct",
        "name": "Self-Destruct",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacent",
        "type": "normal"
    },
    "shadowball": {
        "accuracy": 100,
        "basePower": 80,
        "category": "special",
        "flags": {
            "bullet": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "shadowball",
        "name": "Shadow Ball",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "boosts": {
                "special-defense": -1
            },
            "chance": 20
        },
        "target": "normal",
        "type": "ghost"
    },
    "shadowbone": {
        "accuracy": 100,
        "basePower": 85,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "shadowbone",
        "name": "Shadow Bone",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "defense": -1
            },
            "chance": 20
        },
        "target": "normal",
        "type": "ghost"
    },
    "shadowclaw": {
        "accuracy": 100,
        "basePower": 70,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "shadowclaw",
        "name": "Shadow Claw",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ghost"
    },
    "shadowforce": {
        "accuracy": 100,
        "basePower": 120,
        "category": "physical",
        "flags": {
            "charge": 1,
            "contact": 1,
            "failinstruct": 1,
            "mirror": 1,
            "noassist": 1,
            "nosleeptalk": 1
        },
        "id": "shadowforce",
        "name": "Shadow Force",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ghost"
    },
    "shadowpunch": {
        "accuracy": True,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "punch": 1
        },
        "id": "shadowpunch",
        "name": "Shadow Punch",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ghost"
    },
    "shadowsneak": {
        "accuracy": 100,
        "basePower": 40,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "shadowsneak",
        "name": "Shadow Sneak",
        "pp": 30,
        "priority": 1,
        "secondary": None,
        "target": "normal",
        "type": "ghost"
    },
    "shadowstrike": {
        "accuracy": 95,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "shadowstrike",
        "name": "Shadow Strike",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "defense": -1
            },
            "chance": 50
        },
        "target": "normal",
        "type": "ghost"
    },
    "sharpen": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "attack": 1
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "sharpen",
        "name": "Sharpen",
        "pp": 30,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "shedtail": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {},
        "id": "shedtail",
        "name": "Shed Tail",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "self": {},
        "target": "self",
        "type": "normal",
        "volatileStatus": "substitute"
    },
    "sheercold": {
        "accuracy": 30,
        "basePower": 0,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "sheercold",
        "name": "Sheer Cold",
        "ohko": "Ice",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ice"
    },
    "shellsidearm": {
        "accuracy": 100,
        "basePower": 90,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "shellsidearm",
        "name": "Shell Side Arm",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 20,
            "status": "psn"
        },
        "target": "normal",
        "type": "poison"
    },
    "shellsmash": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "attack": 2,
            "defense": -1,
            "special-attack": 2,
            "special-defense": -1,
            "speed": 2
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "shellsmash",
        "name": "Shell Smash",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "shelltrap": {
        "accuracy": 100,
        "basePower": 150,
        "category": "special",
        "flags": {
            "failcopycat": 1,
            "failinstruct": 1,
            "failmefirst": 1,
            "noassist": 1,
            "nosleeptalk": 1,
            "protect": 1
        },
        "id": "shelltrap",
        "name": "Shell Trap",
        "pp": 5,
        "priority": -3,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "fire"
    },
    "shelter": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "defense": 2
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "shelter",
        "name": "Shelter",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "steel"
    },
    "shiftgear": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "attack": 1,
            "speed": 2
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "shiftgear",
        "name": "Shift Gear",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "steel"
    },
    "shockwave": {
        "accuracy": True,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "shockwave",
        "name": "Shock Wave",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "electric"
    },
    "shoreup": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "heal": 1,
            "snatch": 1
        },
        "id": "shoreup",
        "name": "Shore Up",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "ground"
    },
    "signalbeam": {
        "accuracy": 100,
        "basePower": 75,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "signalbeam",
        "name": "Signal Beam",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "volatileStatus": "confusion"
        },
        "target": "normal",
        "type": "bug"
    },
    "silktrap": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {},
        "id": "silktrap",
        "name": "Silk Trap",
        "pp": 10,
        "priority": 4,
        "secondary": None,
        "target": "self",
        "type": "bug",
        "volatileStatus": "silktrap"
    },
    "silverwind": {
        "accuracy": 100,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "silverwind",
        "name": "Silver Wind",
        "pp": 5,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "self": {
                "boosts": {
                    "attack": 1,
                    "defense": 1,
                    "special-attack": 1,
                    "special-defense": 1,
                    "speed": 1
                }
            }
        },
        "target": "normal",
        "type": "bug"
    },
    "simplebeam": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "simplebeam",
        "name": "Simple Beam",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "sing": {
        "accuracy": 55,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1,
            "sound": 1
        },
        "id": "sing",
        "name": "Sing",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "status": "slp",
        "target": "normal",
        "type": "normal"
    },
    "sizzlyslide": {
        "accuracy": 100,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "contact": 1,
            "defrost": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "sizzlyslide",
        "name": "Sizzly Slide",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "chance": 100,
            "status": "brn"
        },
        "target": "normal",
        "type": "fire"
    },
    "sketch": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "bypasssub": 1,
            "failcopycat": 1,
            "failencore": 1,
            "failinstruct": 1,
            "failmimic": 1,
            "noassist": 1,
            "nosleeptalk": 1
        },
        "id": "sketch",
        "name": "Sketch",
        "noPPBoosts": True,
        "pp": 1,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "skillswap": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "skillswap",
        "name": "Skill Swap",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "skittersmack": {
        "accuracy": 90,
        "basePower": 70,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "skittersmack",
        "name": "Skitter Smack",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "special-attack": -1
            },
            "chance": 100
        },
        "target": "normal",
        "type": "bug"
    },
    "skullbash": {
        "accuracy": 100,
        "basePower": 130,
        "category": "physical",
        "flags": {
            "charge": 1,
            "contact": 1,
            "failinstruct": 1,
            "mirror": 1,
            "nosleeptalk": 1,
            "protect": 1
        },
        "id": "skullbash",
        "name": "Skull Bash",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "skyattack": {
        "accuracy": 90,
        "basePower": 140,
        "category": "physical",
        "flags": {
            "charge": 1,
            "distance": 1,
            "failinstruct": 1,
            "mirror": 1,
            "nosleeptalk": 1,
            "protect": 1
        },
        "id": "skyattack",
        "name": "Sky Attack",
        "pp": 5,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "volatileStatus": "flinch"
        },
        "target": "any",
        "type": "flying"
    },
    "skydrop": {
        "accuracy": 100,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "charge": 1,
            "contact": 1,
            "distance": 1,
            "failinstruct": 1,
            "gravity": 1,
            "mirror": 1,
            "noassist": 1,
            "nosleeptalk": 1,
            "protect": 1
        },
        "id": "skydrop",
        "name": "Sky Drop",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "any",
        "type": "flying"
    },
    "skyuppercut": {
        "accuracy": 90,
        "basePower": 85,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "punch": 1
        },
        "id": "skyuppercut",
        "name": "Sky Uppercut",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "slackoff": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "heal": 1,
            "snatch": 1
        },
        "heal": [
            1,
            2
        ],
        "heal_target": "self",
        "id": "slackoff",
        "name": "Slack Off",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "slam": {
        "accuracy": 75,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "nonsky": 1,
            "protect": 1
        },
        "id": "slam",
        "name": "Slam",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "slash": {
        "accuracy": 100,
        "basePower": 70,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "slicing": 1
        },
        "id": "slash",
        "name": "Slash",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "sleeppowder": {
        "accuracy": 75,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "powder": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "sleeppowder",
        "name": "Sleep Powder",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "status": "slp",
        "target": "normal",
        "type": "grass"
    },
    "sleeptalk": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "failcopycat": 1,
            "failencore": 1,
            "failinstruct": 1,
            "failmimic": 1,
            "noassist": 1,
            "nosleeptalk": 1
        },
        "id": "sleeptalk",
        "name": "Sleep Talk",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "sleepUsable": True,
        "target": "self",
        "type": "normal"
    },
    "sludge": {
        "accuracy": 100,
        "basePower": 65,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "sludge",
        "name": "Sludge",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "status": "psn"
        },
        "target": "normal",
        "type": "poison"
    },
    "sludgebomb": {
        "accuracy": 100,
        "basePower": 90,
        "category": "special",
        "flags": {
            "bullet": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "sludgebomb",
        "name": "Sludge Bomb",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "status": "psn"
        },
        "target": "normal",
        "type": "poison"
    },
    "sludgewave": {
        "accuracy": 100,
        "basePower": 95,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "sludgewave",
        "name": "Sludge Wave",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "status": "psn"
        },
        "target": "allAdjacent",
        "type": "poison"
    },
    "smackdown": {
        "accuracy": 100,
        "basePower": 50,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "nonsky": 1,
            "protect": 1
        },
        "id": "smackdown",
        "name": "Smack Down",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "rock",
        "volatileStatus": "smackdown"
    },
    "smartstrike": {
        "accuracy": True,
        "basePower": 70,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "smartstrike",
        "name": "Smart Strike",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "steel"
    },
    "smellingsalts": {
        "accuracy": 100,
        "basePower": 70,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "smellingsalts",
        "name": "Smelling Salts",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "smog": {
        "accuracy": 70,
        "basePower": 30,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "smog",
        "name": "Smog",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "chance": 40,
            "status": "psn"
        },
        "target": "normal",
        "type": "poison"
    },
    "smokescreen": {
        "accuracy": 100,
        "basePower": 0,
        "boosts": {
            "accuracy": -1
        },
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "smokescreen",
        "name": "Smokescreen",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "snaptrap": {
        "accuracy": 100,
        "basePower": 35,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "snaptrap",
        "name": "Snap Trap",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass",
        "volatileStatus": "partiallytrapped"
    },
    "snarl": {
        "accuracy": 95,
        "basePower": 55,
        "category": "special",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "sound": 1
        },
        "id": "snarl",
        "name": "Snarl",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "boosts": {
                "special-attack": -1
            },
            "chance": 100
        },
        "target": "allAdjacentFoes",
        "type": "dark"
    },
    "snatch": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "failcopycat": 1,
            "mustpressure": 1,
            "noassist": 1
        },
        "id": "snatch",
        "name": "Snatch",
        "pp": 10,
        "priority": 4,
        "secondary": None,
        "target": "self",
        "type": "dark",
        "volatileStatus": "snatch"
    },
    "snipeshot": {
        "accuracy": 100,
        "basePower": 80,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "snipeshot",
        "name": "Snipe Shot",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "tracksTarget": True,
        "type": "water"
    },
    "snore": {
        "accuracy": 100,
        "basePower": 50,
        "category": "special",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "sound": 1
        },
        "id": "snore",
        "name": "Snore",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "volatileStatus": "flinch"
        },
        "sleepUsable": True,
        "target": "normal",
        "type": "normal"
    },
    "snowscape": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {},
        "id": "snowscape",
        "name": "Snowscape",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "all",
        "type": "ice",
        "weather": "snow"
    },
    "soak": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "soak",
        "name": "Soak",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "water"
    },
    "softboiled": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "heal": 1,
            "snatch": 1
        },
        "heal": [
            1,
            2
        ],
        "heal_target": "self",
        "id": "softboiled",
        "name": "Soft-Boiled",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "solarbeam": {
        "accuracy": 100,
        "basePower": 120,
        "category": "special",
        "flags": {
            "charge": 1,
            "failinstruct": 1,
            "mirror": 1,
            "nosleeptalk": 1,
            "protect": 1
        },
        "id": "solarbeam",
        "name": "Solar Beam",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass"
    },
    "solarblade": {
        "accuracy": 100,
        "basePower": 125,
        "category": "physical",
        "flags": {
            "charge": 1,
            "contact": 1,
            "failinstruct": 1,
            "mirror": 1,
            "nosleeptalk": 1,
            "protect": 1,
            "slicing": 1
        },
        "id": "solarblade",
        "name": "Solar Blade",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass"
    },
    "sonicboom": {
        "accuracy": 90,
        "basePower": 0,
        "category": "special",
        "damage": 20,
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "sonicboom",
        "name": "Sonic Boom",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "spacialrend": {
        "accuracy": 95,
        "basePower": 100,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "spacialrend",
        "name": "Spacial Rend",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dragon"
    },
    "spark": {
        "accuracy": 100,
        "basePower": 65,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "spark",
        "name": "Spark",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "status": "par"
        },
        "target": "normal",
        "type": "electric"
    },
    "sparklingaria": {
        "accuracy": 100,
        "basePower": 90,
        "category": "special",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "sound": 1
        },
        "id": "sparklingaria",
        "name": "Sparkling Aria",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 100,
            "dustproof": True,
            "volatileStatus": "sparklingaria"
        },
        "target": "allAdjacent",
        "type": "water"
    },
    "sparklyswirl": {
        "accuracy": 85,
        "basePower": 120,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "sparklyswirl",
        "name": "Sparkly Swirl",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {},
        "target": "normal",
        "type": "fairy"
    },
    "spectralthief": {
        "accuracy": 100,
        "basePower": 90,
        "category": "physical",
        "flags": {
            "bypasssub": 1,
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "spectralthief",
        "name": "Spectral Thief",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "stealsBoosts": True,
        "target": "normal",
        "type": "ghost"
    },
    "speedswap": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "speedswap",
        "name": "Speed Swap",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "spicyextract": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "attack": 2,
            "defense": -2
        },
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "spicyextract",
        "name": "Spicy Extract",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass"
    },
    "spiderweb": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "spiderweb",
        "name": "Spider Web",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "bug"
    },
    "spikecannon": {
        "accuracy": 100,
        "basePower": 20,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "spikecannon",
        "multihit": [
            2,
            5
        ],
        "name": "Spike Cannon",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "spikes": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mustpressure": 1,
            "nonsky": 1,
            "reflectable": 1
        },
        "id": "spikes",
        "name": "Spikes",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "side_conditions": "spikes",
        "target": "foeSide",
        "type": "ground"
    },
    "spikyshield": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "failcopycat": 1,
            "noassist": 1
        },
        "id": "spikyshield",
        "name": "Spiky Shield",
        "pp": 10,
        "priority": 4,
        "secondary": None,
        "target": "self",
        "type": "grass",
        "volatileStatus": "spikyshield"
    },
    "spinout": {
        "accuracy": 100,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "spinout",
        "name": "Spin Out",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {
            "boosts": {
                "speed": -2
            }
        },
        "target": "normal",
        "type": "steel"
    },
    "spiritbreak": {
        "accuracy": 100,
        "basePower": 75,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "spiritbreak",
        "name": "Spirit Break",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "boosts": {
                "special-attack": -1
            },
            "chance": 100
        },
        "target": "normal",
        "type": "fairy"
    },
    "spiritshackle": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "spiritshackle",
        "name": "Spirit Shackle",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ghost"
    },
    "spite": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "spite",
        "name": "Spite",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ghost"
    },
    "spitup": {
        "accuracy": 100,
        "basePower": 0,
        "category": "special",
        "flags": {
            "protect": 1
        },
        "id": "spitup",
        "name": "Spit Up",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "splash": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "gravity": 1
        },
        "id": "splash",
        "name": "Splash",
        "pp": 40,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "splishysplash": {
        "accuracy": 100,
        "basePower": 90,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "splishysplash",
        "name": "Splishy Splash",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "status": "par"
        },
        "target": "allAdjacentFoes",
        "type": "water"
    },
    "spore": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "powder": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "spore",
        "name": "Spore",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "status": "slp",
        "target": "normal",
        "type": "grass"
    },
    "spotlight": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "failcopycat": 1,
            "noassist": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "spotlight",
        "name": "Spotlight",
        "pp": 15,
        "priority": 3,
        "secondary": None,
        "target": "normal",
        "type": "normal",
        "volatileStatus": "spotlight"
    },
    "springtidestorm": {
        "accuracy": 80,
        "basePower": 100,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "wind": 1
        },
        "id": "springtidestorm",
        "name": "Springtide Storm",
        "pp": 5,
        "priority": 0,
        "secondary": {
            "boosts": {
                "attack": -1
            },
            "chance": 30
        },
        "target": "allAdjacentFoes",
        "type": "fairy"
    },
    "stealthrock": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mustpressure": 1,
            "reflectable": 1
        },
        "id": "stealthrock",
        "name": "Stealth Rock",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "side_conditions": "stealthrock",
        "target": "foeSide",
        "type": "rock"
    },
    "steameruption": {
        "accuracy": 95,
        "basePower": 110,
        "category": "special",
        "flags": {
            "defrost": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "steameruption",
        "name": "Steam Eruption",
        "pp": 5,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "status": "brn"
        },
        "target": "normal",
        "thawsTarget": True,
        "type": "water"
    },
    "steamroller": {
        "accuracy": 100,
        "basePower": 65,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "steamroller",
        "name": "Steamroller",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "volatileStatus": "flinch"
        },
        "target": "normal",
        "type": "bug"
    },
    "steelbeam": {
        "accuracy": 95,
        "basePower": 140,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "steelbeam",
        "name": "Steel Beam",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "steel"
    },
    "steelroller": {
        "accuracy": 100,
        "basePower": 130,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "steelroller",
        "name": "Steel Roller",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "steel"
    },
    "steelwing": {
        "accuracy": 90,
        "basePower": 70,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "steelwing",
        "name": "Steel Wing",
        "pp": 25,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "self": {
                "boosts": {
                    "defense": 1
                }
            }
        },
        "target": "normal",
        "type": "steel"
    },
    "stickyweb": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "reflectable": 1
        },
        "id": "stickyweb",
        "name": "Sticky Web",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "side_conditions": "stickyweb",
        "target": "foeSide",
        "type": "bug"
    },
    "stockpile": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "stockpile",
        "name": "Stockpile",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal",
        "volatileStatus": "stockpile"
    },
    "stomp": {
        "accuracy": 100,
        "basePower": 65,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "nonsky": 1,
            "protect": 1
        },
        "id": "stomp",
        "name": "Stomp",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "volatileStatus": "flinch"
        },
        "target": "normal",
        "type": "normal"
    },
    "stompingtantrum": {
        "accuracy": 100,
        "basePower": 75,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "stompingtantrum",
        "name": "Stomping Tantrum",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ground"
    },
    "stoneaxe": {
        "accuracy": 90,
        "basePower": 65,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "slicing": 1
        },
        "id": "stoneaxe",
        "name": "Stone Axe",
        "pp": 15,
        "priority": 0,
        "secondary": {},
        "side_conditions": "stealthrock",
        "target": "normal",
        "type": "rock"
    },
    "stoneedge": {
        "accuracy": 80,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "stoneedge",
        "name": "Stone Edge",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "rock"
    },
    "storedpower": {
        "accuracy": 100,
        "basePower": 20,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "storedpower",
        "name": "Stored Power",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "stormthrow": {
        "accuracy": 100,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "stormthrow",
        "name": "Storm Throw",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fighting",
        "willCrit": True
    },
    "strangesteam": {
        "accuracy": 95,
        "basePower": 90,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "strangesteam",
        "name": "Strange Steam",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 20,
            "volatileStatus": "confusion"
        },
        "target": "normal",
        "type": "fairy"
    },
    "strength": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "strength",
        "name": "Strength",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "strengthsap": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "heal": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "strengthsap",
        "name": "Strength Sap",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass"
    },
    "stringshot": {
        "accuracy": 95,
        "basePower": 0,
        "boosts": {
            "speed": -2
        },
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "stringshot",
        "name": "String Shot",
        "pp": 40,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "bug"
    },
    "struggle": {
        "accuracy": True,
        "basePower": 50,
        "category": "physical",
        "flags": {
            "contact": 1,
            "failcopycat": 1,
            "failencore": 1,
            "failinstruct": 1,
            "failmefirst": 1,
            "failmimic": 1,
            "noassist": 1,
            "nosleeptalk": 1,
            "protect": 1
        },
        "id": "struggle",
        "name": "Struggle",
        "noPPBoosts": True,
        "pp": 1,
        "priority": 0,
        "secondary": None,
        "struggleRecoil": True,
        "target": "randomNormal",
        "type": "normal"
    },
    "strugglebug": {
        "accuracy": 100,
        "basePower": 50,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "strugglebug",
        "name": "Struggle Bug",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "boosts": {
                "special-attack": -1
            },
            "chance": 100
        },
        "target": "allAdjacentFoes",
        "type": "bug"
    },
    "stuffcheeks": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "stuffcheeks",
        "name": "Stuff Cheeks",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "stunspore": {
        "accuracy": 75,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "powder": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "stunspore",
        "name": "Stun Spore",
        "pp": 30,
        "priority": 0,
        "secondary": None,
        "status": "par",
        "target": "normal",
        "type": "grass"
    },
    "submission": {
        "accuracy": 80,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "submission",
        "name": "Submission",
        "pp": 20,
        "priority": 0,
        "recoil": [
            1,
            4
        ],
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "substitute": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "nonsky": 1,
            "snatch": 1
        },
        "id": "substitute",
        "name": "Substitute",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal",
        "volatileStatus": "substitute"
    },
    "suckerpunch": {
        "accuracy": 100,
        "basePower": 70,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "suckerpunch",
        "name": "Sucker Punch",
        "pp": 5,
        "priority": 1,
        "secondary": None,
        "target": "normal",
        "type": "dark"
    },
    "sunnyday": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {},
        "id": "sunnyday",
        "name": "Sunny Day",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "all",
        "type": "fire",
        "weather": "sunnyday"
    },
    "sunsteelstrike": {
        "accuracy": 100,
        "basePower": 100,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "sunsteelstrike",
        "ignoreAbility": True,
        "name": "Sunsteel Strike",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "steel"
    },
    "superfang": {
        "accuracy": 90,
        "basePower": 0,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "superfang",
        "name": "Super Fang",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "superpower": {
        "accuracy": 100,
        "basePower": 120,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "superpower",
        "name": "Superpower",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {
            "boosts": {
                "attack": -1,
                "defense": -1
            }
        },
        "target": "normal",
        "type": "fighting"
    },
    "supersonic": {
        "accuracy": 55,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1,
            "sound": 1
        },
        "id": "supersonic",
        "name": "Supersonic",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal",
        "volatileStatus": "confusion"
    },
    "surf": {
        "accuracy": 100,
        "basePower": 90,
        "category": "special",
        "flags": {
            "mirror": 1,
            "nonsky": 1,
            "protect": 1
        },
        "id": "surf",
        "name": "Surf",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacent",
        "type": "water"
    },
    "surgingstrikes": {
        "accuracy": 100,
        "basePower": 25,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "punch": 1
        },
        "id": "surgingstrikes",
        "multihit": 3,
        "name": "Surging Strikes",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "water",
        "willCrit": True
    },
    "swagger": {
        "accuracy": 85,
        "basePower": 0,
        "boosts": {
            "attack": 2
        },
        "category": "status",
        "flags": {
            "allyanim": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "swagger",
        "name": "Swagger",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal",
        "volatileStatus": "confusion"
    },
    "swallow": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "heal": 1,
            "snatch": 1
        },
        "id": "swallow",
        "name": "Swallow",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "sweetkiss": {
        "accuracy": 75,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "sweetkiss",
        "name": "Sweet Kiss",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fairy",
        "volatileStatus": "confusion"
    },
    "sweetscent": {
        "accuracy": 100,
        "basePower": 0,
        "boosts": {
            "evasion": -2
        },
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "sweetscent",
        "name": "Sweet Scent",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "normal"
    },
    "swift": {
        "accuracy": True,
        "basePower": 60,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "swift",
        "name": "Swift",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "normal"
    },
    "switcheroo": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "failcopycat": 1,
            "mirror": 1,
            "noassist": 1,
            "protect": 1
        },
        "id": "switcheroo",
        "name": "Switcheroo",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark"
    },
    "swordsdance": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "attack": 2
        },
        "category": "status",
        "flags": {
            "dance": 1,
            "snatch": 1
        },
        "id": "swordsdance",
        "name": "Swords Dance",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "synchronoise": {
        "accuracy": 100,
        "basePower": 120,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "synchronoise",
        "name": "Synchronoise",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacent",
        "type": "psychic"
    },
    "synthesis": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "heal": 1,
            "snatch": 1
        },
        "heal": [
            1,
            2
        ],
        "heal_target": "self",
        "id": "synthesis",
        "name": "Synthesis",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "grass"
    },
    "tackle": {
        "accuracy": 100,
        "basePower": 40,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "tackle",
        "name": "Tackle",
        "pp": 35,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "tailglow": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "special-attack": 3
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "tailglow",
        "name": "Tail Glow",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "bug"
    },
    "tailslap": {
        "accuracy": 85,
        "basePower": 25,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "tailslap",
        "multihit": [
            2,
            5
        ],
        "name": "Tail Slap",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "tailwhip": {
        "accuracy": 100,
        "basePower": 0,
        "boosts": {
            "defense": -1
        },
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "tailwhip",
        "name": "Tail Whip",
        "pp": 30,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "normal"
    },
    "tailwind": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "snatch": 1,
            "wind": 1
        },
        "id": "tailwind",
        "name": "Tailwind",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "side_conditions": "tailwind",
        "target": "allySide",
        "type": "flying"
    },
    "takedown": {
        "accuracy": 85,
        "basePower": 90,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "takedown",
        "name": "Take Down",
        "pp": 20,
        "priority": 0,
        "recoil": [
            1,
            4
        ],
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "takeheart": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "takeheart",
        "name": "Take Heart",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "psychic"
    },
    "tarshot": {
        "accuracy": 100,
        "basePower": 0,
        "boosts": {
            "speed": -1
        },
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "tarshot",
        "name": "Tar Shot",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "rock",
        "volatileStatus": "tarshot"
    },
    "taunt": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "taunt",
        "name": "Taunt",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark",
        "volatileStatus": "taunt"
    },
    "tearfullook": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "attack": -1,
            "special-attack": -1
        },
        "category": "status",
        "flags": {
            "mirror": 1,
            "reflectable": 1
        },
        "id": "tearfullook",
        "name": "Tearful Look",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "teatime": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1
        },
        "id": "teatime",
        "name": "Teatime",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "all",
        "type": "normal"
    },
    "technoblast": {
        "accuracy": 100,
        "basePower": 120,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "technoblast",
        "name": "Techno Blast",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "teeterdance": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "dance": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "teeterdance",
        "name": "Teeter Dance",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacent",
        "type": "normal",
        "volatileStatus": "confusion"
    },
    "telekinesis": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "gravity": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "telekinesis",
        "name": "Telekinesis",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic",
        "volatileStatus": "telekinesis"
    },
    "teleport": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {},
        "id": "teleport",
        "name": "Teleport",
        "pp": 20,
        "priority": -6,
        "secondary": None,
        "target": "self",
        "type": "psychic"
    },
    "terablast": {
        "accuracy": 100,
        "basePower": 80,
        "category": "special",
        "flags": {
            "mirror": 1,
            "mustpressure": 1,
            "protect": 1
        },
        "id": "terablast",
        "name": "Tera Blast",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "terrainpulse": {
        "accuracy": 100,
        "basePower": 50,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "pulse": 1
        },
        "id": "terrainpulse",
        "name": "Terrain Pulse",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "thief": {
        "accuracy": 100,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "contact": 1,
            "failcopycat": 1,
            "failmefirst": 1,
            "mirror": 1,
            "noassist": 1,
            "protect": 1
        },
        "id": "thief",
        "name": "Thief",
        "pp": 25,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark"
    },
    "thousandarrows": {
        "accuracy": 100,
        "basePower": 90,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "nonsky": 1,
            "protect": 1
        },
        "id": "thousandarrows",
        "name": "Thousand Arrows",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "ground",
        "volatileStatus": "smackdown"
    },
    "thousandwaves": {
        "accuracy": 100,
        "basePower": 90,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "nonsky": 1,
            "protect": 1
        },
        "id": "thousandwaves",
        "name": "Thousand Waves",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "ground"
    },
    "thrash": {
        "accuracy": 100,
        "basePower": 120,
        "category": "physical",
        "flags": {
            "contact": 1,
            "failinstruct": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "thrash",
        "name": "Thrash",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "self": {
            "volatileStatus": "lockedmove"
        },
        "target": "randomNormal",
        "type": "normal"
    },
    "throatchop": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "throatchop",
        "name": "Throat Chop",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark",
        "volatileStatus": "throatchop"
    },
    "thunder": {
        "accuracy": 70,
        "basePower": 110,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "thunder",
        "name": "Thunder",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "status": "par"
        },
        "target": "normal",
        "type": "electric"
    },
    "thunderbolt": {
        "accuracy": 100,
        "basePower": 90,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "thunderbolt",
        "name": "Thunderbolt",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "status": "par"
        },
        "target": "normal",
        "type": "electric"
    },
    "thundercage": {
        "accuracy": 90,
        "basePower": 80,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "thundercage",
        "name": "Thunder Cage",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "electric",
        "volatileStatus": "partiallytrapped"
    },
    "thunderfang": {
        "accuracy": 95,
        "basePower": 65,
        "category": "physical",
        "flags": {
            "bite": 1,
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "thunderfang",
        "name": "Thunder Fang",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "electric"
    },
    "thunderouskick": {
        "accuracy": 100,
        "basePower": 90,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "thunderouskick",
        "name": "Thunderous Kick",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "boosts": {
                "defense": -1
            },
            "chance": 100
        },
        "target": "normal",
        "type": "fighting"
    },
    "thunderpunch": {
        "accuracy": 100,
        "basePower": 75,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "punch": 1
        },
        "id": "thunderpunch",
        "name": "Thunder Punch",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "status": "par"
        },
        "target": "normal",
        "type": "electric"
    },
    "thundershock": {
        "accuracy": 100,
        "basePower": 40,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "thundershock",
        "name": "Thunder Shock",
        "pp": 30,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "status": "par"
        },
        "target": "normal",
        "type": "electric"
    },
    "thunderwave": {
        "accuracy": 90,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "thunderwave",
        "name": "Thunder Wave",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "status": "par",
        "target": "normal",
        "type": "electric"
    },
    "tickle": {
        "accuracy": 100,
        "basePower": 0,
        "boosts": {
            "attack": -1,
            "defense": -1
        },
        "category": "status",
        "flags": {
            "allyanim": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "tickle",
        "name": "Tickle",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "tidyup": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "attack": 1,
            "speed": 1
        },
        "category": "status",
        "flags": {},
        "id": "tidyup",
        "name": "Tidy Up",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "topsyturvy": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "topsyturvy",
        "name": "Topsy-Turvy",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark"
    },
    "torchsong": {
        "accuracy": 100,
        "basePower": 80,
        "category": "special",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "sound": 1
        },
        "id": "torchsong",
        "name": "Torch Song",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 100,
            "self": {
                "boosts": {
                    "special-attack": 1
                }
            }
        },
        "target": "normal",
        "type": "fire"
    },
    "torment": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "bypasssub": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "torment",
        "name": "Torment",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark",
        "volatileStatus": "torment"
    },
    "toxic": {
        "accuracy": 90,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "toxic",
        "name": "Toxic",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "status": "tox",
        "target": "normal",
        "type": "poison"
    },
    "toxicspikes": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mustpressure": 1,
            "nonsky": 1,
            "reflectable": 1
        },
        "id": "toxicspikes",
        "name": "Toxic Spikes",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "side_conditions": "toxicspikes",
        "target": "foeSide",
        "type": "poison"
    },
    "toxicthread": {
        "accuracy": 100,
        "basePower": 0,
        "boosts": {
            "speed": -1
        },
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "toxicthread",
        "name": "Toxic Thread",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "status": "psn",
        "target": "normal",
        "type": "poison"
    },
    "trailblaze": {
        "accuracy": 100,
        "basePower": 50,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "trailblaze",
        "name": "Trailblaze",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "chance": 100,
            "self": {
                "boosts": {
                    "speed": 1
                }
            }
        },
        "target": "normal",
        "type": "grass"
    },
    "transform": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "failcopycat": 1,
            "failencore": 1,
            "failinstruct": 1,
            "failmimic": 1,
            "noassist": 1
        },
        "id": "transform",
        "name": "Transform",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "triattack": {
        "accuracy": 100,
        "basePower": 80,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "triattack",
        "name": "Tri Attack",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "trick": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "failcopycat": 1,
            "mirror": 1,
            "noassist": 1,
            "protect": 1
        },
        "id": "trick",
        "name": "Trick",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "trickortreat": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "trickortreat",
        "name": "Trick-or-Treat",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ghost"
    },
    "trickroom": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1
        },
        "id": "trickroom",
        "name": "Trick Room",
        "pp": 5,
        "priority": -7,
        "secondary": None,
        "target": "all",
        "type": "psychic"
    },
    "triplearrows": {
        "accuracy": 100,
        "basePower": 90,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "triplearrows",
        "name": "Triple Arrows",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "tripleaxel": {
        "accuracy": 90,
        "basePower": 20,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "tripleaxel",
        "multiaccuracy": True,
        "multihit": 3,
        "name": "Triple Axel",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "ice"
    },
    "tripledive": {
        "accuracy": 95,
        "basePower": 30,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "tripledive",
        "multihit": 3,
        "name": "Triple Dive",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "water"
    },
    "triplekick": {
        "accuracy": 90,
        "basePower": 10,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "triplekick",
        "multiaccuracy": True,
        "multihit": 3,
        "name": "Triple Kick",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "tropkick": {
        "accuracy": 100,
        "basePower": 70,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "tropkick",
        "name": "Trop Kick",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "boosts": {
                "attack": -1
            },
            "chance": 100
        },
        "target": "normal",
        "type": "grass"
    },
    "trumpcard": {
        "accuracy": True,
        "basePower": 0,
        "category": "special",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "trumpcard",
        "name": "Trump Card",
        "noPPBoosts": True,
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "twinbeam": {
        "accuracy": 100,
        "basePower": 40,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "twinbeam",
        "multihit": 2,
        "name": "Twin Beam",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "psychic"
    },
    "twineedle": {
        "accuracy": 100,
        "basePower": 25,
        "category": "physical",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "twineedle",
        "multihit": 2,
        "name": "Twineedle",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "chance": 20,
            "status": "psn"
        },
        "target": "normal",
        "type": "bug"
    },
    "twister": {
        "accuracy": 100,
        "basePower": 40,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "wind": 1
        },
        "id": "twister",
        "name": "Twister",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "chance": 20,
            "volatileStatus": "flinch"
        },
        "target": "allAdjacentFoes",
        "type": "dragon"
    },
    "uproar": {
        "accuracy": 100,
        "basePower": 90,
        "category": "special",
        "flags": {
            "bypasssub": 1,
            "failinstruct": 1,
            "mirror": 1,
            "nosleeptalk": 1,
            "protect": 1,
            "sound": 1
        },
        "id": "uproar",
        "name": "Uproar",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "self": {
            "volatileStatus": "uproar"
        },
        "target": "randomNormal",
        "type": "normal"
    },
    "uturn": {
        "accuracy": 100,
        "basePower": 70,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "uturn",
        "name": "U-turn",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "bug"
    },
    "vacuumwave": {
        "accuracy": 100,
        "basePower": 40,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "vacuumwave",
        "name": "Vacuum Wave",
        "pp": 30,
        "priority": 1,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "vcreate": {
        "accuracy": 95,
        "basePower": 180,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "vcreate",
        "name": "V-create",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "self": {
            "boosts": {
                "defense": -1,
                "special-defense": -1,
                "speed": -1
            }
        },
        "target": "normal",
        "type": "fire"
    },
    "veeveevolley": {
        "accuracy": True,
        "basePower": 0,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "veeveevolley",
        "name": "Veevee Volley",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "venomdrench": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "venomdrench",
        "name": "Venom Drench",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "poison"
    },
    "venoshock": {
        "accuracy": 100,
        "basePower": 65,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "venoshock",
        "name": "Venoshock",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "poison"
    },
    "victorydance": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "attack": 1,
            "defense": 1,
            "speed": 1
        },
        "category": "status",
        "flags": {
            "dance": 1,
            "snatch": 1
        },
        "id": "victorydance",
        "name": "Victory Dance",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "fighting"
    },
    "vinewhip": {
        "accuracy": 100,
        "basePower": 45,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "vinewhip",
        "name": "Vine Whip",
        "pp": 25,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass"
    },
    "visegrip": {
        "accuracy": 100,
        "basePower": 55,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "visegrip",
        "name": "Vise Grip",
        "pp": 30,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "vitalthrow": {
        "accuracy": True,
        "basePower": 70,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "vitalthrow",
        "name": "Vital Throw",
        "pp": 10,
        "priority": -1,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "voltswitch": {
        "accuracy": 100,
        "basePower": 70,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "voltswitch",
        "name": "Volt Switch",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "electric"
    },
    "volttackle": {
        "accuracy": 100,
        "basePower": 120,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "volttackle",
        "name": "Volt Tackle",
        "pp": 15,
        "priority": 0,
        "recoil": [
            1,
            3
        ],
        "secondary": {
            "chance": 10,
            "status": "par"
        },
        "target": "normal",
        "type": "electric"
    },
    "wakeupslap": {
        "accuracy": 100,
        "basePower": 70,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "wakeupslap",
        "name": "Wake-Up Slap",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "fighting"
    },
    "waterfall": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "waterfall",
        "name": "Waterfall",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "chance": 20,
            "volatileStatus": "flinch"
        },
        "target": "normal",
        "type": "water"
    },
    "watergun": {
        "accuracy": 100,
        "basePower": 40,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "watergun",
        "name": "Water Gun",
        "pp": 25,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "water"
    },
    "waterpledge": {
        "accuracy": 100,
        "basePower": 80,
        "category": "special",
        "flags": {
            "mirror": 1,
            "nonsky": 1,
            "pledgecombo": 1,
            "protect": 1
        },
        "id": "waterpledge",
        "name": "Water Pledge",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "water"
    },
    "waterpulse": {
        "accuracy": 100,
        "basePower": 60,
        "category": "special",
        "flags": {
            "distance": 1,
            "mirror": 1,
            "protect": 1,
            "pulse": 1
        },
        "id": "waterpulse",
        "name": "Water Pulse",
        "pp": 20,
        "priority": 0,
        "secondary": {
            "chance": 20,
            "volatileStatus": "confusion"
        },
        "target": "any",
        "type": "water"
    },
    "watershuriken": {
        "accuracy": 100,
        "basePower": 15,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "watershuriken",
        "multihit": [
            2,
            5
        ],
        "name": "Water Shuriken",
        "pp": 20,
        "priority": 1,
        "secondary": None,
        "target": "normal",
        "type": "water"
    },
    "watersport": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "nonsky": 1
        },
        "id": "watersport",
        "name": "Water Sport",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "all",
        "type": "water"
    },
    "waterspout": {
        "accuracy": 100,
        "basePower": 150,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "waterspout",
        "name": "Water Spout",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "allAdjacentFoes",
        "type": "water"
    },
    "wavecrash": {
        "accuracy": 100,
        "basePower": 120,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "wavecrash",
        "name": "Wave Crash",
        "pp": 10,
        "priority": 0,
        "recoil": [
            33,
            100
        ],
        "secondary": None,
        "target": "normal",
        "type": "water"
    },
    "weatherball": {
        "accuracy": 100,
        "basePower": 50,
        "category": "special",
        "flags": {
            "bullet": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "weatherball",
        "name": "Weather Ball",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "whirlpool": {
        "accuracy": 85,
        "basePower": 35,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1
        },
        "id": "whirlpool",
        "name": "Whirlpool",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "water",
        "volatileStatus": "partiallytrapped"
    },
    "whirlwind": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "bypasssub": 1,
            "drag": 1,
            "failcopycat": 1,
            "mirror": 1,
            "noassist": 1,
            "reflectable": 1,
            "wind": 1
        },
        "id": "whirlwind",
        "name": "Whirlwind",
        "pp": 20,
        "priority": -6,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "wickedblow": {
        "accuracy": 100,
        "basePower": 75,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "punch": 1
        },
        "id": "wickedblow",
        "name": "Wicked Blow",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "dark",
        "willCrit": True
    },
    "wickedtorque": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "failcopycat": 1,
            "failencore": 1,
            "failinstruct": 1,
            "failmefirst": 1,
            "failmimic": 1,
            "noassist": 1,
            "nosleeptalk": 1,
            "protect": 1
        },
        "id": "wickedtorque",
        "name": "Wicked Torque",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 10,
            "status": "slp"
        },
        "target": "normal",
        "type": "dark"
    },
    "wideguard": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "wideguard",
        "name": "Wide Guard",
        "pp": 10,
        "priority": 3,
        "secondary": None,
        "side_conditions": "wideguard",
        "target": "allySide",
        "type": "rock"
    },
    "wildboltstorm": {
        "accuracy": 80,
        "basePower": 100,
        "category": "special",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "wind": 1
        },
        "id": "wildboltstorm",
        "name": "Wildbolt Storm",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 20,
            "status": "par"
        },
        "target": "allAdjacentFoes",
        "type": "electric"
    },
    "wildcharge": {
        "accuracy": 100,
        "basePower": 90,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "wildcharge",
        "name": "Wild Charge",
        "pp": 15,
        "priority": 0,
        "recoil": [
            1,
            4
        ],
        "secondary": None,
        "target": "normal",
        "type": "electric"
    },
    "willowisp": {
        "accuracy": 85,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "willowisp",
        "name": "Will-O-Wisp",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "status": "brn",
        "target": "normal",
        "type": "fire"
    },
    "wingattack": {
        "accuracy": 100,
        "basePower": 60,
        "category": "physical",
        "flags": {
            "contact": 1,
            "distance": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "wingattack",
        "name": "Wing Attack",
        "pp": 35,
        "priority": 0,
        "secondary": None,
        "target": "any",
        "type": "flying"
    },
    "wish": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "heal": 1,
            "snatch": 1
        },
        "id": "wish",
        "name": "Wish",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "side_conditions": "wish",
        "target": "self",
        "type": "normal"
    },
    "withdraw": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "defense": 1
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "withdraw",
        "name": "Withdraw",
        "pp": 40,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "water"
    },
    "wonderroom": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1
        },
        "id": "wonderroom",
        "name": "Wonder Room",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "all",
        "type": "psychic"
    },
    "woodhammer": {
        "accuracy": 100,
        "basePower": 120,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "woodhammer",
        "name": "Wood Hammer",
        "pp": 15,
        "priority": 0,
        "recoil": [
            1,
            3
        ],
        "secondary": None,
        "target": "normal",
        "type": "grass"
    },
    "workup": {
        "accuracy": True,
        "basePower": 0,
        "boosts": {
            "attack": 1,
            "special-attack": 1
        },
        "category": "status",
        "flags": {
            "snatch": 1
        },
        "id": "workup",
        "name": "Work Up",
        "pp": 30,
        "priority": 0,
        "secondary": None,
        "target": "self",
        "type": "normal"
    },
    "worryseed": {
        "accuracy": 100,
        "basePower": 0,
        "category": "status",
        "flags": {
            "allyanim": 1,
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "worryseed",
        "name": "Worry Seed",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "grass"
    },
    "wrap": {
        "accuracy": 90,
        "basePower": 15,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "wrap",
        "name": "Wrap",
        "pp": 20,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal",
        "volatileStatus": "partiallytrapped"
    },
    "wringout": {
        "accuracy": 100,
        "basePower": 0,
        "category": "special",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "wringout",
        "name": "Wring Out",
        "pp": 5,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal"
    },
    "xscissor": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1,
            "slicing": 1
        },
        "id": "xscissor",
        "name": "X-Scissor",
        "pp": 15,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "bug"
    },
    "yawn": {
        "accuracy": True,
        "basePower": 0,
        "category": "status",
        "flags": {
            "mirror": 1,
            "protect": 1,
            "reflectable": 1
        },
        "id": "yawn",
        "name": "Yawn",
        "pp": 10,
        "priority": 0,
        "secondary": None,
        "target": "normal",
        "type": "normal",
        "volatileStatus": "yawn"
    },
    "zapcannon": {
        "accuracy": 50,
        "basePower": 120,
        "category": "special",
        "flags": {
            "bullet": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "zapcannon",
        "name": "Zap Cannon",
        "pp": 5,
        "priority": 0,
        "secondary": {
            "chance": 100,
            "status": "par"
        },
        "target": "normal",
        "type": "electric"
    },
    "zenheadbutt": {
        "accuracy": 90,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "zenheadbutt",
        "name": "Zen Headbutt",
        "pp": 15,
        "priority": 0,
        "secondary": {
            "chance": 20,
            "volatileStatus": "flinch"
        },
        "target": "normal",
        "type": "psychic"
    },
    "zingzap": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "zingzap",
        "name": "Zing Zap",
        "pp": 10,
        "priority": 0,
        "secondary": {
            "chance": 30,
            "volatileStatus": "flinch"
        },
        "target": "normal",
        "type": "electric"
    },
    "zippyzap": {
        "accuracy": 100,
        "basePower": 80,
        "category": "physical",
        "flags": {
            "contact": 1,
            "mirror": 1,
            "protect": 1
        },
        "id": "zippyzap",
        "name": "Zippy Zap",
        "pp": 10,
        "priority": 2,
        "secondary": {
            "chance": 100,
            "self": {
                "boosts": {
                    "evasion": 1
                }
            }
        },
        "target": "normal",
        "type": "electric"
    }
}