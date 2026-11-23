# PROGRAM MONITORING ERROR TERHADAP SETPOINT

# Menentukan nilai setpoint
setpoint = 50

# Data output dari soal dosen dan data tambahan
data_output = [
    50, 49, 47, 45, 43,
    52, 54, 57, 51, 48,
    46, 44, 53, 55, 42,
    48, 47, 55, 56, 60
]

# Function untuk menghitung error
def hitung_error(setpoint, output):
    error = abs(setpoint - output)
    return error

    # Function untuk menentukan status error
def status_error(error):
    if error <= 2:
        return "STABIL"
    elif error <= 5:
        return "WARNING"
    else:
        return "TIDAK STABIL"

        # Function untuk menghitung rata-rata
def rata_rata(data):
    return sum(data) / len(data)

    # Memproses seluruh data
data_error = []

print("===== MONITORING ERROR =====")

for nomor, output in enumerate(data_output, start=1):
    error = hitung_error(setpoint, output)
    status = status_error(error)

    data_error.append(error)

    print(f"{nomor:02d}. Output = {output} | Error = {error} | Status = {status}")
    # Menampilkan ringkasan hasil
print("\n===== RINGKASAN HASIL =====")

print("Total data:", len(data_output))
print("Jumlah STABIL:", sum(1 for e in data_error if status_error(e) == "STABIL"))
print("Jumlah WARNING:", sum(1 for e in data_error if status_error(e) == "WARNING"))
print("Jumlah TIDAK STABIL:", sum(1 for e in data_error if status_error(e) == "TIDAK STABIL"))
print("Rata-rata error:", rata_rata(data_error))
print("Error tertinggi:", max(data_error))
print("Error terendah:", min(data_error))