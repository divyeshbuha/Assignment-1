# import cv2
# import os
# import pytesseract
# from PIL import Image
#
# def decode(image_path):
#     try:
#         # We then read the image with text
#         image_read = cv2.imread(image_path)
#         # convert to grayscale image
#         gray = cv2.cvtColor(image_read, cv2.COLOR_BGR2GRAY)
#         # memory usage with image i.e. adding image_read to memory
#         filename = os.path.dirname(image_path)+"{0}.jpg".format("\\grey_scale_image")
#
#         cv2.imwrite(filename, gray)
#         # use for window
#         pytesseract.pytesseract.tesseract_cmd = "{0}/tesseract.exe".format(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#         text = pytesseract.image_to_string(Image.open(filename))
#         os.remove(filename)
#         return text.split("\n")[0].strip()
#     except Exception as e:
#         return None
import requests
from bs4 import BeautifulSoup

class Centralpower():
    def __init__(self):
        self.headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',

        }

    def get_pdf(self):
        login_url = requests.get('http://data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJYAAAAyCAIAAAAx7rVNAAAFG0lEQVR42u2Zf0xVZRjHvxdwd3CHo4AaDZ0/8dKP1UhwIzAYE8nKBY7KxBQJiJQfpmYqRBmggxuXkQis0TT1nxq11UzWz+EftaKNrE3HcmrZakEOE2mZqZ2X+77nXI7357nnes9797LP7p7zPM/7vM/7PPfc9z0H3AAEXINJAedgTMA5+FnAOTgl4Bx8J+AcHBdwDgYEnIP3BZyDQwLGjV63GDlt9AoYHlpo5LRhFzDkhvGVNpoFDLmFfKWNnUFgfA+txf45irLPqtTo4L2KvnsuVY63BCUZ35HTC20a/oK6IDC0gdbiw3xFOfA40VztIp+fFSp6ycfhLI3yMb5c6+s9JOCEDed34asSdMwLKG0Pe2EdjAsqgsChbLryExsV5cgWohlcQz5Pv6ToJR966sv2Nb6HWn9ThmqzxrQ9hK2AcUFJENh2J135pB1rTUSzLhJX9pGbZnMCrnWTW6d0BtFL1st26iyN8jG+XFkSOQI1t6E3E6PNVPl9NZ3UX5zDcgQKg8N4Gy3H5mRyuWM+kX9pJPKZeiLXpxC5LplthG1+BJdr7axca8HvTVRvW6wlZ5dhjQ+WB4fjlexEk0su3y4g8kfPEPmDJ4l8YAWRu3Kpm+Tve3C51ir93gy2rdZoydldWIOD7OBgZ735spJcfl1N5FfTiVyfRuRva4n8RTl168j1I7hca5V+5Ux2T9u05OwurMHBg5oovgtvrcQP2zHWiv+6MdmJc7txdAMqUqjD0+wX8kIb0iMw0UHkR+KIaVns1DbZiYwIMtzhtnqWH7PLtVbpl0RS/dX9WhblLqzBgVUTHg5vLXnEIdWEv9g55cX0qY2wWRl+ZjfRbEmnDpfsuNukZXaVPovdhRdsAS3KCp7AbE2cbEBTPlbMxv0WLJyBvCS8u46uf6yN+nzKnhZOvUI+JQd5uKrrn29yYfIwuzuf2iXs17ta47p4BAk6kWJh+5Cdahrzp/Wp5iHFWdXC15a7MHmYy6XPQgvOshPpc4t1W5fxQUzAJJqRkYwjpewd8SqqXzpnWp/uu0MZomphgdWFycOMzj6xEVgQh4pMnGXPhQPVsJh0WBcvBPSn6sREJ8qzYTJRa1QE0ThMv7V6GtjwqAuT7/M6c6QMFrMnB6/B+fuLDoCbS3P6dVjj/RiYO/XIf9GOpBi1yZfh13twpQujNgzvQl8Jcua5TUxFNMIHxAfMAguKUjG8k1bnaJX3IXIpJfnjF6aeCwtdmHRkaTL+fpNGlmbUN3howSydyEygBZJuKa/Ocp8kOTeJPFlK9U2bqTbpxQOx+LWFhh1phNWsZ/CQg0U6kXM7e7Xd6d1Z7pPj8r1niXx4tQtT4NwTiaGt7OvVjmWJukU2CEjTxEgDbHnklcrDMcgyo3Q+TmynZRrc6H243CfHZUEc/tmHf7vwWLzaFDj9JTTgtW5UpeoW1jggSxPujgl/7MVTiX4MlzWHi8jlsVIXpkBoz1ECdubpE9NoIF8Tzyejvxg/1WPCTnayi2/gx63oK0BhtE/D5bLKmqIYXGonJ8ybTZrZtojk5oj2yXodAhoTPBEK5D45Kw9Mf5sT4BSVCeQ7QY8wL6M4KjQrvQVgTSiQ++SsXB+FP/e4NvlLmRnnG9kLv1ZsigvNMm8NKA9HhqvYf5260DI3PNcog9pwxOvbmXBaLHaEI15bGE6LRZOAc9Au4Bz0CDgH7wg4B/0CzsExAedgUMA5GBJwDk4KOAfnBJyDUQHn4LKAc/4HmrlM+jbmxVYAAAAASUVORK5CYII=',
    headers=self.headers)
        print(login_url)
        # soup = BeautifulSoup(login_url.content, 'html.parser')
        # image_path = soup.findAll('div', {'class': 'captchaimg text-center'})
        # for path in image_path:
        #     print(path.span)

Centralpower().get_pdf()
