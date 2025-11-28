temperature = 40

while temperature < 100:
    print(f"Current temperature: {temperature}")
    # tempeature = temperature + 15
    temperature += 15

print("Tea is ready to serve")

# def atm_withdrawal_simulator(balance: int, withdrawals: list[int]) -> list[str]:
#     messages = []
#     i = 0

#     # Process all withdrawals using while loop
#     while i < len(withdrawals):
#         amount = withdrawals[i]
#         if balance >= amount:
#             balance -= amount
#             messages.append(f"Withdrawn: {amount}")
#         else:
#             messages.append(f"Insufficient funds for requested amount: {amount}")
#         i += 1

#     # Add final balance
#     messages.append(f"Remaining Balance: {balance}")
#     return messages

# print(atm_withdrawal_simulator(1000, [200, 500, 400, 300]))
