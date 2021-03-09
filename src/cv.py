import os
import typer
import requests
import jinja2

from bs4 import BeautifulSoup
import utils

app = typer.Typer()


@app.command()
def gist():
    typer.echo(os.popen("gh gist edit b14877578266205717bbb9820b4ad63f").read())


@app.command()
def update_base():
    soup = BeautifulSoup(
        requests.get("https://registry.jsonresume.org/danialkeimasi").text,
        features="html.parser",
    )
    soup = utils.remove_scripts(soup)
    soup = utils.save_css_as_file(soup, "../docs/styles.css", "styles.css")
    soup = utils.add_jinja(soup)
    utils.save_file(str(soup.prettify()), "templates/auto/base.html")


@app.command()
def export():
    template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="./templates"))
    template = template_env.get_template("index.html")
    rendered_template = template.render()
    utils.save_file(rendered_template, "../docs/index.html")


if __name__ == "__main__":
    app()
