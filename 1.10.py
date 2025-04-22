# Convert dollars into pounds
dollars = 10
usd_to_inr = 48
inr_to_gbp = 70

# First, convert dollars to rupees
rupees = dollars * usd_to_inr

# Then, convert rupees to pounds
pounds = rupees / inr_to_gbp

print(f"{dollars} dollars is equal to {pounds} pounds.")
