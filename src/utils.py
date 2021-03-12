import bs4


def save_file(content, address, mode="w+"):
    with open(address, mode, encoding="utf-8") as file:
        file.write(content)


def remove_scripts(soup):
    for sc in soup.find_all("script"):
        sc.replace_with("")

    return soup


def save_css_as_file(soup, file_address, online_address):
    styles_text = ""

    for se in soup.find_all("style"):
        styles_text += "\n" + se.string
        se.replace_with(
            soup.new_tag("link", attrs={"rel": "stylesheet", "href": online_address})
        )

    save_file(styles_text, file_address)
    return soup


def add_jinja(soup):
    page = str(soup)
    page = page.replace('<html>', '<html>\n<head>')
    page = page.replace('href="kmasi.ir"', 'href="http://kmasi.ir"')
    page = page.replace('<body>', '</head>\n<body>')
    page = page.replace('</body>', '{% block ebody %}{% endblock %}\n</body>')
    page = page.replace('</head>', '{% block ehead %}{% endblock %}\n</head>')
    page = page.replace('<body>', '<body>\n{% block sbody %}{% endblock %}')
    return bs4.BeautifulSoup(page, features="html.parser")
