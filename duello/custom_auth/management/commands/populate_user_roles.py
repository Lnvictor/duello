from django.core.management.base import BaseCommand

from ...serializers import ClaimsSerializer, RolesSerializer


class Command(BaseCommand):
    help = "Insert basic user roles and their specific claims"

    def add_arguments(self, parser):
        return super().add_arguments(parser)

    def handle(self, *args, **options):
        inactive = ClaimsSerializer(
            data={
                "description": "inactive_claim",
                "active": False,
                "can_battle": False,
                "can_create": False,
                "can_battle_in_own": False,
            }
        )
        default = ClaimsSerializer(
            data={
                "description": "default_claim",
                "active": True,
                "can_battle": True,
                "can_create": False,
                "can_battle_in_own": False,
            }
        )
        creator = ClaimsSerializer(
            data={
                "description": "creator_claim",
                "active": True,
                "can_battle": True,
                "can_create": True,
                "can_battle_in_own": True,
            }
        )

        inactive_role = RolesSerializer(data={"description": "inactive", "claim_id": 1})
        default_role = RolesSerializer(data={"description": "default", "claim_id": 2})
        creator_role = RolesSerializer(data={"description": "creator", "claim_id": 3})

        inactive.is_valid(raise_exception=True)
        default.is_valid(raise_exception=True)
        creator.is_valid(raise_exception=True)
        inactive.save()
        default.save()
        creator.save()

        inactive_role.is_valid(raise_exception=True)
        default_role.is_valid(raise_exception=True)
        creator_role.is_valid(raise_exception=True)
        inactive_role.save()
        default_role.save()
        creator_role.save()

        self.stdout.write(self.style.SUCCESS("User roles succesfully created"))
