import bs4
import requests
from pathlib import Path
from typing import Callable


def generate_filename(name: str) -> str:
    is_valid_char: Callable[[str], bool] = lambda char: char.isalnum() or char.isspace()
    get_char_value: Callable[[str], str] = lambda char: char if char.isalnum() else '_'
    formatted_name = name.strip().lower()
    return ''.join(get_char_value(char) for char in formatted_name if is_valid_char(char))


def save_image(img_url: str, path: Path):
    img_response = requests.get(img_url)
    # wb: write binary
    img_file = open(path, 'wb')
    img_file.write(img_response.content)
    img_file.close()


courses_page_url = 'https://escueladirecta.com/courses'

courses_page_response = requests.get(courses_page_url)

courses_page_soup = bs4.BeautifulSoup(courses_page_response.text, 'lxml')

courses = courses_page_soup.select('.course-list .course-listing')

images_path = Path(Path.cwd(), 'images')

if not images_path.exists():
    Path.mkdir(images_path)

for course in courses:
    course_title = course.select_one('.course-listing-title').getText()
    course_img = course.select_one('img.course-box-image')
    img_filename = f"{generate_filename(course_title)}.jpg"
    save_image(course_img['src'], Path(images_path, img_filename))
