from rest_framework.routers import DefaultRouter
from .views import Salom1ViewSet, Salom2ViewSet, Salom3ViewSet,  Salom4ViewSet, Salom5ViewSet
    
   
   
   
    


router = DefaultRouter()
router.register('salom1', Salom1ViewSet)
router.register('salom2', Salom2ViewSet)
router.register('salom3', Salom3ViewSet)
router.register('salom4', Salom4ViewSet)
router.register('salom5', Salom5ViewSet)

urlpatterns = router.urls