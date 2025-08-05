from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.db import IntegrityError
from django.test import TestCase

UserModel = get_user_model()

class TestUserModel(TestCase):
    def setUp(self):
        self.email = "email@test.com"
        self.password = "test1234"

        self.user = UserModel.objects.create_user(
            email=self.email,
            password=self.password
        )

    def test__valid_str_method__returns__emails(self):
        self.assertEqual(self.email, str(self.user))


    def test__unique_email_constraint__raises_integrity_error(self):
        with self.assertRaises(IntegrityError):
            self.user = UserModel.objects.create_user(
                email=self.email,
                password=self.password
            )

    def test__car_approval_permission__valid(self):
        group = Group.objects.create(name='Moderator')
        permission = Permission.objects.get(codename='approve_car')

        group.permissions.add(permission)

        self.user.groups.add(group)

        self.assertTrue(self.user.has_perm('cars.approve_car'))


class TestProfileModel(TestCase):

    def test__full_name_property__returns_string(self):
        email = "email@test.com"
        password = "test1234"

        user = UserModel.objects.create_user(
            email=email,
            password=password
        )

        user2 = UserModel.objects.create_user(
            email=email + '2',
            password=password
        )

        user3 = UserModel.objects.create_user(
            email=email + '3',
            password=password
        )

        user4 = UserModel.objects.create_user(
            email=email + '4',
            password=password
        )

        user.profile.first_name = 'Ivan'
        user.profile.last_name = 'Draganov'

        user2.profile.first_name = 'Ivan'

        user3.profile.last_name = 'Draganov'


        self.assertEqual(user.profile.first_name + ' ' + user.profile.last_name, user.profile.full_name)
        self.assertEqual(user2.profile.first_name, str(user2.profile.full_name))
        self.assertEqual(user3.profile.last_name, str(user3.profile.full_name))
        self.assertEqual(user4.email, str(user4.profile.full_name))

