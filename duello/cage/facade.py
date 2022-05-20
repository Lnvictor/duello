from duello.custom_auth.models import Users

from .models import Cage


def create_cage(user_id, title, description):
    user = Users.objects.filter(id=id).get()
    cage = Cage(creator=user, title=title, description=description)
    cage.save()
    return cage
