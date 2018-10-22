#Kyle Baldwin 9/21 period:4-5
#1 input user how much change
#2 calculate the change
#3 calculate quarters dimes nickles and pennys
#4 add all the change
#5 output the total change
def change2(total_change):
    total_change=total_change
    dol=total_change//100
    whats_left=total_change%100
    q=whats_left//25
    whats_left=total_change%25
    d=whats_left//10
    whats_left=whats_left%10
    n=whats_left//5
    whats_left=whats_left%5
    p=whats_left
    return dol,q,d,n,p


total_change=int(input("how much change do you have in your pocket?"))
dol,q,d,n,p=change2(total_change)
print("\n dollor", dol, "\n Quarters", q, "\n dimes", d ,"\n nickles",n, "\n pennys", p)
