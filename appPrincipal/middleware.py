from django.shortcuts import redirect

class AdminRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin-panel/') and not request.user.is_staff:
            return redirect('login') 
        return self.get_response(request)