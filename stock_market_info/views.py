import os
import requests
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, \
    authentication_classes, throttle_classes
from users.authentication import ApiKeyAuthentication
from .throttle_rate import OncePerSecondThrottle, TenPerMinuteThrottle, \
    OneTHoundredPerHourThrottle, OneThousandPerDayThrottle


def get_alphavantage_url(symbol):
    api_key = os.environ.get("ALPHAVANTAGE_KEY")
    return f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=compact&apikey={api_key}'


@api_view(['GET'])
@permission_classes([HasAPIKey])
@authentication_classes([ApiKeyAuthentication])
@throttle_classes([OncePerSecondThrottle, TenPerMinuteThrottle, OneTHoundredPerHourThrottle,
    OneThousandPerDayThrottle])
def get_market_info(request, symbol):
    url = get_alphavantage_url(symbol)
    r = requests.get(url)
    data = r.json()
    return Response({'user': request.user.email, 'data': data})
