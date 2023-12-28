# -*- coding: utf-8 -*-
# from odoo import http


# class Exporter(http.Controller):
#     @http.route('/exporter/exporter', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/exporter/exporter/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('exporter.listing', {
#             'root': '/exporter/exporter',
#             'objects': http.request.env['exporter.exporter'].search([]),
#         })

#     @http.route('/exporter/exporter/objects/<model("exporter.exporter"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('exporter.object', {
#             'object': obj
#         })
