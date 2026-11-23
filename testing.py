#PROGRAM PENGUJIAN (TESTING)

setpoint = 50

def hitung_error(setpoint, output):
    return abs(setpoint - output)

def status_error(error):
    if error <= 2:
       return "STABIL"
    elif error <= 5:
       return "WARNING"
    else:
       return "TIDAK STABIL"

#Data pengujian

data_testing = [
(50, "STABIL"),
(49.5, "STABIL"),
(49, "STABIL"),
(48, "STABIL"),
(47, "WARNING"),
(46, "WARNING"),
(45, "WARNING"),
(44, "TIDAK STABIL"),
(52, "STABIL"),
(60, "TIDAK STABIL")
]

print("========== HASIL PENGUJIAN ==========")
print(f"Setpoint: {setpoint}")
print("-" * 85)

lulus = 0
gagal = 0

for nomor, (output, harapan) in enumerate(data_testing, start=1):

    error = hitung_error(setpoint, output)

    aktual = status_error(error)

    status = "PASS" if aktual == harapan else "FAIL"

    if status == "PASS":

        lulus += 1

    else:

        gagal += 1

    print(f"Test {nomor}")

    print(f"Nilai Output Aktual : {output}")

    print(f"Nilai Error Aktual  : {error}")

    print(f"Hasil yang Diharapkan: {harapan}")

    print(f"Hasil Aktual        : {aktual}")

    print(f"Status Pengujian    : {status}")

    print("-" * 85)

print("========== RINGKASAN ==========")
print(f"Total Pengujian : {len(data_testing)}")
print(f"PASS            : {lulus}")
print(f"FAIL            : {gagal}")
print(f"Status Akhir    : {'LULUS' if gagal == 0 else 'PERLU PERBAIKAN'}")