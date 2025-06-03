import os
import pandas as pd

# ==== CẤU HÌNH ====
folder_path = "Data"  # Thư mục chứa các file CSV cần gộp
output_file = "Data\\batdongsan_merged_full.csv"

# ==== LẤY DANH SÁCH FILE CSV ====
csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]
print(f"Tìm thấy {len(csv_files)} file CSV trong thư mục '{folder_path}'")

# ==== ĐỌC VÀ GỘP ====
all_dataframes = []
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    try:
        df = pd.read_csv(file_path)
        print(f"Đã đọc file: {file} ({df.shape[0]} dòng, {df.shape[1]} cột)")
        all_dataframes.append(df)
    except Exception as e:
        print(f"Lỗi khi đọc file {file}: {e}")

# ==== GỘP TOÀN BỘ ====
merged_df = pd.concat(all_dataframes, ignore_index=True, sort=False)
merged_df.drop_duplicates(subset="Link", inplace=True)

# ==== LƯU FILE ====
merged_df.to_csv(output_file, index=False, encoding="utf-8-sig")
print(f"\nGộp thành công {len(csv_files)} file! Đã lưu thành {output_file}")
print(f"Tổng cộng: {merged_df.shape[0]} dòng, {merged_df.shape[1]} cột")
