import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from model.generate import generate

@csrf_exempt 
def generate_text(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        input_string = data['input-string']
        length = data['length']
        
        generated_text = generate(input_string, int(length))

        return JsonResponse({'message':generated_text})
    else:
        return HttpResponse("Hello World!")