# -*- coding: utf-8 -*-
from odoo import models, fields, api


class biblio(models.Model):
    _name = 'biblio.biblio'

    name = fields.Char('Title', required=True)
    isbn = fields.Char('ISBN')
    active = fields.Boolean('Active?', default=True)
    date_pub = fields.Date()
    image = fields.Binary('Cover')
    publisher_id = fields.Many2one('res.partner', string='publisher') 
    auteur = fields.Many2many('res.partner', string='auteur')

