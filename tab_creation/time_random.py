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


# ouvrir excel
wb = load_workbook("data.xlsx")
ws = wb.active

# SIMULATION d'un achat au hasard
for loops in range(0,17567):
    random_hour = random.randint(0, 23)
    random_minut = random.randint(0, 59)

    current_hour = random_hour
    current_hour = str(current_hour)
    current_minuts = random_minut
    current_minuts = str(current_minuts)
    actual_time = current_hour + ":" + current_minuts

    random_rayon = random.randint(0, 4)
    current_random_rayon = rayons[random_rayon]

    nb_element_max = len(current_random_rayon) - 1
    random_element_in_r = random.randint(0, nb_element_max)

    random_hour = random.randint(0, 22)
    random_minut = random.randint(0, 57)
    # --- client profile gen
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
    # generate_Time

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
            current_prenom.capitalize(),
            current_nom.capitalize(),
            current_age,
            current_full_mail.capitalize(),
            random_home_nb,
            current_rrv,
            current_adress.capitalize(),
            current_cp,
            current_full_tel_generated,
            current_sexe,
            actual_time,
        ]
    )

wb.save("data.xlsx")
