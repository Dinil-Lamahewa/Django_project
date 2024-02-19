
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from myapp.models import MyModel

@csrf_exempt  # This decorator is used to disable CSRF protection for simplicity in this example
def upload_csv(request):
    if request.method == 'POST' and request.FILES['file']:
        try:
            csv_file = request.FILES['file']
            df = pd.read_csv(csv_file)

            # Assuming 'field1' and 'field2' are required columns in the CSV
            for index, row in df.iterrows():
                MyModel.objects.create(
                    field1=row['field1'],
                    field2=row['field2'],
                    # Add more fields as needed
                )

            return JsonResponse({'message': 'Data uploaded successfully'}, status=200)

        except Exception as e:
            return JsonResponse({'message': f'Failed to upload data. {str(e)}'}, status=400)

    return JsonResponse({'message': 'Invalid request method or missing file'}, status=400)
