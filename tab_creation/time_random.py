import random
from magasin import produit as prod
from liste_client import (
    liste_adrs,
    liste_CP,
    liste_email_at,
    liste_age,
    liste_nom,
    liste_prenom,
    liste_telephone,
    sexe,
    rrv,
)
import pandas as pd
import openpyxl
from openpyxl import workbook, load_workbook
from Item import r_fruits_legumes, r_frais, r_dph, r_epicerie, r_liquides


def sep():
    print("-----------------")


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

# generate hours


# end def
for lines in range(1):
    random_hour = random.randint(0, 22)
    random_minut = random.randint(0, 57)


# declaration rayon
rayons = [r_fruits_legumes, r_dph, r_epicerie, r_liquides, r_frais]
# ---------------------------------

# client profil---------------------------
nb_prenom_max = len(liste_prenom) - 1
nb_nom_max = len(liste_nom) - 1
nb_adrs_max = len(liste_adrs) - 1
nb_type_mail_max = len(liste_email_at) - 1
nb_for_gen_tel_max = len(liste_telephone) - 1
nb_age_max = len(liste_age) - 1
nb_rrv_max = len(rrv) - 1
nb_sex_max = len(sexe) - 1
nb_cp_max = len(liste_CP) - 1

# client profile gen
# name gen
random_prenom = random.randint(0, nb_prenom_max)
current_prenom = liste_prenom[random_prenom]
# last name gen
random_nom = random.randint(0, nb_nom_max)
current_nom = liste_nom[random_nom]
# age gen
random_age = random.randint(0, nb_age_max)
current_age = liste_age[random_age]
# email creation----
random_atmail = random.randint(0, nb_type_mail_max)
current_at_mail = liste_email_at[random_atmail]
current_email = current_prenom + current_nom
current_full_mail = current_email + current_at_mail
# adress gen----
random_home_nb = random.randint(1, 200)

random_rrv = random.randint(0, nb_rrv_max)
current_rrv = rrv[random_rrv]

random_adress = random.randint(0, nb_adrs_max)
current_adress = liste_adrs[random_adress]

random_cp = random.randint(0, nb_cp_max)
current_cp = liste_CP[random_cp]
# num tel gen
random_tel_digit = random.randint(111111, 999999)
random_tel_digit_str = str(random_tel_digit)

random_tel_sart = random.randint(0, nb_for_gen_tel_max)
current_tel_start = liste_telephone[random_tel_sart]
current_full_tel_generated = current_tel_start + random_tel_digit_str
# -----print test client
# sex gen-----
random_sexe = random.randint(0, nb_sex_max)
current_sexe = sexe[random_sexe]
# ----------
sep()
print(
    current_prenom.capitalize(),
    current_nom.capitalize(),
    current_age,
    "Ans \n",
    "Email:",
    current_full_mail.capitalize(),
    "\n",
    "Adresse : ",
    random_home_nb,
    current_rrv,
    current_adress.capitalize(),
    current_cp,
    "\n",
    "Téléphone :",
    current_full_tel_generated,
    "\n",
    "Sexe :",
    current_sexe,
)
sep()
# ouvrir excel
wb = load_workbook("data.xlsx")
ws = wb.active

# SIMULATION d'un achat au hasard
for loops in range(0, 7):

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
