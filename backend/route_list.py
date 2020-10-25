from app import Companies, CompanyData, UploadData, PCReport, LEPReport

ROUTES = {
    '/api/companies': Companies,
    '/api/company_data/<int:id_company>': CompanyData,
    '/api/upload_data': UploadData,

}
