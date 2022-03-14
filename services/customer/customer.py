from api import schemas


class Customer:
    @staticmethod
    def validate_checkout(customer: schemas.CustomerBase) -> bool:
        if (
            not customer.billing_address
            or not customer.shipping_address
            or not customer.card_expiration
            or not customer.card_holder
            or not customer.card_number
        ):
            return False
        return True
