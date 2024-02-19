from django.http import JsonResponse
import pandas as pd
from .models import MyModel

def upload_csv(request):
    try:
        if request.method == 'POST' and request.FILES['file']:
            csv_file = request.FILES['file']
            df = pd.read_csv(csv_file)

            # Validate CSV columns
            required_columns = ['field1', 'field2']  # Add more as needed
            if not set(required_columns).issubset(df.columns):
                raise ValueError("Missing required columns in CSV.")

            # Validate and insert data
            for index, row in df.iterrows():
                MyModel.objects.create(
                    field1=row['field1'],
                    field2=row['field2'],
                    # Add more fields as needed
                )

            return JsonResponse({'message': 'Data uploaded successfully'}, status=200)

    except Exception as e:
        return JsonResponse({'message': f'Failed to upload data. {str(e)}'}, status=400)
