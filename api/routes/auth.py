from api.resources.auth import SignupApi, LoginApi, ForgotPasswordApi, ResetPasswordApi

def init_auth_routes(api):
  api.add_resource(SignupApi, '/api/v1/auth/signup')
  api.add_resource(LoginApi, '/api/v1/auth/login')
  api.add_resource(ForgotPasswordApi, '/api/v1/auth/password/forgot')
  api.add_resource(ResetPasswordApi, '/api/v1/auth/password/reset')