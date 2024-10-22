import os
import shutil

# 다운로드 폴더 경로
download_folder = r'C:\Users\student\Downloads'

# 이동할 폴더 경로
image_folder = os.path.join(download_folder, 'images')
data_folder = os.path.join(download_folder, 'data')
docs_folder = os.path.join(download_folder, 'docs')
archive_folder = os.path.join(download_folder, 'archive')

# 파일 확장자에 따른 이동 규칙
file_types = {
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'],
    'data': ['.csv', '.xlsx', '.xls'],
    'docs': ['.txt', '.doc', '.pdf'],
    'archive': ['.zip', '.rar', '.tar', '.gz', '.bz2']
}

# 폴더가 존재하지 않으면 생성하는 함수
def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# 중복 파일명 처리 함수
def get_unique_file_path(folder_path, filename):
    base, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename

    # 파일이 이미 존재하면 새로운 파일명을 생성
    while os.path.exists(os.path.join(folder_path, new_filename)):
        new_filename = f"{base}({counter}){extension}"
        counter += 1
    
    return os.path.join(folder_path, new_filename)

# 각 폴더가 없으면 생성
create_folder_if_not_exists(image_folder)
create_folder_if_not_exists(data_folder)
create_folder_if_not_exists(docs_folder)
create_folder_if_not_exists(archive_folder)

# 다운로드 폴더 내 파일을 순회
for filename in os.listdir(download_folder):
    # 파일 경로
    file_path = os.path.join(download_folder, filename)
    
    # 디렉토리가 아니고 파일일 경우만 처리
    if os.path.isfile(file_path):
        # 파일 확장자 추출
        _, extension = os.path.splitext(filename)

        # 확장자에 따라 적절한 폴더로 이동
        if extension.lower() in file_types['images']:
            target_folder = image_folder
        elif extension.lower() in file_types['data']:
            target_folder = data_folder
        elif extension.lower() in file_types['docs']:
            target_folder = docs_folder
        elif extension.lower() in file_types['archive']:
            target_folder = archive_folder
        else:
            continue  # 해당되지 않는 확장자는 무시

        # 중복된 파일명을 처리하여 새로운 경로 설정
        new_file_path = get_unique_file_path(target_folder, filename)
        
        # 파일 이동
        shutil.move(file_path, new_file_path)

print("파일 정리가 완료되었습니다.")

https://www.gpters.org/data-science