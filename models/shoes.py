from odoo import api, fields, models

class ShoeProduct(models.Model):
    _name = 'shoe.product'
    _description = 'Shoe Product'



    name = fields.Char(string='Name', required=True)
    brand = fields.Char(string='Brand', required=True)
    price = fields.Float(string='Price', required=True)
    gender = fields.Selection([('male', 'Men'), ('female', 'Women'), ('unisex', 'Unisex')], string='Gender', required=True)
    note = fields.Text(string='Note')

    responsible_id = fields.Many2one('res.users', string='Responsible')



    @api.model
    def create(self, vals):
        if vals.get('name'):
            vals['name'] = vals['name'].title()
        return super(ShoeProduct, self).create(vals)

    def write(self, vals):
        if vals.get('name'):
            vals['name'] = vals['name'].title()
        return super(ShoeProduct, self).write(vals)


# class ProductProduct(models.Model):
#     _inherit = 'product.template'
#
#     shoe_product_ids = fields.One2many('shoe.product', 'related_product_id', string='Shoe Products')
