
from django.db.models.functions import Lower,Trim

choises_rating = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
)

def search_filter(request):
    from KinoVibe.models import Videofile
    
    key = str(request.GET.get('key'))
    movie = Videofile.objects.filter(title__icontains=key)
    return movie