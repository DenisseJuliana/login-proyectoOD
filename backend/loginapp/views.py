from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        # Carga los datos JSON del cuerpo de la solicitud
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'fail', 'message': 'Invalid JSON'}, status=400)

        # Obtiene el nombre de usuario y la contraseña
        username = data.get('username')
        password = data.get('password')

        # Intenta autenticar al usuario
        user = authenticate(username=username, password=password)

        if user is not None:
            # Si la autenticación es exitosa
            return JsonResponse({'status': 'ok'})
        else:
            # Si las credenciales son incorrectas
            return JsonResponse({'status': 'fail', 'message': 'Invalid credentials'}, status=401)
    
    # Maneja otros métodos HTTP (GET, PUT, etc.)
    return JsonResponse({'status': 'fail', 'message': 'Method not allowed'}, status=405)


