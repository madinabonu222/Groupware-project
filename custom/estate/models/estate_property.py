from email.policy import default
from hashlib import new
from attr import field
from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate property plans"
    _order = "sequence"
    def create (self,values):
        override_create = super(EstateProperty,self).create(values)
        return override_create
    
    # name = fields.Char('Property Name', required=True, translate=True)
    name = fields.Char(default="Unknown")
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    description = fields.Text('Text')
    postcode = fields.Char('Postcode')
    data_availability = fields.Date('Data')
    expected_price = fields.Float('Expected Price')
    selling_price = fields.Float('Selling Price')
    bedrooms = fields.Integer('Bedrooms')
    living_area = fields.Integer('Living Area')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area')
    garden_orientation = fields.Selection(
        string='Orientation',
        selection = [('north','North'),('south','South'),('east','East'),('west','West')],
        help = "Orientation is used to separate geographical location"
    )
    sequence = fields.Integer('Sequence')
    active = fields.Boolean(active=False)
    state = fields.Boolean(default="New")


