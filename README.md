### People

People resource management

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
<summary>Server</summary>

Start the server:

```sh
(venv) python manage.py runserver
```

Open [127.0.0.1:8000](http://127.0.0.1:8000/).

</details>

#### Debug

To debug its recommended to use the [VSCode](https://code.visualstudio.com/) [debug tool](https://code.visualstudio.com/docs/editor/debugging), that provide debug for Python and for Django.

#### Credits

Developed by [Sphinxs](https://github.com/Sphinxs).