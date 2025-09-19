# The Triangle Factory

# https://open.kattis.com/problems/triangelfabriken

*c, = map(int,[input()for _ in' '*3])
if any(a>90 for a in c):
    print("Trubbig Triangel")
elif all(a<90 for a in c):
    print("Spetsig Triangel")
elif any(a==90 for a in c):
    print("Ratvinklig Triangel")