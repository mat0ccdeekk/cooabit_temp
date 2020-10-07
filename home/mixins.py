from django.contrib.auth.mixins import UserPassesTestMixin

class StaffMixing(UserPassesTestMixin):
    """ lo scopo di questo mixin è fare in modo che lo staff possa crea re nuove sezioni """
    def test_func(self):
        return self.request.user.is_staff
