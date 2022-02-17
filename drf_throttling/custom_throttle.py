from rest_framework.throttling import UserRateThrottle

class CustomThrottle(UserRateThrottle):
    # help(UserRateThrottle)
    scope ='custom'