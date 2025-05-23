import os
import time
import random
import requests
from bs4 import BeautifulSoup
from pathlib import Path
from typing import Set, List

def random_sleep(min_ms=3000, max_ms=27000):
    time.sleep(random.uniform(min_ms / 1000, max_ms / 1000))

def send_get_request(url: str, headers: dict) -> str:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def save_to_file(content: str, file_path: Path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def read_file(file_path: Path) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def get_tags(html: str) -> List[str]:
    soup = BeautifulSoup(html, 'html.parser')
    job_sectors = soup.select('.job_sector')
    tags = []

    for sector in job_sectors:
        spans = sector.select('span')
        for idx, span in enumerate(spans):
            if idx == 0:
                continue
            tag = span.get_text(strip=True)
            if tag and tag != '외':
                tags.append(tag)

    return tags

def crawl_saramin(save_dir: Path, end_page: int):
    save_dir.mkdir(parents=True, exist_ok=True)
    for i in range(1, end_page + 1):
        headers = {
            "accept": "*/*",
            "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,th;q=0.6",
            "content-type": "text/plain;charset=UTF-8",
            "origin": "https://www.saramin.co.kr",
            "referer": "https://www.saramin.co.kr/",
            "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
        }
        url = f"https://www.saramin.co.kr/zf_user/jobs/list/job-category?page={i}&cat_mcls=2&search_optional_item=n&search_done=y&panel_count=y&preview=y&page_count=100&isAjaxRequest=0&sort=RL&type=job-category&is_param=1&isSearchResultEmpty=1&isSectionHome=0&searchParamCount=1&tab=job-category#searchTitle"
        html = send_get_request(url, headers)
        save_to_file(html, save_dir / f"{i}.txt")
        random_sleep()

def parse_saramin(save_dir: Path, forbidden_words: Set[str]) -> Set[str]:
    tag_set = set()
    files = sorted([f for f in save_dir.glob('*.txt')], key=lambda x: int(x.stem))
    
    for file in files:
        html = read_file(file)
        tags = get_tags(html)
        for tag in tags:
            if tag not in forbidden_words:
                tag_set.add(tag.upper().strip())
    
    return tag_set
