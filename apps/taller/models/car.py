# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Car(models.Model):
    _name = 'taller.car'
    _description = 'taller.car'

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")
    brand = fields.Char(string="Brand")
    date_car = fields.Date("Date Car")
    km = fields.Integer(string="Km")