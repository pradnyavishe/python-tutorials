staff = [("Amit", 16), ("Zara", 17), ("Raj", 15)]

for name, age in staff:
    if age <= 18:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print(f"No one is eligible to manage the staff")

# # This function will be tested automatically.
# # Do not change the function name or parameters.
# def scan_parcels(parcel_codes: list[str]) -> list[str]:
#     # Write your code below this line
#     messages = []
    
#     for code in parcel_codes:
#         if code == "DAMAGED":
#             messages.append("Skipped damaged parcel")
#             continue
#         elif code == "STOP":
#             messages.append( "Critical error: Stopping scan")
#             break
#         else:
#             messages.append("Scanned parcel: {code}")
#     else:
#         # This runs only if the loop completes without break
#         messages.append("All parcels scanned successfully")
        
#     return messages    
        
#     pass