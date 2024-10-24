# Covid Data #
---------------------------
Libraries Used:

* requests: Handles HTTP requests to fetch web content.
* bs4 (BeautifulSoup): Parses HTML data.
* OutputUtil: A custom utility module that contains functions for generating HTML, XML, and other outputs.

Functionality:

* print_html_content(url): Sends an HTTP GET request to the specified URL and prints the raw HTML content.
* parse_html_content(url): Parses the HTML content of a webpage, making it more readable using BeautifulSoup's prettify method.
* next_text(itr): Extracts and returns the next text item from an iterator, stripping any leading or trailing whitespace.
* next_int(itr): Attempts to extract the next integer value from an iterator by parsing text. If parsing fails, it returns 0.

Scraping COVID Data:

* scrape_covid_data():
*Scrapes COVID-19 case data from Worldometer's coronavirus spread page. It pulls data for each country, including its population (retrieved by another function, get_country_population), total cases, deaths, cases per capita, and death percentage.
* Data is stored in a list with rows containing country name, continent, population, cases, deaths, cases per capita, and percentage of deaths.
*Finally, the data is sorted by country name and returned along with column headers.

Scraping Country Populations:

* get_country_population(): Scrapes Worldometer’s population data by country. It builds a dictionary where the key is the country name and the value is the population.

Main Program Execution:

* The main() function orchestrates the process:
* Scrapes the data using scrape_covid_data.
* Uses OutputUtil to generate two outputs:
* An HTML file (Assignment05.html) displaying the data in a styled table with sortable columns.
* An XML file (Assignment05.xml) representing the same data in XML format.
* Both files are opened in the browser upon generation.
