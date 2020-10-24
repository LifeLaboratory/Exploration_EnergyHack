from app import Companies, CompanyData

ROUTES = {
    '/api/companies': Companies,
    '/api/company_data/<int:id_company>': CompanyData,

}
