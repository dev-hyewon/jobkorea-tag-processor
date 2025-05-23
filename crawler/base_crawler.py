from abc import ABC, abstractmethod
from pathlib import Path
from typing import Set

class BaseCrawler(ABC):

    def __init__(self, save_dir: Path, page_end: int):
        self.save_dir = save_dir
        self.page_end = page_end

    @abstractmethod
    def crawl(self):
        pass

    @abstractmethod
    def parse(self, forbidden_words: Set[str]) -> Set[str]:
        pass
