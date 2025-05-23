from pathlib import Path
from crawler.saramin_crawler import SaramInCrawler
from processor.tag_processor import TagProcessor

if __name__ == "__main__":
    site = "saramin"
    forbidden_words = {"JAVA", "PYTHON", "C"}

    crawler = SaramInCrawler(Path("data/raw/" + site), page_end=5)
    processor = TagProcessor(crawler, Path("data/collected_from/" + site + ".txt"))
    processor.execute(forbidden_words)
