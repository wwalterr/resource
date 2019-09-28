### People

🤬 People resource management

---

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d2b2f710258f42bb949c3b0b01d3d247)](https://www.codacy.com/manual/Sphinxs/People?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Sphinxs/People&amp;utm_campaign=Badge_Grade) ![GitHub commit activity](https://img.shields.io/github/commit-activity/w/sphinxs/people) [![Maintainability](https://api.codeclimate.com/v1/badges/c99faed633623f244c61/maintainability)](https://codeclimate.com/github/Sphinxs/People/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/c99faed633623f244c61/test_coverage)](https://codeclimate.com/github/Sphinxs/People/test_coverage)

---

#### Setup

<details>
<summary>Python</summary>

Add the PPA:

```sh
$ sudo add-apt-repository ppa:deadsnakes/ppa
```

Update the source list:

```sh
$ apt update
```

Install the Python 3.7:

```sh
$ sudo apt install python3.7
```

</details>

<details>
<summary>Venv</summary>

Install the Python 3.7 Venv:

```sh
$ apt install python3.7-venv
```

Create the virtual environment:

```sh
$ python3.7 -m venv venv
```

Activate the virtual environment:

```sh
$ source ./venv/bin/activate
```

Deactivate the virtual environment:

```sh
$ deactivate
```

</details>

<details>
<summary>SQLite 3</summary>

Install the SQLite 3:

```sh
$ sudo apt install libsqlite3-dev
```

**Obs**: To explore the database its recommended to install the [SQLite Browser](https://sqlitebrowser.org)

</details>

<details>
<summary>Python Dependencies</summary>

Update the virtual enrivonment Pip:

```sh
(venv) pip install --upgrade pip
```

Inside the virtual enrivonment install the dependencies:

```sh
(venv) pip install -r requirements.txt
```

</details>

#### Run

<details>
<summary>Database</summary>

Here we use SQLite 3, i.e, its not necessary to configure third party softwares like MySQL, PostgreSQL, etc.

Make the migrations:

```sh
(venv) python manage.py makemigrations
```

Migrate:

```sh
(venv) python manage.py migrate
```

</details>

<details>
<summary>User</summary>

Create an super user to access the [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) painel:

```sh
(venv) python manage.py createsuperuser
```

</details>

<details>
<summary>Static</summary>

Generate the static files:

```sh
(venv) python manage.py collectstatic
```

</details>

<details>
<summary>Server</summary>

Start the server:

```sh
(venv) python manage.py runserver
```

Open [127.0.0.1:8000](http://127.0.0.1:8000/).

</details>

#### Structure

The project structure generated through `tree -L 1` can be found bellow:

<details>
<summary>Tree</summary>

├── application          # Application
├── collections          # Application requests
├── manage.py            # Django shortcut
├── people               # Project
├── README.md            # Documentation
└── requirements.txt     # Dependencies

</details>

#### Debug

<details>
<summary>Editor</summary>

To debug its recommended to use the [VSCode](https://code.visualstudio.com/) [debug tool](https://code.visualstudio.com/docs/editor/debugging), that provide debug for Python and for Django.

</details>

<details>
<summary>Insomnia</summary>

Its also recommended to debug via the browsable API or through requests to the API, via the available [collections](./collections/insomnia.json), that can be opened through [Insomnia](https://insomnia.rest/), [Postman](https://www.getpostman.com/) or another HTTP client.

</details>

#### Deploy

The application can be found here on [Heroku](https://people-django.herokuapp.com/) and the tutorial to make the deploy can be found here on [Code Mentor](https://www.codementor.io/jamesezechukwu/how-to-deploy-django-app-on-heroku-dtsee04d4).

#### Credits

Developed by [Sphinxs](https://github.com/Sphinxs).