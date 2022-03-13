from django.utils import timezone


def formIsValid(request, list_of_parameters):
    status = True
    message = ""
    for parameter in list_of_parameters:
        if parameter in request.POST and request.POST.get(parameter):
            temp_status = True
        else:
            temp_status = False
            message += f"{parameter}, "
        status = status and temp_status
    return {
        "status": status,
        "message": f"Please enter <b>{message}</b> before submission!",
    }
