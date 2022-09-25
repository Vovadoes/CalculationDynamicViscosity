import json
import math

# System consts

path_to_A = "./student_coefficient.json"

# Consts
G = 9.81
A = None
dG = 0.006
Nmax = 5

p = float(input("p = "))
dp = float(input("dp = "))
p0 = float(input("p0 = "))
dp0 = float(input("dp0 = "))
l = float(input("l = "))
dl = float(input("dl = "))
t = float(input("t = "))
dt = float(input("dt = "))
ddnp = float(input("ddnp = "))

n = int(input("Количество измерений"))

measurements = []
for i in range(n):
    d = float(input(f"d{i + 1} = "))
    dd = float(input(f"dd{i + 1} = "))
    measurements.append({"d": d, "dd": dd})
del d, dd

# Change A to n
with open(path_to_A, "r", encoding="UTF-8") as f:
    A = round(json.loads(f.read())[str(n)]["0.95"], 2)

# print(f"{A=}, {n=}")

ddcn = A * math.sqrt(sum([i["dd"] ** 2 for i in measurements]) / (n * (n - 1)))

dcp = sum([i["d"] for i in measurements]) / n

dd = ddcn + ddnp

E = (dG / G) + ((dp + dp0) / (p - p0)) + 2 * (dd / dcp) + (dl / l) + (dt / t)

nl = (G / 18) * ((p - p0) / (l / 100)) * ((dcp / 1000) ** 2) * t

dnl = nl * E

print(f"nl = {round(nl, 10)} +- {round(dnl, 10)} Па*с")
print(f"Ee = {round(E * 100, 2)} %")
