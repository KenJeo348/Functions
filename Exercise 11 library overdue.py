def calc_fine(days_overdue):
    base_charge = 0.5
    daily_charge = 0.8
    total_fine = base_charge + daily_charge * days_overdue
    if total_fine > 30:
        total_fine = 30
    return total_fine


# Main Routine
days_overdue_ = int(input("Days Overdue: "))
print(f"${calc_fine(days_overdue_):.2f}")

