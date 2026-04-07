from tools import search_flights, search_hotels, calculate_budget

print("--- Testing search_flights ---")
print(search_flights.invoke({"origin": "Hà Nội", "destination": "Đà Nẵng"}))
print("\n--- Testing search_hotels ---")
print(search_hotels.invoke({"city": "Đà Nẵng", "max_price_per_night": 1500000}))
print("\n--- Testing calculate_budget ---")
print(calculate_budget.invoke({"total_budget": 5000000, "expenses": "Vé máy bay: 1.450.000, Khách sạn: 2.100.000, Ăn uống: 1.000.000"}))
