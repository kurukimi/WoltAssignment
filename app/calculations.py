import math
import dateutil.parser
from constants import const

def cartValueFee(cartValue):
    if cartValue < const.minCartValue:
        return const.minCartValue - cartValue
    return 0

def distanceFee(distance):
    fee = const.minDistanceFee
    diff = distance - const.minDistance 
    if diff <= 0:
        return fee
    additional = math.ceil(diff/const.additionalDistance) * const.additionalDistanceFee
    return fee + additional
    
def itemFee(numOfItems):
    if numOfItems > const.maxItems:
        additional = numOfItems - const.maxItems
        return additional * const.additionalItemFee
    return 0

def rushTime(time):
    dTime = dateutil.parser.isoparse(time)
    if dTime.weekday() == 4 and 15 <= dTime.hour <= 19:
        return True
    return False


def totalFees(numOfItems, distance, cartValue, time):
    if cartValue >= const.freeOfChargeValue:
        return 0
    
    total = cartValueFee(cartValue) + distanceFee(distance) + itemFee(numOfItems)

    if rushTime(time):
        total *= const.rushTimeMultiplier

    return min(const.maxDeliveryPrice, int(total))

    

    
    