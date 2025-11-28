# boolean

is_boiling = True
stir_count = 5
total_actions = stir_count + is_boiling  # upcasting
print(f"Total actions: {total_actions}")

milk_present = 0  # no milk
print(f"Is there milk? {bool(milk_present)}")

milk_present = 1  # no milk
print(f"Is there milk? {bool(milk_present)}")

milk_present = 00  # no milk
print(f"Is there milk? {bool(milk_present)}")

milk_present = 11  # no milk
print(f"Is there milk? {bool(milk_present)}")

milk_present = "pradnya"  # no milk
print(f"Is there milk? {bool(milk_present)}")

milk_present = None  # no milk
print(f"Is there milk? {bool(milk_present)}")

water_hot = True
tea_added = False

can_server = water_hot and tea_added
print(f"Can serve chai? {can_server}")

can_server = water_hot or tea_added
print(f"Can serve chai? {can_server}")