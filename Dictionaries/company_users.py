company_dict = {}

command = input()

while command != "End":
    company, name = command.split(" -> ")
    if company not in company_dict:
        company_dict[company] = []
    if name not in company_dict[company]:
        company_dict[company].append(name)
    command = input()

for companies in sorted(company_dict):
    print(companies)
    for names in company_dict[companies]:
        print(f"-- {names}")