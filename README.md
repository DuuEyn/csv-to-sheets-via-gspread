<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/DuuEyn/csv-to-sheets-via-gspread">
    <img src="https://lh3.googleusercontent.com/yCF7mTvXRF_EhDf7Kun5_-LMYTbD2IL-stx_D97EzpACfhpGjY_Frx8NZw63rSn2dME0v8-Im49Mh16htvPAGmEOMhiTxDZzo6rB7MY" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">CSV to Sheets</h3>

  <p align="center">
    Converts a CSV file to Google Sheets via gspread.
    <br />
    <br />
    <a href="https://github.com/DuuEyn/csv-to-sheets-via-gspread
">View Repo</a>
    ·
    <a href="https://github.com/DuuEyn/csv-to-sheets-via-gspread
/issues">Report Bug</a>
    ·
    <a href="https://github.com/DuuEyn/csv-to-sheets-via-gspread
/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This script creates a new Google Sheets file from a CSV file, preserving the number of rows and colums the file has, via gspread and Google Sheets API

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python.org]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started



### Prerequisites

* Ensure that you are running `Python 3.8+`
* Install gspread
  ```sh
  pip install gspread
  ```
* Follow gspread's <a href="https://docs.gspread.org/en/v6.0.0/oauth2.html#for-end-users-using-oauth-client-id">instructions</a> on how to authenticate using an OAuth Client ID 

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/DuuEyn/csv-to-sheets-via-gspread
   ```
2. Move `csv_to_sheets.py` and your CSV files to your working directory.
3. Run the function `convert_to_sheets()` for each of the CSV file you would like to convert.
   
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The function `convert_to_sheets()` requires one parameter, the name of the CSV file. If the file is on a separate directory, Make sure to include the file path in your function call. In addition, replace `Your Spreadsheet Name` with your preferred name of the file when calling gspread's `create()` method. You can pass the CSV's filename as well if needed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add some NewFeature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

DuuEyn - iddiche@gmail.com

Project Link: [https://github.com/DuuEyn/csv-to-sheets-via-gspread](https://github.com/DuuEyn/csv-to-sheets-via-gspread)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/DuuEyn/csv-to-sheets-via-gspread.svg?style=for-the-badge
[contributors-url]: https://github.com/DuuEyn/csv-to-sheets-via-gspread/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/DuuEyn/csv-to-sheets-via-gspread.svg?style=for-the-badge
[forks-url]: https://github.com/DuuEyn/csv-to-sheets-via-gspread/network/members
[stars-shield]: https://img.shields.io/github/stars/DuuEyn/csv-to-sheets-via-gspread.svg?style=for-the-badge
[stars-url]: https://github.com/DuuEyn/csv-to-sheets-via-gspread/stargazers
[issues-shield]: https://img.shields.io/github/issues/DuuEyn/csv-to-sheets-via-gspread.svg?style=for-the-badge
[issues-url]: https://github.com/DuuEyn/csv-to-sheets-via-gspread/issues
[license-shield]: https://img.shields.io/github/license/DuuEyn/csv-to-sheets-via-gspread.svg?style=for-the-badge
[license-url]: https://github.com/DuuEyn/csv-to-sheets-via-gspread/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/ian-dewaine-diche-69406a2bb
[Python.org]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
