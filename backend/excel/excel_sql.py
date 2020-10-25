SQL_ADD_LEP = """
INSERT INTO "ЛЭП" {LEP}
VALUES ({num_set}, {num_pp}, '{name}', '{disp_name}', {napr}, '{techsost}')
RETURNING id
"""

SQL_ADD_PROVOD = """
INSERT INTO "Провод" {PROVOD}
VALUES ({id_lep}, '{name}', {year}, {colcep}, '{dlpotr}', '{dlpocep}', '{dluchpotr}', '{dluchpocep}')
RETURNING id
"""

SQL_ADD_RES = """
INSERT INTO "РЭС" {RES}
VALUES ({num_set}, '{name_res}')
RETURNING id
"""

SQL_ADD_PODSTANC = """
INSERT INTO "Подстанция" {PODSTANC}
VALUES ('{name}', {num_podst}, {year}, '{class_napr}', {id_res}, {id_set})
RETURNING id
"""

SQL_ADD_TRANSFORM = """
INSERT INTO "Трансформатор" {TRANSFORM}
VALUES ({id_podst}, {year_izg}, {year_on}, '{type}', {nom_p}, '{techsost}', '{number}')
RETURNING id
"""

SQL_ADD_SETT = """
INSERT INTO "Сеть" {SETT}
VALUES ({comp_id}, '{sett_name}')
RETURNING id
"""

SQL_FIND_SETT = """
SELECT id
FROM "Сеть"
WHERE "Название" = '{sett_name}' AND "Компания" = {comp_id}
"""