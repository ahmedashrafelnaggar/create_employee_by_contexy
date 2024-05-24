# -*- coding: utf-8 -*-
# {
#     'name': " IPMC  Employee Recruitment ",
#     'summary': """ IPMC Recruitment Customizations """,
#     'description': """ IPMC Recruitment Customizations """,
#     'author': " BOT Team ",
#     'website': " https://github.com/mohamed-a-ibrahim/ipmc ",
#     'category': 'Human Resources',
#     'sequence':-100,
#     'version': '1.0.0.0',
#     'license':'LGPL-3',
#     'depends': ['hr_recruitment'],
#     'data': [
#         'security/ir.model.access.csv',
#         'views/employee_view.xml',
#     ],
#     'demo': [],
#     "application": True,
#     "installable": True,
#     "auto_install": False,
#
# }
{
    'name': 'IPMC  Employee Recruitment',
    'version': '15.0.0.1',
    'license': 'OPL-1',
    'depends': ['base','hr_recruitment'],
    'summary': 'Sale delivery updates that to filter more quick to departments and source documents of delivery orders.',
    'author': 'Ahmed',
    'data': [
        'views/employee_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
}
