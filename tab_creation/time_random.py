import random
from magasin import produit as prod
import pandas as pd
import openpyxl
from openpyxl import workbook, load_workbook
from Item import r_fruits_legumes, r_frais, r_dph, r_epicerie, r_liquides

hours = [
    0,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
]
minutes = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    48,
    49,
    50,
    51,
    52,
    53,
    54,
    55,
    56,
    57,
    58,
    59,
]
sepration = "---------------"
# generate hours


# end def
for lines in range(1):
    random_hour = random.randint(0, 22)
    random_minut = random.randint(0, 57)


# declaration rayon
rayons = [r_fruits_legumes, r_dph, r_epicerie, r_liquides, r_frais]
# ---------------------------------
# ouvrir excel
wb = load_workbook("data.xlsx")
ws = wb.active

# SIMULATION d'un achat au hasard
for loops in range(0, 110):

    random_rayon = random.randint(0, 4)
    current_random_rayon = rayons[random_rayon]

    nb_element_max = len(current_random_rayon) - 1
    random_element_in_r = random.randint(0, nb_element_max)

    random_hour = random.randint(0, 22)
    random_minut = random.randint(0, 57)
    ws.append(
        [
            current_random_rayon[random_element_in_r].nom,
            current_random_rayon[random_element_in_r].rayon,
            current_random_rayon[random_element_in_r].marque,
            current_random_rayon[random_element_in_r].prix_vente,
            current_random_rayon[random_element_in_r].prix_achat,
            current_random_rayon[random_element_in_r].fournisseur,
            current_random_rayon[random_element_in_r].bio,
            current_random_rayon[random_element_in_r].ID,
            current_random_rayon[random_element_in_r].tva,
        ]
    )

wb.save("data.xlsx")
