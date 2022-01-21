from django.contrib import messages
from django.shortcuts import redirect, render


def permission_denied(request, exception):
    messages.warning(request, '權限不足')
    return redirect('root')


def page_not_found(request, exception):
    return render(request, 'errors/404.html', status=404)