
def datetime_adapter(obj, request):
    return obj.strftime("%a %b %d, %Y at %I:%M %p")

def new_datetime_adapter(obj, request):
    return obj.strftime("%m/%d/%Y %I:%M:%S %p")