# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    part_number = fields.Char(string="Part No/Name")
    size_h = fields.Float('SizeH')
    size_l = fields.Float('SizeL')
    size_p = fields.Float('SizeP')
    status = fields.Char('Status')
    stock_status = fields.Char('Stock Status')
    medium = fields.Char('Medium')
    picture_name = fields.Char('Medium')
    control_gallery = fields.Char('Stock Status')
    sub_location = fields.Char('Stock Status')
    artist = fields.Many2one('res.partner')


