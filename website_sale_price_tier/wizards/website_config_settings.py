# Copyright 2017 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)

from odoo import fields, models


class WebsiteConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    show_implicit_price_tier = fields.Boolean(
        related='website_id.show_implicit_price_tier',
    )
