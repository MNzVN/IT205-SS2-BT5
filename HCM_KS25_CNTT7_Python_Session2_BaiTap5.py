name = input("Nhap ho ten: ")
age = int(input("Nhap tuoi: "))
spo2 = int(input("Nhap SpO2: "))
heart = int(input("Nhap nhip tim: "))
bhyt = input("Co the BHYT khong (yes/no): ")


if spo2 < 90 or heart > 120:
    triage = "DO (Cap cuu khan)"
elif (spo2 >= 90 and spo2 <= 95) or (heart >= 100 and heart <= 120):
    triage = "VANG (Theo doi sat)"
else:
    triage = "XANH (Kham thuong)"

if age < 6 or age >= 80:
    fee = 0
elif bhyt == "yes":
    fee = 250000
else:
    fee = 500000

print("--- PHIEU KHAM BENH DIEN TU ---")
print("Ten benh nhan:", name)
print("Tuoi:", age)
print("Phan luong:", triage)
print("Tien tam ung:", fee, "VND")

print("--- LOG HE THONG ---")
print("Bien name:", type(name))
print("Bien age:", type(age))
print("Bien spo2:", type(spo2))
print("Bien heart:", type(heart))
print("Bien bhyt:", type(bhyt))