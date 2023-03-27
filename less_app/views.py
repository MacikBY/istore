from django.shortcuts import render

from .models import LessUser, School


# Create your views here.
def get_page_less1(request):
    less_users = LessUser.objects.all()
    print(LessUser.__dict__)
    context = {"users": less_users}
    return render(request, 'less_app/less_page_1.html', context)

def get_news(request):
    less_users = LessUser.objects.all()
    context = {"users": less_users}
    return render(request, 'less_app/less_news.html', context)


def get_all_courses_students(request):
    if request.method == "POST":
        school = School.objects.filter(name=request.POST.get("name_school"))
        print(school.__str__())
        context = {"school": school}
        # students_this_school = School.objects.filter(school_id=school.id)
        # print(students_this_school)
        # for i in students_this_school:
        #
        #     print(i.courses[0])
    return render(request, "less_app/courses_and_student_m2m.html", context)
