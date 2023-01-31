# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    fax = fields.Char(string='Fax')
    dob = fields.Char(string='DoB')
    control_gallery = fields.Char(string='DoB')
    title = fields.Char(string='DoB')
    mailing = fields.Char(string='DoB')
    vip = fields.Char(string='DoB')
    nationality = fields.Many2one('res.country', 'Nationality',related='country_id' ,required=True)
