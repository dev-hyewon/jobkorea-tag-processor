from pathlib import Path
from typing import Set
from crawler.base_crawler import BaseCrawler

class TagProcessor:
    def __init__(self, crawler: BaseCrawler, result_file: Path):
        self.crawler = crawler
        self.result_file = result_file

    def execute(self, forbidden_words: Set[str]):
        print("크롤링 시작...")
        self.crawler.crawl()

        print("파싱 시작...")
        tags = self.crawler.parse(forbidden_words)

        self._save_tags_to_file(tags)
        print(f"결과가 {self.result_file} 에 저장되었습니다.")

    def _save_tags_to_file(self, tags: Set[str]):
        self.result_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.result_file, 'w', encoding='utf-8') as f:
            for tag in sorted(tags):
                f.write(tag + '\n')
