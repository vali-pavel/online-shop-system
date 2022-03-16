from dataclasses import dataclass
from typing import Union
import requests

import constants


@dataclass
class Order:
    auth_token: str
    product_id: int
    order_quantity: int

    def get_product_inventory(self) -> Union[int, None]:
        product_response = requests.get(
            f"{constants.PRODUCTS_API_URL}/{self.product_id}/inventory",
            headers=self._get_auth_header(),
        )
        if product_response.status_code != 200:
            return None

        response_json = product_response.json()
        return response_json["inventory"]

    def calculate_new_inventory(self, inventory) -> int:
        return inventory - self.order_quantity

    def validate_customer(self, customer_id: int) -> bool:
        customer_validation_response = requests.get(
            f"{constants.CUSTOMERS_API_URL}/{customer_id}/validate",
            headers=self._get_auth_header(),
        )
        if customer_validation_response.status_code != 200:
            return False

        return True

    def submit_order(self, new_inventory: int):
        requests.put(
            f"{constants.PRODUCTS_API_URL}/{self.product_id}/inventory",
            headers=self._get_auth_header(),
            data={"inventory": new_inventory},
        )

    def _get_auth_header(self):
        return {"authorization": self.auth_token}
