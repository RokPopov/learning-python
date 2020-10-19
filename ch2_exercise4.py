# the cost of service per hour
cost_per_hour = 1.02

# compute the cost for service per day and month
cost_per_day = 24 * cost_per_hour
cost_per_month = 30 * cost_per_day

# compute the cost for service of 20 servers per day and month
cost_per_day_twenty = 20 * cost_per_day
cost_per_month_twenty = 20 * cost_per_month

# budgeting
budget = 1836
operational_days = budget / cost_per_day

# display the results
print("Cost to operate one server per day is {:.2f}eur.".format(cost_per_day))
print("Cost to operate one server per month is {:.2f}eur.".format(cost_per_month))
print("Cost to operate 20 servers per day is {:.2f}eur.".format(cost_per_day_twenty))
print("Cost to operate 20 servers per month is {:.2f}eur.".format(cost_per_month_twenty))
print("With the budget of {0:.2f}eur we can afford to operate 1 server for {1:.0f} days."
      .format(budget, operational_days))
