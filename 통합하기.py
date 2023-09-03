import os
import shutil

# 복사할 이미지를 찾을 폴더의 루트 경로
root_folder = './'

# 대상 폴더(통합 폴더) 생성
destination_folder = './통합'
os.makedirs(destination_folder, exist_ok=True)

# 검색 키워드 설정
keyword = "식품영양정보"

# 이미 복사한 파일의 이름을 저장할 세트
copied_files = set()

# root_folder의 모든 하위 폴더와 파일을 검사
for foldername, subfolders, filenames in os.walk(root_folder):
    for filename in filenames:
        # 파일 이름에 키워드가 포함되어 있는지 확인
        if keyword in filename:
            # 파일의 원래 경로
            source_path = os.path.join(foldername, filename)

            # 대상 폴더에 이미 동일한 이름의 파일이 있는지 확인
            if filename not in copied_files:
                # 파일을 대상 폴더로 복사
                shutil.copy(source_path, destination_folder)
                print(f"파일 '{filename}'을 복사했습니다.")

                # 복사한 파일 이름을 세트에 추가
                copied_files.add(filename)
            else:
                print(f"파일 '{filename}'은 이미 복사되었습니다. 패스합니다.")

print("복사가 완료되었습니다.")