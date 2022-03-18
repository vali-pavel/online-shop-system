from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Response,
    Request,
)
from . import schemas
from order import Order


router = APIRouter(prefix="/api")


@router.post("/orders")
def submit_order(request: Request, order_request: schemas.Order):
    order = Order(
        auth_token=request.headers["authorization"],
        product_id=order_request.product_id,
        order_quantity=order_request.quantity,
    )
    product_inventory = order.get_product_inventory()
    if product_inventory == None:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            "Could not get the inventory from the specified product",
        )

    new_inventory = order.calculate_new_inventory(product_inventory)
    if new_inventory < 0:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            "Not enough quantity available for this product",
        )

    is_valid_customer = order.validate_customer(order_request.user_id)
    if not is_valid_customer:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            "Invalid customer or customer fields provided",
        )
    order.submit_order(new_inventory)
    return Response(None, status.HTTP_200_OK)
