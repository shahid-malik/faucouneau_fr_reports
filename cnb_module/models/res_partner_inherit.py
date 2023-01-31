# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    fax = fields.Char(string='Fax')
    dob = fields.Char(string='DoB')
    nationality = fields.Char(string='Nationality')
