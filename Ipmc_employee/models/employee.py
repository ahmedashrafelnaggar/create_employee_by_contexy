from odoo import models, fields, _


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    employment_id = fields.Many2one('employment.status')
    res_country_id = fields.Many2one('res.country', 'Country')
    res_country_state_id = fields.Many2one('res.country.state', 'Country State')
    res_bank_id = fields.Many2one('res.bank', 'Bank')
    hr_job_id = fields.Many2one('hr.job', 'Job')
    hr_department_id = fields.Many2one('hr.department', 'Department')

    ex_id = fields.Integer(string="External ID")

    # identifier = fields.Char(string="identifier")
    iqama_number = fields.Char(string="Residential Number")
    iqama_exp_date = fields.Date(string="Residential Expiry Date")
    iqama_src_id = fields.Many2one('res.country.state', string='Residential Source')
    nationality_id = fields.Many2one('res.country', string='Nationality')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    contact_name = fields.Char(string='Contact Name')
    phone = fields.Char(string='Contact Phone')

    hr_recruitment_degree_id = fields.Many2one('hr.recruitment.degree', 'Degree')
    speciality = fields.Char(string="Speciality")
    birth_date = fields.Date(string="Date of Birth")
    address = fields.Char(string="Address")

    applicant_id = fields.Many2one('hr.applicant', string="Applicant ID")
    partner_mobile = fields.Char(readonly=0 , string=' Mobile')
    email_from = fields.Char(readonly=0, string='Email ')
    email_cc= fields.Char(string='Email cc')
    # categ_ids = fields.many2many('hr.applicant.category', string='Tags')





    Employement_Status = fields.Many2one('employment.status', string="Employment Status")
    years_of_experience = fields.Integer(string="Years of Experience")
    employer = fields.Char(string="Employer")
    workplace = fields.Char(string="Work Place")


    years_of_experience_in_haj = fields.Integer(string="Years of Experience in HAJ")
    job_title_in_haj = fields.Many2one('hr.job',string="Job Title in HAJ")
    party_name_in_haj = fields.Char(string="Party Name")

    job_app_announcement_id = fields.Many2one('ipmc.application.announcement',string="Announcement")

    applied_job_workplace_id = fields.Many2one('res.country.state',string="chosen Work Place ")
    first_job_id_applied = fields.Many2one('hr.job',string="First Desired Job")
    first_job_sector_id = fields.Many2one('hr.department',string=" First Desired Department")
    second_job_id_applied = fields.Many2one('hr.job',string="Second Desired Job")
    second_job_sector_id = fields.Many2one('hr.department',string="Second Desired Department")
    third_job_id_applied = fields.Many2one('hr.job',string="Third Desired Job")
    third_job_sector_id = fields.Many2one('hr.department',string="Third Desired Department")
    bank_id = fields.Many2one('res.bank',string="Bank Name")
    iban = fields.Char(string="IBAN Number")
    authorized_iban = fields.Binary(string="IBAN Image URL")
    profile_image = fields.Binary(string="Person Picture URL")
    cv = fields.Binary(string="CV URL")

    instructionandcondition = fields.Text('Instructions and conditions')
