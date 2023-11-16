import json

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from app.google.google_docs import googleAPI


@csrf_exempt
def endpoint(request):
    """Создать файл в Google docs"""
    if request.method == 'POST':
        res: dict = json.loads(request.body)
        try:
            new_file = {
                'filename': res['name'],
                'body': res['data'],
            }
            googleAPI.create_file(**new_file)
        except KeyError:
            return HttpResponse('Ошибка: Не переданы необходимые параметры')

        return HttpResponse('Документ создан')
    else:
        return HttpResponse('Попробуйте выполнить POST запрос')
