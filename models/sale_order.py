from odoo import models, api, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    def action_confirm(self):
        """ Sobreescribimos la confirmación de venta para crear recargas """
        res = super().action_confirm()
        self._create_recarga_tasks()
        return res
    
    def _create_recarga_tasks(self):
        """ Crea tareas de recarga para líneas que cumplan los criterios """
        RecargaTask = self.env['recarga.task']
        
        for order in self:
            # Verificar si es lista de precios TAE
            if order.pricelist_id and 'tae' in (order.pricelist_id.name or '').lower():
                for line in order.order_line:
                    # Verificar si es producto de recarga
                    if line.product_id and 'recarga' in (line.product_id.name or '').lower():
                        RecargaTask.create({
                            'name': f"REC-SO-{order.name}-{line.id}",
                            'product_id': line.product_id.id,
                            'sale_order_id': order.id,
                            'partner_id': order.partner_id.id,
                            'amount': line.price_subtotal,
                            'pricelist_id': order.pricelist_id.id,
                            'state': 'draft',
                            'notes': _('''
                                <p>Generado desde Orden de Venta: <strong>%s</strong></p>
                                <p>Cantidad: %s</p>
                                <p>Precio Unitario: %s</p>
                            ''') % (order.name, line.product_uom_qty, line.price_unit)
                        })
