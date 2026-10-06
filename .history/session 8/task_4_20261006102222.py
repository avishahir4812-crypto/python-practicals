def apply_coupon(amount, coupon_code=None):

    if coupon_code == "SAVE10":
        discount = amount * 0.10
        final_amount = amount - discount
    else:
        final_amount = amount

    return final_amount


# Without coupon
print("Without Coupon:", apply_coupon(1000))


# With coupon
print("With Coupon:", apply_coupon(1000, "SAVE10"))