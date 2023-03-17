<a name="readme-top"></a>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://i.ibb.co/njkqjW7/17984.png" alt="Logo" width="180" height="80">
  </a>

  <h3 align="center">Shopium Scan API</h3>

  <p align="center">
    The Following is a general presentaion of our project 
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</div>

<div>
<br />
<br />
<br />
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<a name="about-the-project"></a>
<!-- ABOUT THE PROJECT -->
## About The Project

* Shopium Scan API is an artificial intelligence module made for **Shopium** to scan users sales receipts for data extraction and classification.


* The data classification of this project is based on pre-defined **Regex** patterns to identify different kinds of data in a raw extracted text.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<a name="built-with"></a>
### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
<br />
<br />
* [Tesseract][Next-url]
* [Flask][React-url]
* [MongoDB][Vue-url]




<p align="right">(<a href="#readme-top">back to top</a>)</p>


<a name="getting-started"></a>
<!-- GETTING STARTED -->
## Getting Started

Before we proceed , this project was designed to run those different tasks :
<br />
1. Receipt's Image URL Reading
2. Image Processing
3. Data Extraction
4. Data Classification
5. Return a well-structured JSON object
<br /><br />

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```sh
   git clone https://github.com/firas122/scan
   ```

2. Install **pip** packages
   ```sh
   pip install -r requirements.txt
   ```

3. Run the API using (the application will be running on localhost ip address using **5000** as port)
   ```js
   python /project_directory_path/scan/api.py
   ```
   

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
<br /><br />
## Usage

* Terminal output will include an url by default **127.0.0.1** (localhost) running on port **5000** using the path **/do**


* Send a ``POST`` request to that url with one variable `url` that represents the receipt image on using the platform you wish to use (`postman` for example) :

<div align="center">
 <br /><br /><br /><br />
<img src="https://i.ibb.co/MkW49Py/Capture1.png" alt="Logo" width="780" height="300">

</div>
<br /><br />

* And the resulting JSON Object should look like this one :
<br /><br />
```sh
  {
    "date": "24/02/2021",
    "name": "Monoprix",
    "products": [
        {
            "pname": "TAMPON EPONGE A RE ",
            "pquantity": 1,
            "ptotal": 1230.0,
            "pupri": 1230.0
        },
        {
            "pname": "YAGURT AU FRUITS F ",
            "pquantity": 2,
            "ptotal": 1440.0,
            "pupri": 720.0
        },
        {
            "pname": "YROURT AU FRUIT CE ",
            "pquantity": 1,
            "ptotal": 720.0,
            "pupri": 720.0
        },
        {
            "pname": "BANANE IMPORTEE. ",
            "pquantity": 1,
            "ptotal": 2090.0,
            "pupri": 2090.0
        }
    ],
    "time": "14:02",
    "total": 5480.0
}
  ```





## Roadmap

- [x] Image Processing
- [x] Data Extraction
- [x] Data classification
- [ ] Multi-Ticket Forms support
- [ ] Design a Machine learning approach


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Shopium - [@Shopium](https://twitter.com/your_username) - shopium.local@gmail.com

Project Link: [https://github.com/firas122/Scan](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
