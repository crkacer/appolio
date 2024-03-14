from rentoro.models import RentalPropertyShare
from rentoro.models import RentalProperty, RentalPropertyUnit, LandlordProfile
from rentoro.utils.property_code import generate_unique_property_code
import logging 

def fetch_rental_share_code(rental: RentalProperty) -> str:
    logger = logging.getLogger('django')
    try:
        # find rental_share, if cannot then create
        rental_share = RentalPropertyShare.objects.filter(rental_id=rental.id).first()
        if not rental_share:
            rental_share = RentalPropertyShare(rental=rental)
            rental_share.save()

        while True:
            code = generate_unique_property_code()
            if not RentalPropertyShare.objects.filter(unique_code=code).exists():
                break

        rental_share.unique_code = code
        rental_share.expire_at = ""
        rental_share.save()

        return code
    
    except Exception as e:
        logger.info(str(e))
        return ""

