<div id="top"></div>

[![LinkedIn][linkedin-shield]][linkedin-url]
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GNU v3 License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/estebanvz/eta-lib/">
    <img src="https://avatars.githubusercontent.com/u/65377832?s=400&u=12c57a2350bcd69068ced71f630ca0d5559e6621&v=4)}" alt="Logo" width="80" height="80" style="border-radius:100%">
  </a>

  <h3 align="center"> eta-lib - A pandas based Technical Analysis Library
</h3>

  <p align="center">
    Python Package forked from bta-lib and based on pandas.
    <br />
    <!-- <a href="https://github.com/estebanvz/eta-lib"><strong>Explore the docs »</strong></a>
    <br /> -->
    <br />
    <a href="https://github.com/estebanvz/eta-lib/">View Test</a>
    ·
    <a href="https://github.com/estebanvz/eta-lib/issues">Report Bug</a>
    ·
    <a href="https://github.com/estebanvz/eta-lib/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS
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
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details> -->



<!-- ABOUT THE PROJECT -->
## About The Package

This is a package that fix some compatibility problems presented on bta-lib with the new version of numpy and pandas.

``bta-lib`` is ``pandas`` based technical analysis library and part of the
``backtrader`` family.

Author of bta-lib: **Daniel Rodriguez**
Original github: [https://github.com/mementum/bta-lib](https://github.com/mementum/bta-lib)
<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

This project was builded with the next technologies.

* [Python](https://python.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started


<!-- ### Prerequisites

You need the next components to run this project.
* Docker. To install it follow these steps [Click](https://docs.docker.com/get-docker/). 
  On Ubuntu, you can run:
```sh
sudo apt-get install docker-ce docker-ce-cli containerd.io
```
* Visual Studio Code. To install it follow these steps [Click](https://code.visualstudio.com/download). On Ubuntu, you can run:
```sh
sudo snap install code --classic
```
* Install the visual studio code extension "Remote - Containers" -->
### Building

Follow the next steps:

1. Setup the project:
   ```python
   python setup.py sdist
   ```
2. Build the package:
   ```python
   python setup.py build
   ```
3. Install the package
   ```python
   python setup.py install
   ```
4. Install the package using pip.
    ```bash
    pip install eta-lib
    ```
<p align="right">(<a href="#top">back to top</a>)</p>

### Intalling

Just need to use pip with git command:
```python
pip install git+https://github.com/estebanvz/eta-lib.git
```

### Usage

Get the keys from API Binance:

[GET BINANCE API KEYS](https://www.binance.com/en/support/faq/360002502072)

You can use the package using the **api_key** and **api_secret** from binance API.
Also you could download the package **crypo_price** to download data from Binance API.
[Crypto Price Package](https://github.com/estebanvz/crypto_price)
```python
import os
from decouple import config
from crypto_price import CryptoDataExtractor
from eta-lib import CryptoDataTransformation
API_KEY = config("API_KEY")
API_SECRET = config("API_SECRET")
extractor = CryptoDataExtractor()
extractor.from_binance(api_key=API_KEY,api_secret=API_SECRET,time_in_hours=24*10)
transformer = CryptoDataTransformation()
transformer.readDataset()

```

<!-- USAGE EXAMPLES
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
<!-- ## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/estebanvz/eta-lib/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p> -->

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

## bta-lib Links

  - Main Page: https://btalib.backtrader.com/
  - Documentation: https://btalib.backtrader.com/introduction/
  - Community: https://community.backtrader.com/category/10/bta-lib
  - GitHub Repo: https://github.com/mementum/bta-lib

<!-- CONTACT -->
## Contact

Esteban Vilca - [@ds_estebanvz](https://twitter.com/ds_estebanvz) - [esteban.wilfredo.g@gmail.com](mailto:esteban.wilfredo.g@gmail.com)

Project Link: [https://github.com/estebanvz/eta-lib](https://github.com/estebanvz/eta-lib)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/estebanvz/eta-lib.svg
[contributors-url]: https://github.com/estebanvz/eta-lib/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/estebanvz/eta-lib.svg
[forks-url]: https://github.com/estebanvz/eta-lib/network/members
[stars-shield]: https://img.shields.io/github/stars/estebanvz/eta-lib.svg
[stars-url]: https://github.com/estebanvz/eta-lib/stargazers
[issues-shield]: https://img.shields.io/github/issues/estebanvz/eta-lib.svg
[issues-url]: https://github.com/estebanvz/eta-lib/issues
[license-shield]: https://img.shields.io/github/license/estebanvz/eta-lib.svg
[license-url]: https://github.com/estebanvz/eta-lib/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?=linkedin&colorB=888
[linkedin-url]: https://linkedin.com/in/estebanvz
[product-screenshot]: images/screenshot.png