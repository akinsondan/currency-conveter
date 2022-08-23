import requests

c_code = input().upper()
#ex_c = input()
#amount = float(input())
usd_eur = {}
eur_usd ={}
x_ex_dict = {}

r = requests.get(f"http://www.floatrates.com/daily/{c_code}.json").json()
if c_code == 'USD':
    usd_eur['eur'] = r['eur']
elif c_code == 'EUR':
    eur_usd['usd'] = r['usd']
else:
    x_ex_dict['usd'] = r['usd']
    x_ex_dict['eur'] = r['eur']

cache_code_list = []

while True:
    ex_c = input()
    if ex_c:
        amount = float(input())
    else:
        break
    print("Checking the cache...")

    if c_code == 'USD':
        if ex_c in usd_eur:
            print("Oh! It is in the cache!")
            print(f"You received {round(usd_eur[ex_c]['rate']*amount,2)} {ex_c.upper()}.")
        else:
            print("Sorry, but it is not in the cache!")
            print(f"You received {round(r[ex_c.lower()]['rate']*amount,2)} {ex_c.upper()}.")
            usd_eur[f"{ex_c.lower()}"] = r[f"{ex_c.lower()}"]
            continue

    elif c_code == 'EUR':
        if ex_c in eur_usd:
            print("Oh! It is in the cache!")
            print(f"You received {round(eur_usd[ex_c]['rate']*amount,2)} {ex_c.upper()}.")
        else:
            print("Sorry, but it is not in the cache!")
            print(f"You received {round(r[ex_c.lower()]['rate']*amount,2)} {ex_c.upper()}.")
            eur_usd[f"{ex_c.lower()}"] = r[f"{ex_c.lower()}"]
            continue

    elif ex_c in x_ex_dict:
        if ex_c == 'usd':
            print("Oh! It is in the cache!")
            print(f"You received {round(x_ex_dict[ex_c]['rate']*amount,2)} {ex_c.upper()}.")
            continue

        elif ex_c == 'eur':
            print("Oh! It is in the cache!")
            print(f"You received {round(x_ex_dict[ex_c]['rate']*amount,2)} {ex_c.upper()}.")
            cache_code_list.append(f"{ex_c}")
            continue

        elif ex_c != 'eur' and 'usd':
            print("Oh! It is in the cache!")
            print(f"You received {round(x_ex_dict[ex_c]['rate']*amount,2)} {ex_c.upper()}.")

    elif ex_c not in x_ex_dict:
        print("Sorry, but it is not in the cache!")
        print(f"You received {round(r[ex_c.lower()]['rate']*amount,2)} {ex_c.upper()}.")
        x_ex_dict[f"{ex_c.lower()}"] = r[f"{ex_c.lower()}"]
        continue
