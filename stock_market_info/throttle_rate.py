from rest_framework.throttling import UserRateThrottle


class OncePerSecondThrottle(UserRateThrottle):
    rate = '1/second'


class TenPerMinuteThrottle(UserRateThrottle):
    rate = '10/min'


class OneTHoundredPerHourThrottle(UserRateThrottle):
    rate = '100/hour'


class OneThousandPerDayThrottle(UserRateThrottle):
    rate = '1000/day'
