from ..models import AuditLog

def log_event (*,request = None, user = None, event_type, model_name=None, object_id=None, description=None):
    if user and user.is_authenticated:
        final_user = user
    else:
        final_user= None
    AuditLog.objects.create(
        user= final_user,
        event_type=event_type,
        model_name=model_name,
        object_id=object_id,
        description=description,
        ip_address=get_client_ip(request),
        user_agent=request.META.get("HTTP_USER_AGENT") if request else None,
    )

def get_client_ip(request):
    if not request:
        return None
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        return x_forwarded_for.split(",")[0]
    return request.META.get("REMOTE_ADDR")