# mxshop
该项目为前后端分离项目，前端使用vue框架，后端为django-rest-framework。
实现的功能有：
登录注册、手机验证码、
三级导航、首页轮播、首页新品以及首页分类商品、自定义导航、
商品的分类展示、商品的详情展示、添加购物车、收藏、
个人中心的实现、个人信息修改、收货地址等等
未实现的功能：
支付、第三方登录


使用方法：
git clone到你的项目目录中去，
pip install -r requirements.txt等相关依赖包,
安装vue.js,
cnpm install Vue项目 然后cnpm run dev，
django项目则python manage.py migrate生成对应数据库，
使用db_tools下的两个python文件导入商品内容，
然后python manage.py runserver，
就可以去网页中查看相关的内容了。
