# python_mobile_app

This project will demonstrate how to use kivy to develop a cross platform mobile app written in Python.

# Motivation

It's something to do I guess.

# Demo

![App Screens](/demo_anim/python_mob_app_demo.gif)

# Pre-requisites

This project uses **Pipenv** for the sandboxed virtual environment, so you will need to install this prior to modifying this project. See the installation steps here:

```http
https://pipenv-fork.readthedocs.io/en/latest/install.html#installing-pipenv
```

# Python Installation

A note on the Python version. For the purposes of this project I have used Kivy. Kivy currently *does not* support Python version 3.8. For that reason please do not attempt to modofy this project with **Python version 3.8.x** as it won't work. If you already have python 3.8.x installed, don't fret. You can install **Pyenv** and use multiple versions of Python on your machine. See how to install and use Pyenv here:

```http
https://github.com/pyenv/pyenv
```

# Libraries/Technologies Used

* [Kivy](https://kivy.org/#home)
Used to build the mobile application user interface (cross plaform mobile application development library).
* [Invoke](http://www.pyinvoke.org/)
Used to run and define repetitive tasks.


# Setup Project (use for modification of the app only)

Pipenv install -r requirements.txt
kivy.angle is not required for mac os . Install ffpyplayer
See install step help here:
https://kivy.org/doc/stable/installation/installation-osx.html

Once garden in installed then instal some widgets with garden.

garden install --kivy iconfonts -> install the package (inconfonts) inside the kivy installation.

# Run the app locally

On te terminal input:

```console
$ python main.py --size=320x646 --dpi=96
```

Which will start the application with that given window size and dots per inch.

# Deploy to iPhone

TODO

# Deploy to Android

TODO


#