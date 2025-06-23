from rest_framework.throttling import  AnonRateThrottle


class MatriculaAnonRateThrottle(AnonRateThrottle):
    rates = '5/day'
