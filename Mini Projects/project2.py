def main():
    cost_per_hour = 0.51
    hours_per_day = 24
    days_per_week = 7
    days_per_month = 30
    
    cost_per_day = cost_per_hour * hours_per_day
    cost_per_week = cost_per_day * days_per_week
    cost_per_month = cost_per_day * days_per_month
    
    budget = 918
    days_can_operate = budget / cost_per_day
    
    print(f"How much does it cost to operate one server per day? ${cost_per_day:.2f}")
    print(f"How much does it cost to operate one server per week? ${cost_per_week:.2f}")
    print(f"How much does it cost to operate one server per month? ${cost_per_month:.2f}")
    print(f"How many days can I operate one server with ${budget}? {int(days_can_operate)} days")

if __name__ == "__main__":
    main()
