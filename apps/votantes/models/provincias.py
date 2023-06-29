# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Provincias(models.Model):
    _name = 'provincias.votantes'
    _description = 'provincias.votantes'

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")
    capital = fields.Char(string="Capital")
    population = fields.Integer(string="Population")
