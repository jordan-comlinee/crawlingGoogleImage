import os

folder_path = "./통합"  # 이미지 파일들이 있는 폴더 경로

# 폴더 내의 모든 파일 리스트 가져오기
file_list = os.listdir(folder_path)

# 이미지 파일 확장자들
image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]

count = 0

for filename in file_list:
    # 파일의 확장자 확인
    file_extension = os.path.splitext(filename)[1].lower()

    # 이미지 파일인 경우에만 이름 변경
    if file_extension in image_extensions:
        new_extension = ".png"  # 확장자를 .png로 통일
        new_filename = f"{count}{new_extension}"
        new_path = os.path.join(folder_path, new_filename)
        old_path = os.path.join(folder_path, filename)

        # 이미지 파일의 이름 변경
        os.rename(old_path, new_path)

        count += 1

print("이미지 파일 이름 변경 및 확장자 통일 완료")