a, b, c = [1,2,3]
print(f"a: {a}, b: {b}, c: {c}\n")
print(f"{a,b,c}\n")
print(a,b,c) 

*a, b, c = [1, 2, 3, 4, 5]
print(f"a: {a}, b: {b}, c: {c}\n")

List1 = [1,"Mack", 2, 4]
List2 = [5, "Styles", 6]
combined = [*List1, * List2]
print(combined)
 