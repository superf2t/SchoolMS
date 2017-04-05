from django.contrib import admin
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from rest_framework import routers

from user.views import UserViewSet
from school.views import *
from oa.views import *

router = routers.DefaultRouter()

# 用户
router.register(r'user', UserViewSet)
# 学校
router.register(r'school', SchoolViewSet)
# 校区
router.register(r'branch', BranchViewSet)
# 部门
router.register(r'department', DepartmentViewSet)
# 员工
router.register(r'staff', StaffViewSet)
# 邮件模板
router.register(r'email_template', EmailTemplateViewSet)
# 邮件
router.register(r'email', EmailViewSet)
# 通知模板
router.register(r'notification_template', NotificationTemplateViewSet)
# 通知
router.register(r'notification', NotificationViewSet)
# 员工工作报告模板
router.register(r'work_report_template', WorkReportTemplateViewSet)
# 员工工作报告
router.register(r'work_report', WorkReportViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls
