from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            
            group = None
            
            if request.user.groups.exists(): #속한그룹이있다면
                group = request.user.groups.all()[0].name
                print('yes')
            print(group)
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse(
                    """<h1> admin,staff만 입장가능합니다</h1>"""
                    )
        return wrapper_func
    return decorator

#admin은 admin으로 나머지 고객그룹은 각각페이지로
def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group =None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        
        if group == 'customer':
            return redirect('user-page')
        
        if group =='admin':
            return view_func(request, *args, **kwargs)
        
    return wrapper_function