#name: joosan tibbetts
#desc: post office

SHIPPING_COST = .27
package_weight = 0

while True:
    try:
        package_weight = float(input("Enter package weight: "))
        if package_weight < 0.2 or package_weight > 65.75:
            raise Exception("Package weight out of range")
        else: break
    except BaseException as e:
        print(f"Invalid input: {e}")

COST_TO_SHIP = SHIPPING_COST * package_weight

print("-" * 50)
print(f"Your package weighs {package_weight} lb(s) and will cost ${COST_TO_SHIP}.")
print("-" * 50)