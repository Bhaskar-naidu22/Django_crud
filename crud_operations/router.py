from crud_student.viewsets import studentViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('student', studentViewset)
