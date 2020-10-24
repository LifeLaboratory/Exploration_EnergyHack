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