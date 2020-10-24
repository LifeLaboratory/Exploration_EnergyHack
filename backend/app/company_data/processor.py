from base.base_sql import Sql


def get_networks(id_company):
    sql_query = f'''
    select
       "Компания"."Название" "НазваниеРодителя"
    , 'Cеть' "ТипЗаписи"
    ,  "Сеть".*
    from "Компания"
    left join "Сеть" on "Сеть"."Компания" = "Компания".id
    where "Компания".id = {id_company}
    '''
    return Sql.exec(query=sql_query)


def get_rec(id_network):
    sql_query = f'''
select
'РЭС' "ТипЗаписи"
, *
from "РЭС"
where "Сеть" = {id_network}
        '''
    return Sql.exec(query=sql_query)


def get_pc(id_rec):
    sql_query = f'''
select 
'Подстанция' "ТипЗаписи"
, *
from "Подстанция"
where "РЭС" = {id_rec}
          '''
    return Sql.exec(query=sql_query)


def get_trans(id_pc):
    sql_query = f'''
select 
array[]::integer[] children
, 'Трансформатор' "ТипЗаписи"
, *
from "Трансформатор"
where "Подстанция" = {id_pc}
      '''
    return Sql.exec(query=sql_query)


def get_lep(id_network):
    sql_query = f'''
select 
'ЛЭП' "ТипЗаписи"
, *
from "ЛЭП"
where "Сеть" = {id_network}
          '''
    return Sql.exec(query=sql_query)


def get_troc(id_lep):
    sql_query = f'''
select 
array[]::integer[] children
, 'Трос' "ТипЗаписи"
, *
from "Трос"
where "ЛЭП" = {id_lep}
          '''
    return Sql.exec(query=sql_query)


def get_opora(id_lep):
    sql_query = f'''
select 
 'Опора' "ТипЗаписи"
, *
from "Опора"
where "ЛЭП" = {id_lep}
          '''
    return Sql.exec(query=sql_query)


def get_provod(id_opora):
    sql_query = f'''
select 
'Провод' "ТипЗаписи"
, *
from "Провод"
where "Опора" = {id_opora}
          '''
    return Sql.exec(query=sql_query)


def get_company_data(id_company):
    networks = get_networks(id_company)
    net = networks[0]
    id_network = net.get('id')

    rec = get_rec(id_network)
    for r in rec:
        id_rec = r.get('id')
        pc = get_pc(id_rec)
        for p in pc:
            id_pc = p.get('id')
            trans = get_trans(id_pc)
            p['children'] = trans
        r['children'] = pc
    net['children'] = rec

    lep = get_lep(id_network)
    for l in lep:
        id_lep = l.get('id')
        troc = get_troc(id_lep)
        opora = get_opora(id_lep)
        for op in opora:
            id_opora = op.get('id')
            provod = get_provod(id_opora)
            op['children'] = provod
        l['children'] = troc
        l['children'] += opora
    net['children'] += lep
    return net
