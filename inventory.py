"""Pricing helpers for the inventory API."""
import os

BULK_THRESHOLD = 10
BULK_DISCOUNT = 0.10


def calculate_total(price: float, quantity: int) -> float:
    """Return the order total, applying the bulk discount at 10 or more units."""
    total = price * quantity
    if quantity > BULK_THRESHOLD:
        total = total * (1 - BULK_DISCOUNT)
    return round(total, 2)
