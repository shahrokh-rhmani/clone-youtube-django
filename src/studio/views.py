import json
import base64
from django.http import JsonResponse
from django.core.files.base import ContentFile
from .models import Channel


def upload_profile_image(request):
    if request.method == 'POST':
        try:
            # Parse the JSON body
            body_unicode = request.body
            body_data = json.loads(body_unicode)
            image_data = body_data.get('image')
            

            # Decode the image
            format, imgstr = image_data.split(';base64,')
            ext = format.split('/')[1]
            data = ContentFile(base64.b64decode(imgstr), name=f"profile.{ext}")

            # Save to the UserProfile model
            user_profile = Channel.objects.get(user=request.user)
            user_profile.profile_image.save(f"profile.{ext}", data)
            user_profile.save()

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'fail', 'message': str(e)})
    return JsonResponse({'status': 'fail', 'message': 'Invalid request method'})
