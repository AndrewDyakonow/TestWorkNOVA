import json

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def endpoint(request):
    """Создать файл в Google docs"""
    if request.method == 'POST':
        res: dict = json.loads(request.body)
        try:
            file_name = res['name']
            file_text = res['data']
        except KeyError:
            return HttpResponse('Ошибка: Не переданы необходимые параметры')

        return HttpResponse('Документ создан')
    else:
        return HttpResponse('Попробуйте выполнить POST запрос')
