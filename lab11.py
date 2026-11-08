# REFLECTION
# 1. Use .get() when a key might not exist and you want to provide a fallback 
#    default value without breaking your program (great for messy data or optional fields). 
#    Use bracket notation when the key is strictly required for the logic to work, 
#    and a missing key indicates a critical bug that should crash the program immediately.
#
# 2. This pattern is the equivalent of an Excel Pivot Table or a SUMIF formula. 
#    The Python version is more useful for large datasets because it doesn't suffer 
#    from row-count limits, runs faster on millions of rows, and can be automated 
#    seamlessly into larger data pipelines without manual spreadsheet steps.

# EXERCISE 1 · Beginner: One customer
print("--- Exercise 1 ---")
customer = {
    "name": "Alice Smith",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.50
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# EXERCISE 2 · Beginner: Update and add
print("\n--- Exercise 2 ---")
customer["phone"] = "555-0199"
print("After adding phone:", customer)

customer["tier"] = "platinum"
print("After updating tier:", customer)

del customer["email"]
print("After deleting email:", customer)


# EXERCISE 3 · Beginner: Safe lookup
print("\n--- Exercise 3 ---")
# Safe lookup with .get()
email_safe = customer.get("email", "no email on file")
print("Safe lookup result:", email_safe)

# Bracket notation lookup with try/except
try:
    email_unsafe = customer["email"]
except KeyError:
    print("Caught KeyError: 'email' key does not exist.")


# EXERCISE 4 · Beginner: Iterate
print("\n--- Exercise 4 ---")
for key, value in customer.items():
    print(f"{key}: {value}")

# Note: If you iterate without .items() (e.g., `for key in customer:`), 
# you only get the keys, not the values. You would then have to look up 
# each value manually using bracket notation like `customer[key]`.


# EXERCISE 5 · Intermediate: Lookup table
print("\n--- Exercise 5 ---")
tier_discounts = {"bronze": 0, "silver": 0.05, "gold": 0.10, "platinum": 0.15}

current_tier = customer.get("tier", "bronze")
discount_rate = tier_discounts.get(current_tier, 0)

purchase_amount = 200
discounted_price = purchase_amount * (1 - discount_rate)

print(f"Tier: {current_tier}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Final Price: ${discounted_price:.2f}")


# EXERCISE 6 · Intermediate: List of dicts
print("\n--- Exercise 6 ---")
customers = [
    {"name": "Bob Jones", "tier": "bronze"},
    {"name": "Charlie Brown", "tier": "silver"},
    {"name": "Diana Prince", "tier": "gold"}
]

for c in customers:
    t = c["tier"]
    rate = tier_discounts.get(t, 0)
    discount_amount = 300 * rate
    print(f"{c['name']} ({t}): ${discount_amount:.2f} discount on $300 purchase")


# EXERCISE 7 · Intermediate: Nested catalog
print("\n--- Exercise 7 ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK ALERT: {product} has only {info['stock']} units left!")


# EXERCISE 8 · Advanced: Sales by region
print("\n--- Exercise 8 ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_summary = {}
for tx in transactions:
    reg = tx["region"]
    amt = tx["amount"]
    sales_summary[reg] = sales_summary.get(reg, 0) + amt

# Print sorted by region name
for reg in sorted(sales_summary.keys()):
    print(f"{reg}: {sales_summary[reg]}")