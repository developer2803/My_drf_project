from rest_framework.routers import DefaultRouter

from apps.news.views import NewsViewSet
from apps.administration.views import AdministrationViewSet
from apps.ads.views import AdViewSet
from apps.links.views import UsefulLinkViewSet
from apps.media_library.views import VideoViewSet, AudioViewSet, ImageViewSet
from apps.regions.views import RegionViewSet
from apps.requisites.views import RequisiteViewSet
from apps.press_office.views import AudioChiqishViewSet, VideoChiqishViewSet, TextChiqishViewSet

from apps.ads.views import PressContactViewSet
from apps.suborganizations.views import SubOrganizationViewSet
from apps.central_office.views import CentralOfficeViewSet
from apps.saxovat_va_komak.views import JamgarmaViewSet, JamgarmaYiliViewSet

router = DefaultRouter()

router.register(r'news', NewsViewSet, basename='news')

router.register(r'administration', AdministrationViewSet, basename='administration')
router.register(r'ads', AdViewSet, basename='ads')
router.register(r'links', UsefulLinkViewSet, basename='links')
router.register(r'mediateka/audio', AudioViewSet, basename='audios')
router.register(r'mediateka/video', VideoViewSet, basename='videos')
router.register(r'mediateka/image', ImageViewSet, basename='images')
router.register(r'regions', RegionViewSet, basename='regions')
router.register(r'requisites', RequisiteViewSet, basename='requisites')

router.register(r'press_contact', PressContactViewSet, basename='press_contact')
router.register(r'press_office/video', VideoChiqishViewSet, basename='video_chiqish')
router.register(r'press_office/audio', AudioChiqishViewSet, basename='audio_chiqish')
router.register(r'press_office/text', TextChiqishViewSet, basename='text_chiqish')

router.register(r'jamgarma_yili', JamgarmaYiliViewSet, basename='jamgarma_yili')
router.register(r'sub_organizations', SubOrganizationViewSet, basename='sub_organizations')
router.register(r'central_office', CentralOfficeViewSet, basename='central_office')


urlpatterns = router.urls