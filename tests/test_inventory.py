from inventory import calculate_total


def test_no_discount_below_threshold():
    assert calculate_total(10.0, 5) == 50.0


def test_bulk_discount_at_threshold():
    assert calculate_total(10.0, 10) == 90.0


def test_bulk_discount_above_threshold():
    assert calculate_total(2.0, 20) == 36.0
