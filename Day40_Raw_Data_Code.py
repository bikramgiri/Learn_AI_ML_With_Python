import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv("Raw_Data.csv")
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

# Case-1:
# plt.plot(ages, dev_salaries, linestyle='--', label='Full stack devs')

# plt.fill_between(ages, dev_salaries, interpolate = True, color = 'red', label = "Fill area", alpha = 0.3)


# *Case-2:
plt.plot(ages, dev_salaries, linestyle='--', label='Full stack devs')

plt.plot(ages, py_salaries, label='Python devs')

plt.fill_between(ages, py_salaries, dev_salaries, where = (py_salaries > dev_salaries), interpolate = True, color='blue', alpha=0.25, label="Above Full stack Devs")

plt.fill_between(ages, py_salaries, dev_salaries, where = (py_salaries <= dev_salaries), interpolate = True, color='red', alpha=0.25, label="Below Full stack Devs")


plt.legend()
plt.title('Median Salaries in USD by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary in USD')

plt.tight_layout()
plt.show()