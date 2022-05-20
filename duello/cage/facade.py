from .models import Cage
from duello.custom_auth.models import Users


def create_cage(user_id, title, description):
    user=Users.objects.filter(id=id).get()
    cage = Cage(creator=user, title=title, description=description)
    cage.save()
    return cage
