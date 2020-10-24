# coding=utf-8
from base import base_name as names
from base.base_router import BaseRouter
from base.base_sql import Sql
result_data = []
id_company = 1


def get_networks(id_company):
    sql_query = f'''
    select
       "Компания"."Название" "НазваниеРодителя"
    ,  "Сеть".*
    from "Компания"
    left join "Сеть" on "Сеть"."Компания" = "Компания".id
    where "Компания".id = {id_company}
    '''
    return Sql.exec(query=sql_query)


def get_rec(id_network):
    sql_query = f'''
        select *
        from "РЭС"
        where "Сеть" = {id_network}
        '''
    return Sql.exec(query=sql_query)


def get_pc(id_rec):
    sql_query = f'''
          select *
          from "Подстанция"
          where "РЭС" = {id_rec}
          '''
    return Sql.exec(query=sql_query)


def get_trans(id_pc):
    sql_query = f'''
      select *
        , array[]::integer[] children
      from "Подстанция"
      where "РЭС" = {id_pc}
      '''
    return Sql.exec(query=sql_query)


def get_lep(id_network):
    sql_query = f'''
select *
from "ЛЭП"
where "Сеть" = {id_network}
          '''
    return Sql.exec(query=sql_query)


def get_troc(id_lep):
    sql_query = f'''
select *, array[]::integer[] children
from "Трос"
where "ЛЭП" = {id_lep}
          '''
    return Sql.exec(query=sql_query)


def get_opora(id_lep):
    sql_query = f'''
select *
from "Опора"
where "ЛЭП" = {id_lep}
          '''
    return Sql.exec(query=sql_query)


def get_provod(id_opora):
    sql_query = f'''
select *
from "Провод"
where "Опора" = {id_opora}
          '''
    return Sql.exec(query=sql_query)



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

asdsadd = 1

