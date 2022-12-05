from magasin import produit as prod

r_fruits_legumes = []
r_dph = []
r_epicerie = []
r_liquides = []
r_frais = []

# liste produits fruits et legumes
# --------------------------------------

r_fruits_legumes.append(
    prod(
        "fruits et legumes",
        "TerreAzure",
        0.20,
        0.35,
        "Terre Azure",
        4426,
        True,
        0.2,
        "Pommes Gala",
    )
)
r_fruits_legumes.append(
    prod(
        "fruits et legumes",
        "TerreAzure",
        0.25,
        0.40,
        "Terre Azure",
        4427,
        True,
        0.2,
        "Pommes Golden",
    )
)
r_fruits_legumes.append(
    prod(
        "fruits et legumes",
        "TerreAzure",
        0.22,
        0.44,
        "Terre Azure",
        4428,
        True,
        0.2,
        "Pommes granny smith",
    )
)
r_fruits_legumes.append(
    prod(
        "fruits et legumes",
        "TerreAzure",
        0.19,
        0.24,
        "Terre Azure",
        4429,
        False,
        0.2,
        "Pommes pink lady",
    )
)
r_fruits_legumes.append(
    prod(
        "fruits et legumes",
        "TerreAzure",
        0.20,
        0.30,
        "Terre Azure",
        4430,
        False,
        0.2,
        "Pommes reinettes",
    )
)
r_fruits_legumes.append(
    prod(
        "fruits et legumes",
        "TerreAzure",
        0.21,
        0.33,
        "Terre Azure",
        4431,
        False,
        0.2,
        "Poire conférence",
    )
)
r_fruits_legumes.append(
    prod(
        "fruits et legumes",
        "TerreAzure",
        0.22,
        0.35,
        "Terre Azure",
        4432,
        True,
        0.2,
        "La comice",
    )
)
r_fruits_legumes.append(
    prod(
        "fruits et legumes",
        "TerreAzure",
        0.19,
        0.36,
        "Terre Azure",
        4433,
        True,
        0.2,
        "La passe-crassane",
    )
)
r_fruits_legumes.append(
    prod(
        "fruits et legumes",
        "Instagrum",
        0.19,
        0.40,
        "Instagrum R",
        4434,
        True,
        0.2,
        "Orange sangine",
    )
)
r_fruits_legumes.append(
    prod(
        "fruits et legumes",
        "Instagrum",
        0.19,
        0.38,
        "Instagrum R",
        4435,
        True,
        0.2,
        "Orange Salusatina",
    )
)
r_fruits_legumes.append(
    prod(
        "fruits et legumes",
        "Instagrum",
        0.22,
        0.45,
        "Instagrum R",
        4435,
        True,
        0.2,
        "La Navel Late",
    )
)

# ---------------------------------------
# liste produits dph
r_dph.append(
    prod("DPH", "Fabreez", 0.85, 1.35, "Fabreez inc", 8801, False, 0.2, "Fabreez")
)
r_dph.append(
    prod(
        "DPH",
        "L arbre vert",
        1.1,
        2.65,
        "arbre vert inc",
        8802,
        False,
        0.2,
        "Luiquide vaissel Arbre vrt",
    )
)
r_dph.append(
    prod(
        "DPH", "PIAC", 0.85, 1.86, "Piac inc", 8803, False, 0.2, "Luiquide vaissel Piac"
    )
)
r_dph.append(
    prod("DPH", "Mir", 0.85, 1.6, "Mir inc", 8804, False, 0.2, "Luiquide Mir framboise")
)
r_dph.append(
    prod("DPH", "Mir", 0.85, 1.65, "Mir inc", 8805, False, 0.2, "Luiquide Mir Citron")
)
r_dph.append(
    prod(
        "DPH",
        "PIAC",
        0.85,
        1.86,
        "Piac inc",
        8806,
        False,
        0.2,
        "Luiquide vaissel Piac citron",
    )
)
r_dph.append(
    prod(
        "DPH",
        "PIAC",
        0.85,
        1.90,
        "Piac inc",
        8807,
        False,
        0.2,
        "Luiquide vaissel Piac lavande",
    )
)

# liste produits epicerie
r_epicerie.append(
    prod("epicirei", "Lys", 0.85, 1.99, "Lays R", 9900, False, 0.2, "Chips nature Lays")
)
r_epicerie.append(
    prod("epicirei", "Lys", 0.95, 2.00, "Lays R", 9901, False, 0.2, "Chips BBQ Lays")
)
r_epicerie.append(
    prod(
        "epicirei", "Lys", 0.95, 2.10, "Lays R", 9902, False, 0.2, "Chips VINAIGRE Lays"
    )
)
r_epicerie.append(
    prod(
        "epicirei",
        "Pringles",
        0.95,
        1.59,
        "Pringles R",
        9903,
        False,
        0.2,
        "Pringles nature",
    )
)
r_epicerie.append(
    prod(
        "epicirei",
        "Pringles",
        0.95,
        1.65,
        "Pringles R",
        9904,
        False,
        0.2,
        "Pringles ognion creme",
    )
)
r_epicerie.append(
    prod(
        "epicirei",
        "Pringles",
        0.95,
        1.65,
        "Pringles R",
        9905,
        False,
        0.2,
        "Pringles paprika",
    )
)


# liste produit liquide

r_liquides.append(
    prod(
        "luiquide",
        "Fanta",
        0.95,
        1.27,
        "Coca cola R",
        1100,
        False,
        0.2,
        "Fanta orange",
    )
)
r_liquides.append(
    prod(
        "luiquide",
        "Fanta",
        0.95,
        1.29,
        "Coca cola R",
        1101,
        False,
        0.2,
        "Fanta Pommes",
    )
)
r_liquides.append(
    prod(
        "luiquide",
        "Fanta",
        0.95,
        1.33,
        "Coca cola R",
        1102,
        False,
        0.2,
        "Fanta citron",
    )
)
r_liquides.append(
    prod(
        "luiquide",
        "Schweppes",
        2.5,
        4.76,
        "Schweppes R",
        1103,
        False,
        0.2,
        "Schweppes tonic",
    )
)
r_liquides.append(
    prod(
        "luiquide",
        "Schweppes",
        2.5,
        4.80,
        "Schweppes R",
        1104,
        False,
        0.2,
        "Schweppes Agrume",
    )
)

# liste produits frais
r_frais.append(
    prod(
        "frais",
        "Petit navire",
        4.5,
        6.66,
        "P navir",
        2200,
        True,
        0.2,
        "Saumon fumé norvège",
    )
)
r_frais.append(
    prod(
        "frais",
        "Coraya",
        2.5,
        3.89,
        "Coraya inc",
        2201,
        False,
        0.2,
        "Battonet de crab",
    )
)
r_frais.append(
    prod(
        "frais",
        "Benin",
        1.99,
        2.56,
        "Benin inc",
        2202,
        True,
        0.2,
        "Tarama",
    )
)
r_frais.append(
    prod(
        "frais",
        "Casino",
        0.99,
        1.56,
        "Casino inc",
        2203,
        False,
        0.2,
        "Rillette",
    )
)
