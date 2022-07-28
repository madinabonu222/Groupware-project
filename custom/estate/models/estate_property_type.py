from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate property menu"


    name=fields.Char('Type Name')
    title = fields.Char("Title")
