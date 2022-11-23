import re

print("\n-------- Advance Python Calculator ---------")
print("p.s. \"It still doesn't have PEMDAS Rules Applied, it can only calculate from left to right\"")
print("Only supporting the following operations: (+ - / *)\n")

def Filter(x, m, values):
    x_var = x
    value = False
    while value is False:
        if x_var == "/exit":
            value = True
            break
        for i in x_var:
            if i not in values:
                print("Invalid input.")
                value = False
                x_var = input(f"\n{m}")
                break
            else:
                value = True
    return x_var

while True:
    m = "Input: "
    initial_db = re.split('(\W)', (Filter(input(m), m, "1234567890+-/* ")))
    filtered_db = []
    for i in initial_db:
        if i.strip():
            filtered_db.append(i)
    
    if ("".join(filtered_db) == "/exit"):
        break
    
    dialog_box = 0
    dialog_box += int(filtered_db[0])

    if ("".join(filtered_db).isdigit()):
        print("= " + ("".join(filtered_db)))
    else:
        for i in filtered_db:
            if i == "+":
                dialog_box += int(filtered_db[filtered_db.index(i) + 1])
                filtered_db.remove(i)
            elif i == "-":
                dialog_box -= int(filtered_db[filtered_db.index(i) + 1])
                filtered_db.remove(i)
            elif i == "*":
                dialog_box *= int(filtered_db[filtered_db.index(i) + 1])
                filtered_db.remove(i)
            elif i == "/":
                dialog_box /= int(filtered_db[filtered_db.index(i) + 1])
                filtered_db.remove(i)
        print(f"= {dialog_box}")


