# Copyright 2023 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Stock Release Channel Delivery",
    "summary": """
        Exposes clearly the carrier linked to the release channel """,
    "version": "16.0.1.0.1",
    "license": "AGPL-3",
    "author": "ACSONE SA/NV,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/wms",
    "depends": [
        "stock_release_channel",
        "delivery",
    ],
    "data": ["views/stock_release_channel_views.xml"],
    "demo": [],
}
