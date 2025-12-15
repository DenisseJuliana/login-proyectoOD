from django.contrib.auth import authenticate # Importa la función para verificar credenciales.
from django.http import JsonResponse        # Importa la clase para enviar respuestas HTTP en formato JSON.
from django.views.decorators.csrf import csrf_exempt # Importa el decorador para deshabilitar la protección CSRF.
import json                                 # Módulo estándar de Python para manejar datos JSON.

@csrf_exempt                                # Desactiva la verificación de CSRF para esta función (común en APIs).
def login_view(request):                    # Define la vista que recibe la solicitud HTTP (request).
    if request.method == 'POST':            # Verifica si la solicitud se envió mediante el método POST.
        data = json.loads(request.body)     # Lee el cuerpo de la solicitud (request.body) y lo convierte de JSON a un diccionario de Python.
        username = data.get('username')     # Extrae el valor asociado a la clave 'username' del diccionario.
        password = data.get('password')     # Extrae el valor asociado a la clave 'password' del diccionario.

        # Llama a Django para verificar si el usuario y la contraseña coinciden con un registro en la base de datos.
        user = authenticate(username=username, password=password) 

        if user is not None:                # Si 'user' no es None, significa que la autenticación fue exitosa.
            return JsonResponse({'status': 'ok'}) # Devuelve una respuesta JSON indicando éxito (código HTTP 200).
        else:                               # Si 'user' es None, la autenticación falló.
            return JsonResponse({'status': 'fail'}, status=401) # Devuelve una respuesta JSON con un estado 401 (No autorizado).