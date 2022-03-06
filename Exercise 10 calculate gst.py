def calc_gst(net_price):
    gst_inclusive = net_price * 1.15
    return gst_inclusive


# Main Routine
enter_gst = int(input("Enter the gst exclusive price: "))
print(f"The gst inclusive price is ${calc_gst(enter_gst)}")
