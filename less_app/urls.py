from django.urls import path

from less_app.views import get_page_less1, get_news, get_all_courses_students

app_name ='less_app'

urlpatterns = [
    path('less_page_1/', get_page_less1, name='less_page_1'),
    path('news', get_news, name='news'),
    path('m2m_fk/', get_all_courses_students, name='m2m_fk'),
    ]