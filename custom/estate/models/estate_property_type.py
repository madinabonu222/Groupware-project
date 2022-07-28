from email.policy import default
from hashlib import new
from unicodedata import name
from attr import field
from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate property menu"
    _order = "sequence"


    name=fields.Char('Type Name', required=True)
    title = fields.Char(default="Unkown")
