import hashlib

def create_hash(data):
    # Membuat objek hash
    hasher = hashlib.sha256()

    # Mengupdate hash dengan data
    hasher.update(data.encode('utf-8'))

    # Mengambil nilai hash dalam format heksadesimal
    hash_value = hasher.hexdigest()

    return hash_value

# Contoh penggunaan
original_data = "Hello, World!"
hash_result = create_hash(original_data)
print(hash_result)
print(f"Data asli: {original_data}")
print(f"Nilai Hash: {hash_result}")

# Fungsi untuk memverifikasi data
def verify_data(data, hash_to_verify):
    return create_hash(data) == hash_to_verify

# Contoh penggunaan verifikasi
data_to_verify = "Hello, World!"
#hash_to_verify = "eeb9a43a46d1d5c7eaab1e2b2a8b09789d35179c0517a0a0f017129b721e642e"
hash_to_verify = "dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f"

if verify_data(data_to_verify, hash_to_verify):
    print("Data valid.")
else:
    print("Data tidak valid.")
