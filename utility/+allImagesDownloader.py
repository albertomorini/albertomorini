from pathlib import Path
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,"
        "application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
}


def get_image_url(img_tag):
    """
    Extract best possible image URL from an <img> tag.
    """

    for attr in ("data-srcset", "data-src", "data-fallback-src", "src"):
        value = img_tag.get(attr)

        if value:
            # srcset may contain multiple URLs
            if attr == "data-srcset":
                return value.split(",")[0].split()[0]

            return value

    return None


def get_extension(url):
    """
    Extract file extension from URL.
    """

    path = urlparse(url).path
    ext = Path(path).suffix.lower()

    if ext in [".jpg", ".jpeg", ".png", ".gif", ".webp"]:
        return ext

    return ".jpg"


def download_images(url, folder_name="downloads"):
    folder = Path(folder_name)
    folder.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    session.headers.update(HEADERS)

    print(f"Fetching page: {url}")

    try:
        response = session.get(
            url,
            timeout=15,
            headers={
                **HEADERS,
                "Referer": "https://www.google.com/",
                "Accept": (
                    "text/html,application/xhtml+xml,"
                    "application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
                ),
                "Accept-Language": "en-US,en;q=0.5",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
            },
        )
        
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch page: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # FIXED: findAll -> find_all
    images = soup.find_all("img")

    print(f"Found {len(images)} image tags")

    downloaded = 0
    seen = set()

    for idx, img in enumerate(images, start=1):

        image_url = get_image_url(img)

        if not image_url:
            continue

        # Convert relative URLs to absolute
        image_url = urljoin(url, image_url)

        # Skip duplicates
        if image_url in seen:
            continue

        seen.add(image_url)

        try:
            img_response = session.get(image_url, timeout=15)

            if img_response.status_code != 200:
                continue

            content_type = img_response.headers.get("content-type", "")

            if "image" not in content_type:
                continue

            extension = get_extension(image_url)

            filename = folder / f"image_{idx}{extension}"

            with open(filename, "wb") as f:
                f.write(img_response.content)

            downloaded += 1

            print(f"[{downloaded}] Saved: {filename.name}")

        except requests.RequestException as e:
            print(f"Failed to download {image_url}: {e}")

    print(f"\nDownloaded {downloaded} images")


if __name__ == "__main__":
    download_images(
        "https://www.zipcomic.com/the-boys-issue-1",
        "1"
    )