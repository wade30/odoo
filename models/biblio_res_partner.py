# -*- coding: utf-8 -*-

from odoo import models, fields, api


class champs(models.Model):
     _inherit = ['res.partner']

     is_auteur=fields.Boolean('est_auteur')
     is_publisher=fields.Boolean('est_publiciteur')