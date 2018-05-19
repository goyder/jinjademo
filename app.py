import pandas as pd
import os
from bs4 import BeautifulSoup

from flask import Flask, render_template

app = Flask(__name__)


def csv_to_html(csv_filepath):
    """
    Read in a .csv file.
    Return an HTML representation.
    :param csv_filepath: Filepath to a .csv file to be displayed.
    :return: HTML representation of table to be inserted into block.
    """
    # Read in CSV file
    df_csvfile = pd.read_csv(
        csv_filepath,
    )

    # Convert to html
    html_csvfile = df_csvfile.to_html(
        escape=False,
        table_id="table",
        index=False,
        index_names=False,
    )

    # Add a tag for the bootstrapping
    soup = BeautifulSoup(html_csvfile)
    soup.find(id="table")['data-toggle'] = "table"
    soup.find(id="table")['data-pagination'] = "true"
    soup.find(id="table")['data-search'] = "true"

    # Return as CSV file
    return soup


def generate_csv_block(csv_filepath, title, comments):
    """
    Accept a pathway to a .csv fileway, and return an HTML representation to be plotted.
    :param csv_filepath: Filepath to a .csv file to be displayed.
    :param title: Title of HTML block.
    :param comments: Comments to be included under the title.
    :return: HTML block to be inserted into main page.
    """
    html_table = csv_to_html(csv_filepath)
    return render_template(
        "csv_section_block.html",
        title=title,
        comments=comments,
        table=html_table
    )


@app.route('/')
def hello_world():
    # Container object to hold any components that we might want to distribute.
    html_blocks = list()

    # Populate with content
    html_blocks.append(generate_csv_block(
        csv_filepath=os.path.join("static", "bike_costs.csv"),
        title="Costs through Europe",
        comments="Costs of activities throughout a bike trip of Europe."
    ))

    return render_template(
        "base.html",
        blocks=html_blocks
    )


if __name__ == '__main__':
    app.run()
