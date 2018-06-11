# fabsetup-theno-letsencrypt

Create tls-webserver certificates which are trusted by the web pki.

With this [fabsetup](https://github.com/theno/fabsetup) addon
you can install or update [termdown](https://github.com/trehn/termdown),
a _"[c]ountdown timer and stopwatch in your terminal"_.

It installs termdown via `pip install --user termdown`.
Also, it installs a bash-wrapper script at `~/bin/termdown` which
is convenient to time
[pomodoro sessions](https://en.wikipedia.org/wiki/Pomodoro_Technique)
and pops up a notification when the timer finishes:

```bash
termdown 25m
```

Touched files, dirs, and installed packages:

        /etc/letsencrypt/*

## Usage

```bash
# task info
fabsetup -d theno.letsencrypt

# run task
fabsetup theno.letsencrypt
```

## Installation

As a [pypi package](https://pypi.python.org/pypi/fabsetup-theno-letsencrypt)
with command `pip` (recommended way):

```bash
pip install  fabsetup-theno-letsencrypt
```

## Development

https://github.com/theno/fabsetup/blob/master/howtos/fabsetup-addon.md

Devel commands:

```bash
# save changes
git commit -am 'I describe my changes'

# upload to github
git push origin master

# update version number in fabsetup_theno_letsencrypt

# create and publish package at pypi
fab -f fabfile-dev.py  pypi

# clean up
fab -f fabfile-dev.py  clean
```

Clone the [github repository](https://github.com/theno/fabsetup):

```bash
mkdir -p ~/.fabsetup-addon-repos
git clone https://github.com/theno/fabsetup-theno-letsencrypt.git  ~/.fabsetup-addon-repos/fabsetup-theno-letsencrypt

# install fabsetup if not done already
pip install fabsetup

# fabsetup now finds the addon bcause it is located at ~/.fabsetup-addon-repos
fabsetup -d theno.letsencrypt
```

More ways to run the task:

```bash
# you also can run the task directly
cd ~/.fabsetup-addon-repos/fabsetup-theno-letsencrypt
fab -d theno.letsencrypt

# or from a cloned fabsetup repository
git clone https://github.com/theno/fabsetup.git ~/.fabsetup
cd ~/.fabsetup
fab -d theno.letsencrypt

# run directly, fabsetup from cloned repo
cd ~/.fabsetup-addon-repos/fabsetup-theno-letsencrypt
PYTHONPATH=~/.fabsetup fab -d theno.letsencrypt
```
