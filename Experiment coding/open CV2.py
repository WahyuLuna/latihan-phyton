import cv2

# Fungsi untuk menangani setiap frame
def process_frame(frame):
    # Di sini, Anda dapat melakukan operasi pengolahan frame jika diperlukan
    # Contoh: Ubah frame menjadi abu-abu
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray_frame

# Buka kamera (ganti indeks sesuai kebutuhan)
cap = cv2.VideoCapture(1)

while True:
    # Baca frame dari kamera
    ret, frame = cap.read()

    # Cek nilai ret
    if not ret:
        print("Pembacaan frame gagal. Pastikan kamera terhubung dan berfungsi.")
        break

    # Panggil fungsi untuk memproses frame (jika diperlukan)
    processed_frame = process_frame(frame)

    # Tampilkan frame yang diproses dalam jendela
    cv2.imshow('Camera Feed', processed_frame)

    # Break loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tutup kamera dan jendela OpenCV
cap.release()
cv2.destroyAllWindows()
