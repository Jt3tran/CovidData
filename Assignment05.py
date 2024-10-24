import requests
from bs4 import BeautifulSoup
import OutputUtil as ou


# Define a function to print the HTML content of a webpage at a given URL (uniform resource locator, web address)
def print_html_content(url):
    response = requests.get(url)
    print(response.content)


# Define a function to parse the HTML content for a given URL.
def parse_html_content(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup.prettify())


# Define a function to get the next text item from an iterator
def next_text(itr):
    return next(itr).text.strip()


# Define a function to get the next int item from an iterator
def next_int(itr):
    try:
        return int(next_text(itr).replace(',', ''))
    except ValueError:
        return 0


# Define a function to scrape the site.
def scrape_covid_data():
    dict_country_population = get_country_population()
    url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    data = []
    data_iterator = iter(soup.find_all('td'))
    while True:
        try:
            country = next_text(data_iterator)
            if country.startswith('Japan'):
                country = 'Japan'
            cases = next_int(data_iterator)
            deaths = next_int(data_iterator)
            continent = next_text(data_iterator)
            if country in dict_country_population:
                population = dict_country_population[country]
                population = int(population.replace(',', ''))
                cases_per_capita = round(cases / population, 2)
                percent_deaths = round((deaths / cases) * 100, 2)
                data.append([country, continent, population, cases, deaths, cases_per_capita, percent_deaths])
            else:
                print(f"Country {country} not found in population data")

        except StopIteration:
            break

    headers = ['Country', 'Continent', 'Population', 'Cases', 'Deaths', 'Cases Per Capita', 'Percent Deaths']
    data.sort(key=lambda row: row[0])

    return headers, data


# Define a function get_country_population(url) that will scrape this website to get country populations.
def get_country_population():
    dict_country_population = {}
    url = 'https://www.worldometers.info/world-population/population-by-country/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    data_iterator = iter(soup.find_all('td'))
    while True:
        try:
            next(data_iterator)  # Skip the first junk element
            country = next_text(data_iterator)
            population = next_text(data_iterator)
            dict_country_population[country] = population
            for _ in range(7):  # Skip the remaining junk elements
                next(data_iterator)

        except StopIteration:
            break

    return dict_country_population


def main():
    headers, data = scrape_covid_data()
    title = "Covid Data By Country"
    types = ["S", "S", "N", "N", "N", "N", "N"]
    alignments = ["L", "L", "L", "R", "R", "R", "R"]

    # Write HTML file
    ou.write_html_file("Assignment05.html", title, headers, types, alignments, data, True)

    # Write XML file
    ou.write_xml_file('Assignment05.xml', title, headers, types, data, do_open=True)


if __name__ == "__main__":
    main()
