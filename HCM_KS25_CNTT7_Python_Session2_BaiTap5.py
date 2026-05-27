
patient_name = input("Nhap ho ten benh nhan: ")

patient_age = int(input("Nhap tuoi benh nhan: "))

spo2_level = int(input("Nhap chi so SpO2 (%): "))

heart_rate = int(input("Nhap nhip tim (nhip/phut): "))

has_insurance = input(
    "Ban co the BHYT khong? (yes/no): "
).lower()


if spo2_level < 90 or heart_rate > 120:
    triage_result = "BAO DONG DO - CAP CUU KHAN"

elif (90 <= spo2_level <= 95) or (100 <= heart_rate <= 120):
    triage_result = "BAO DONG VANG - THEO DOI SAT"

else:
    triage_result = "XANH - KHAM THUONG"

base_fee = 500000

if patient_age < 6 or patient_age >= 80:
    hospital_fee = 0

elif has_insurance == "yes":
    hospital_fee = 250000

else:
    hospital_fee = base_fee

print("\n===== PHIEU KHAM BENH =====")

print("Ho ten:", patient_name)
print("Tuoi:", patient_age)
print("SpO2:", spo2_level)
print("Nhip tim:", heart_rate)
print("BHYT:", has_insurance)

print("\nKet qua phan luong:")
print(triage_result)

print("\nTam ung vien phi:")
print(f"{hospital_fee:,} VND")

print("\n===== LOG HE THONG =====")

print("patient_name =", type(patient_name))
print("patient_age =", type(patient_age))
print("spo2_level =", type(spo2_level))
print("heart_rate =", type(heart_rate))
print("has_insurance =", type(has_insurance))