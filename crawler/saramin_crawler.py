import time
import random
import requests
from bs4 import BeautifulSoup
from pathlib import Path
from typing import Set, List

from crawler.base_crawler import BaseCrawler


class SaramInCrawler(BaseCrawler):
    def __init__(self, save_dir: Path, page_end: int):
        super().__init__(save_dir, page_end)

    def crawl(self):
        self.save_dir.mkdir(parents=True, exist_ok=True)

        for i in range(1, self.page_end + 1):
            url = f"https://www.saramin.co.kr/zf_user/jobs/list/job-category?page={i}&cat_mcls=2&search_optional_item=n&search_done=y&panel_count=y&preview=y&page_count=100&isAjaxRequest=0&sort=RL&type=job-category&is_param=1&isSearchResultEmpty=1&isSectionHome=0&searchParamCount=1&tab=job-category#searchTitle"
            headers = {
                "accept": "*/*",
                "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,th;q=0.6",
                "content-type": "text/plain;charset=UTF-8",
                "origin": "https://www.saramin.co.kr",
                "referer": "https://www.saramin.co.kr/",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
            }

            response = requests.get(url, headers=headers)
            response.raise_for_status()

            file_path = self.save_dir / f"{i}.txt"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(response.text)

            time.sleep(random.uniform(3, 27))  # 랜덤 딜레이 (3~27초)

    def parse(self, forbidden_words: Set[str]) -> Set[str]:
        tag_set = set()
        files = sorted([f for f in self.save_dir.glob('*.txt') if f.is_file()],
                       key=lambda x: int(x.stem))

        for file in files:
            with open(file, 'r', encoding='utf-8') as f:
                html = f.read()
                tags = self._extract_tags(html)
                for tag in tags:
                    tag_upper = tag.upper().strip()
                    if tag_upper not in forbidden_words:
                        tag_set.add(tag_upper)

        return tag_set

    def _extract_tags(self, html: str) -> List[str]:
        soup = BeautifulSoup(html, 'html.parser')
        job_sectors = soup.select('.job_sector')
        tags = []

        for sector in job_sectors:
            spans = sector.select('span')
            for idx, span in enumerate(spans):
                if idx == 0:
                    continue  # 첫 span은 직군명 (제외)
                tag = span.get_text(strip=True)
                if tag and tag != '외':
                    tags.append(tag)

        return tags
