import os
import typer
import requests
import bs4

import utils

app = typer.Typer()


@app.command()
def update():
    typer.echo(os.popen("gh gist edit b14877578266205717bbb9820b4ad63f").read())


@app.command()
def export():
    soup = bs4.BeautifulSoup(
        requests.get("https://registry.jsonresume.org/danialkeimasi").text,
        features="html.parser",
    )
    soup = utils.remove_scripts(soup)
    soup = utils.save_css_as_file(soup, "export/styles.css", "/styles.css")
    utils.save_file(str(soup.prettify()), "export/index.html")


if __name__ == "__main__":
    app()