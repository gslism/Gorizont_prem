from .models import Notification, SupportRequest


def notifications_count(request):
    """Контекстный процессор для подсчета непрочитанных уведомлений и списка уведомлений"""
    if request.user.is_authenticated:
        unread_count = Notification.objects.filter(user=request.user, is_read=False).count()
        notifications = Notification.objects.filter(user=request.user).order_by('-created_at')[:10]
        new_support_requests_count = 0
        if request.user.is_admin:
            new_support_requests_count = SupportRequest.objects.filter(status=SupportRequest.STATUS_NEW).count()
        return {
            'unread_notifications_count': unread_count,
            'notifications_list': notifications,
            'new_support_requests_count': new_support_requests_count,
        }
    return {
        'unread_notifications_count': 0,
        'notifications_list': [],
        'new_support_requests_count': 0,
    }
