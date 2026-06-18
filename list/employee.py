employee_details =  {"emmu":1000,"waleed":100,"saanu":50,"afsal":300,"sinu":150,"ani":500,"ammu":100}
salaries = list(employee_details.values())
salaries.sort(reverse=True)
top_three = salaries[0:3:1]
for key,value in employee_details.items():
    if employee_details[key] in top_three:
        print(key,value)