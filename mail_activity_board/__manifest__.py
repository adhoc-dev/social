# Copyright 2018 David Juaneda - <djuaneda@sdi.es>
# Copyright 2021 Sodexis
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Mail Activity Board",
    "summary": "Add Activity Boards",
    "version": "15.0.1.0.0",
    "development_status": "Beta",
    "category": "Social Network",
    "website": "https://github.com/OCA/social",
    "author": "SDi, David Juaneda, Sodexis, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": [
        "calendar",
        "board",
    ],
    "assets": {
        "web.assets_backend": [
            "/static/src/components/chatter_topbar/chatter_topbar.js",
        ],
    },
    "data": [
        "views/mail_activity_view.xml",
    ],
    "qweb": ["static/src/components/chatter_topbar/chatter_topbar.xml"],
    "installable": True,
    "auto_install": False,
    "application": False,
}
