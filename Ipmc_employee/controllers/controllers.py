# -*- coding: utf-8 -*-
# from odoo import http


# class IpmcBotCustom(http.Controller):
#     @http.route('/ipmc_bot_custom/ipmc_bot_custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ipmc_bot_custom/ipmc_bot_custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ipmc_bot_custom.listing', {
#             'root': '/ipmc_bot_custom/ipmc_bot_custom',
#             'objects': http.request.env['ipmc_bot_custom.ipmc_bot_custom'].search([]),
#         })

#     @http.route('/ipmc_bot_custom/ipmc_bot_custom/objects/<model("ipmc_bot_custom.ipmc_bot_custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ipmc_bot_custom.object', {
#             'object': obj
#         })
