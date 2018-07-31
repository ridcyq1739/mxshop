"""mxshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path,re_path,include
import xadmin
from mxshop.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from goods.views import GoodsListViewSet,CategoryViewSet,HotSearchsViewset,BannerViewSet,IndexCategoryViewSet
from users.views import SmsCodeViewSet,UserViewSet
from user_operation.views import UserFavViewSet,LeavingMessageViewSet,AddressViewSet
from trade.views import ShoppingCartViewSet,OrderViewSet

router = DefaultRouter()

#配置goods的url
router.register(r'goods', GoodsListViewSet, base_name='goods')
#配置goodscategory的url
router.register(r'categorys', CategoryViewSet, base_name='categorys')
#验证码
router.register(r'code', SmsCodeViewSet, base_name='code')
#热门搜索
router.register(r'hotsearchs', HotSearchsViewset, base_name="hotsearchs")
#用户
router.register(r'users', UserViewSet, base_name='users')
#收藏
router.register(r'userfavs', UserFavViewSet, base_name='userfavs')
#留言
router.register(r'messages', LeavingMessageViewSet, base_name='messages')
#收货地址
router.register(r'address', AddressViewSet, base_name='address')
#购物车
router.register(r'shopcarts', ShoppingCartViewSet, base_name='shopcarts')
#订单
router.register(r'orders', OrderViewSet, base_name='orders')
#轮播图
router.register(r'banners', BannerViewSet, base_name='banners')
#首页商品xi列数据
router.register(r'indexgoods', IndexCategoryViewSet, base_name='indexgoods')


goods_list = GoodsListViewSet.as_view({
    'get': 'list',
})
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    re_path(r'^', include(router.urls)),

    re_path(r'^api-auth/', include('rest_framework.urls',namespace="rest_framework")),
    re_path(r'^ueditor/', include('DjangoUeditor.urls')),
    #drf自带的认证方式
    re_path(r'^api-token-auth/', views.obtain_auth_token),
    #jwtd额认证接口
    re_path(r'^login/', obtain_jwt_token),
    re_path(r'^docs/',include_docs_urls(title="mxsx")),
]
