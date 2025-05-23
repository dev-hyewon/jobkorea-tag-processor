# 환경변수 적용
# from dotenv import load_dotenv
# load_dotenv()

from pathlib import Path
from crawler.saramin_crawler import crawl_saramin, parse_saramin

def save_tags_to_file(tags, file_path: Path):
    with open(file_path, 'w', encoding='utf-8') as f:
        for tag in sorted(tags):
            f.write(tag + '\n')

if __name__ == "__main__":
    raw_dir = Path("data/raw/saramin")
    raw_dir.parent.mkdir(parents=True, exist_ok=True)
    end_page = 3  # 원하는 크롤링 페이지 수
    forbidden_words = {"JAVA", "C", "PYTHON"}  # 예시로 금지어 설정

    print("크롤링 시작...")
    crawl_saramin(raw_dir, end_page)

    print("태그 파싱 중...")
    tags = parse_saramin(raw_dir, forbidden_words)

    processed_dir = Path("data/processed/saramin.txt")
    processed_dir.parent.mkdir(parents=True, exist_ok=True)
    save_tags_to_file(tags, processed_dir)
    print(f"결과 태그가 {processed_dir} 파일에 저장되었습니다.")