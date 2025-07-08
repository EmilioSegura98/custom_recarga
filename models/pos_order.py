from odoo import models, api, _

class POSOrder(models.Model):
    _inherit = 'pos.order'

    def _create_order(self, order, draft, existing_order):
        orders = super()._create_order(order, draft, existing_order)
        recarga_model = self.env['recarga.task']
        
        for pos_order in orders:
            if pos_order.pricelist_id and 'tae' in (pos_order.pricelist_id.name or '').lower():
                for line in pos_order.lines:
                    if line.product_id and 'recarga' in (line.product_id.name or '').lower():
                        recarga_model.create({
                            'name': f"REC-{pos_order.name}-{line.id}",
                            'product_id': line.product_id.id,
                            'pos_order_id': pos_order.id,
                            'partner_id': pos_order.partner_id.id or self.env.ref('base.public_partner').id,
                            'amount': line.price_subtotal,
                            'pricelist_id': pos_order.pricelist_id.id,
                            'state': 'draft',
                            'notes': f"Recarga generada automáticamente desde POS: {pos_order.name}"
                        })
        return orders
