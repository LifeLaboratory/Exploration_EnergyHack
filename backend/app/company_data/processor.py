from base.base_sql import Sql


def get_networks(id_company):
    sql_query = f'''
    select
       "Компания"."Название" "НазваниеРодителя"
    , 'Cеть' "Тип_записи"
    ,  "Сеть".*
    from "Компания"
    left join "Сеть" on "Сеть"."Компания" = "Компания".id
    where "Компания".id = {id_company}
    '''
    return Sql.exec(query=sql_query)


def get_rec(id_network):
    sql_query = f'''
select
'РЭС' "Тип_записи"
, *
from "РЭС"
where "Сеть" = {id_network}
order by id
        '''
    return Sql.exec(query=sql_query)


def get_pc(id_rec):
    sql_query = f'''
select 
'Подстанция' "Тип_записи"
, *
from "Подстанция"
where "РЭС" = {id_rec}
order by id
          '''
    return Sql.exec(query=sql_query)


def get_pc_w_rec(id_network):
    sql_query = f'''
select 
'Подстанция' "Тип_записи"
, *
from "Подстанция"
where "Сеть" = {id_network}
and "РЭС" is NULL
order by id
          '''
    return Sql.exec(query=sql_query)


def get_trans(id_pc):
    sql_query = f'''
select 
array[]::integer[] children
, 'Трансформатор' "Тип_записи"
, *
from "Трансформатор"
where "Подстанция" = {id_pc}
order by id
      '''
    return Sql.exec(query=sql_query)


def get_lep(id_network):
    sql_query = f'''
select 
'ЛЭП' "Тип_записи"
, *
from "ЛЭП"
where "Сеть" = {id_network}
order by id
          '''
    return Sql.exec(query=sql_query)


def get_provod(id_lep):
    sql_query = f'''
select 
'Провод' "Тип_записи"
, *
from "Провод"
where "ЛЭП" = {id_lep}
order by id
          '''
    return Sql.exec(query=sql_query)


def get_company_data(id_company):
    networks = get_networks(id_company)
    net = {}
    for net in networks:
        # net = networks[0]
        id_network = net.get('id')

        rec = get_rec(id_network) or []
        for r in rec:
            id_rec = r.get('id')
            pc = get_pc(id_rec) or []
            for p in pc:
                id_pc = p.get('id')
                trans = get_trans(id_pc)
                p['children'] = trans
            r['children'] = pc
        net['children'] = rec

        pc_w_rec = get_pc_w_rec(id_network)
        for p in pc_w_rec:
            id_pc = p.get('id')
            trans = get_trans(id_pc)
            p['children'] = trans
        net['children'] += pc_w_rec

        lep = get_lep(id_network) or []
        for l in lep:
            id_lep = l.get('id')
            opora = get_provod(id_lep) or []
            l['children'] = opora
            for op in opora:
                id_opora = op.get('id')
                provod = get_provod(id_opora) or []
                op['children'] = provod
        net['children'] += lep
    return networks
