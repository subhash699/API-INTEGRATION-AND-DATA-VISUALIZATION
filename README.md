# API-INTEGRATION-AND-DATA-VISUALIZATION

COMPANY: CODTECH IT SOLUCTIONS

NAME: SUBHASH K

INTERN ID: CT04DG769

DOMAIN: PYTHON PROGRAMMING

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH



As part of my internship at CodTech IT Solutions Pvt. Ltd., Task 1 focused on integrating a public API with Python and creating meaningful data visualizations. The goal of this task was to use Python to fetch real-time weather data from the OpenWeatherMap API and visualize the information using matplotlib and seaborn libraries. This exercise allowed me to work on a practical use case that combined API handling, data processing, and graphical representation. Such skills are highly valuable in data analytics and real-time reporting applications.

To begin with, I selected the OpenWeatherMap API, a widely used free API that provides current weather data for cities across the globe. I registered on the official OpenWeatherMap website to obtain a free API key, which is necessary to access the API endpoints. The API provides a wealth of weather-related data, including temperature, humidity, wind speed, pressure, and more. For this task, I focused on two primary parameters—temperature (in degrees Celsius) and humidity (in percentage)—as they are straightforward and useful for visualization purposes.

The development environment I used was Python 3.12.2 along with the IDLE Shell. I installed the required Python libraries using pip, specifically requests for fetching API data, pandas for handling data structures, and matplotlib and seaborn for creating visualizations. The script started by defining a list of major Indian cities, such as Delhi, Mumbai, Chennai, Bengaluru, Hyderabad, Kolkata, Ahmedabad, and Pune. These cities were chosen to demonstrate the capability of fetching and comparing weather data across different geographical regions.

Using a `for` loop, the script iterated through each city in the list and sent a request to the OpenWeatherMap API using the requests module. The response, which was in JSON format, was parsed to extract relevant data like the current temperature and humidity. This information was stored in a list of dictionaries, with each dictionary representing one city’s weather data. After collecting the data for all cities, the list was converted into a pandas DataFrame for better structure and easy manipulation.

For the visualization part, I used seaborn to create a bar chart showing the current temperature for each city. The bar chart provided a clear comparison of how temperature varied across different cities. The chart was color-coded using the 'coolwarm' palette to enhance readability. I also created a line chart using seaborn to depict humidity levels for each city. The line chart helped visualize the trend in humidity across regions, with markers and a green line for clarity. Both charts were displayed using matplotlib’s `plt.show()` function and could be saved as image files using `plt.savefig()` if needed.

This task had multiple real-world applications. For example, such scripts can be integrated into weather monitoring dashboards, used by travel agencies, agriculture platforms, or mobile applications providing localized weather updates. It also highlighted the importance of automation in real-time data collection and presentation. Learning how to work with APIs, handle JSON responses, and transform the data into visual insights added valuable experience to my programming and data analysis skills.

In conclusion, Task 1 gave me hands-on experience in API integration and data visualization, two essential areas in modern software development and data science. I learned how to communicate with web-based APIs, extract useful information, process it into structured formats, and present it visually in a way that is informative and accessible. The task strengthened my understanding of Python's ecosystem and its practical use in solving real-time problems.

OUTPUT:

![Image](https://github.com/user-attachments/assets/b22c2631-a133-4154-908f-686f4fe7e242)
![Image](https://github.com/user-attachments/assets/96daa874-85ab-4fb8-b750-6981fdd48752)
