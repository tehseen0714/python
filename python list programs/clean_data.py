raw_data = [
    {"user_id": 1, "name": "  Alice Smith  ", "status": "active", "purchase_amount": "150.50", "signup_date": "2023/05/12", "tags": ["premium", "newsletter"]},
    {"user_id": 2, "name": "BOB JONES", "status": "inactive", "purchase_amount": "0.00", "signup_date": "2023/08/21", "tags": ["free"]},
    {"user_id": 3, "name": "Charlie brown", "status": "active", "purchase_amount": "invalid_data", "signup_date": "2024/01/05", "tags": ["premium"]},
    {"user_id": 4, "name": "   ", "status": "active", "purchase_amount": "45.00", "signup_date": "2024/02/10", "tags": ["free", "newsletter"]},
    {"user_id": 5, "name": "Eve Davis", "status": "ACTIVE", "purchase_amount": "300.00", "signup_date": "2023/11/30", "tags": ["premium", "referral"]}
]

# to clean the data 
cleaned_data=[]
for record in raw_data:

    #clean user name
    name=record["name"].strip().title()
    if name=="":
        continue

    # clean purchase amount
    if record["purchase_amount"] == "invalid_data":
     purchase = 0.0
    else:
     purchase = float(record["purchase_amount"])

    #cleaned_record
    cleaned_record = {
        "user_id":record ["user_id"],
        "name":name,
        "status":record["status"].lower(),
        "purchase_amount":purchase,
        "signup_date":record["signup_date"].replace("/","-"),
        "tags":record["tags"]
    }
    cleaned_data.append(cleaned_record)
print("cleaned data:")
for user in cleaned_data:
  print(user)


# select distinct elements
distinct_tags= set()
for user in cleaned_data:
    for tag in user["tags"]:
        distinct_tags.add(tag)

print("distinct tags:")
print(distinct_tags)


# yearly revenue
yearly_revenue = {}
for user in cleaned_data:
    year = user["signup_date"][:4]
    if year not in yearly_revenue:
        yearly_revenue[year] = 0.0
    yearly_revenue[year] += user["purchase_amount"]

print("\nYearly Revenue:")
print(yearly_revenue)