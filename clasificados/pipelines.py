from django.shortcuts import redirect

__author__ = 'edx'
from social.pipeline.partial import partial

def get_avatar(backend, strategy, details, response, user=None, *args, **kwargs):
    url = None
    if backend.name == 'facebook':
        url = 'https://graph.facebook.com/%s/picture?type=large' % response['id']

    """
    if url:
        if user.avatar:
            return
        else:
            pass
            #user.avatar = url
            #user.save()
            """


def user_details(strategy, details, response, is_new=False, user=None, *args, **kwargs):

    if user and not is_new:
        changed = False
        protected = strategy.setting('PROTECTED_USER_FIELDS', [])
        keep = ('username', 'id', 'pk',) + tuple(protected)

        for name, value in details.items():
            if name not in keep and hasattr(user, name):
                if value and value != getattr(user, name, None):
                    try:
                        setattr(user, name, value)
                        changed = True
                    except AttributeError:
                        pass
        if changed:
            strategy.storage.user.changed(user)

#Definir el nombre de usuario basado en el correo electronico
def get_username(strategy, details, user=None, *args, **kwargs):
    email = str(details['email'])
    if not user:
        details['username'] = email.split('@')[0]

def set_password(strategy, details, user=None, *args, **kwargs):
    password = str(details['password'])
    if user:
        user.set_password(password)
        user.save()

@partial
def complete_record(backend, strategy, request, details, response, user=None, is_new=False,  *args, **kwargs):
    if is_new:
        if strategy.session_get('password'):
            details['password'] = strategy.session_pop('password')
        else:
            strategy.session['usuario'] = details['username']
            return redirect('/completar-registro/')

