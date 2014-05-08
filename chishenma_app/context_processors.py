def process(request):
    return {
        'authenticated': request.user.is_authenticated(),
        'username': request.user.username if request.user.is_authenticated() else None
    }
