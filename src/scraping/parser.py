from bs4 import BeautifulSoup


class HTMLPageParser:
    """HTML 页面解析器."""

    def parse(self, html, parser="lxml"):
        return BeautifulSoup(html, parser)

    def find_text(self, soup, tag, class_name=None):
        element = soup.find(tag, class_=class_name)
        return element.get_text(strip=True) if element else None

    def find_all_items(self, soup, tag, class_name=None):
        return soup.find_all(tag, class_=class_name)
