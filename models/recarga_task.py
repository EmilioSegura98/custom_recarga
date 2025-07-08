from odoo import models, fields, api

class RecargaTask(models.Model):
    _name = 'recarga.task'
    _description = 'Tarea de Recarga'
    _order = 'create_date desc'
    
    name = fields.Char(string='Referencia', required=True, index=True)
    partner_id = fields.Many2one('res.partner', string='Cliente', required=True)
    product_id = fields.Many2one('product.product', string='Producto', required=True)
    amount = fields.Float(string='Monto', digits='Product Price')
    state = fields.Selection([
        ('draft', 'Pendiente'),
        ('in_process', 'En Proceso'),
        ('done', 'Completada'),
        ('cancel', 'Cancelada')],
        string='Estado', default='draft', tracking=True)
    notes = fields.Text(string='Notas')
    sale_order_id = fields.Many2one('sale.order', string='Orden de Venta')
    pos_order_id = fields.Many2one('pos.order', string='Orden POS')
