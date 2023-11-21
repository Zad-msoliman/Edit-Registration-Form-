from odoo.addons.web.controllers.home import ensure_db, Home, SIGN_UP_REQUEST_PARAMS, LOGIN_SUCCESSFUL_PARAMS
from odoo import http, _
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.addons.auth_signup.models.res_users import SignupError
from odoo.exceptions import UserError
from odoo.http import request


              # this code create user then search then update phone and mobile

class Phone(Home):
    @http.route('/web/signup', type='http', auth='public', website=True, sitemap=False)
    def web_auth_signup(self, *args, **kw):
        qcontext = self.get_auth_signup_qcontext()
        web_company = request.env.company
        res = super().web_auth_signup()
        user = request.env['res.users'].sudo().search([("login", "=", qcontext.get("login"))])
        user.sudo().write({
            'phone': kw.get('phone'),
            'mobile': kw.get('mobile'),
        })
        return res
