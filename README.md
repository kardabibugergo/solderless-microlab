# FTVC Solderless Microlab

An open source jacketed lab reactor made from off-the-shelf components you can buy online.

Read the motivation behind the project here: [docs/motivation.md](docs/motivation.md)

## Setup

Clone the repo:

```text
$ git clone https://github.com/FourThievesVinegar/solderless-microlab.git
$ cd solderless-microlab
```

### API Server

#### Install dependencies:

##### Python

(for Debian / Ubuntu)

```text
$ sudo apt update
$ sudo apt install python3 python3-pip python-virtualenv python3-virtualenv
```

(for macOS)

```text
$ brew update
$ brew install python3
$ pip3 install virtualenv
```

Set up a Python virtual environment:

```text
$ cd backend
$ virtualenv -p python3 env
$ source env/bin/activate
(env) $ pip install -r requirements.txt
```

##### Redis

(on the Pi)

```text
sudo apt -y install screen git redis-server python-celery-common python3-flask python3-pip python3-rpi.gpio python3-serial

```

(for Debian / Ubuntu)

```text
sudo apt update
sudo apt install redis-server
```

To run Resis as a service,

```text
sudo nano /etc/redis/redis.conf
```

and change the option for `supervised` from `no` to `systemd`

#### Start the server:

```text
(env) $ python main.py
```

### Web GUI

#### Install dependencies:

(for Debian / Ubuntu)

Follow a guide to install yarn for Debian:

https://classic.yarnpkg.com/en/docs/install/#debian-stable

In summary:

```text
$ curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
$ echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
$ sudo apt update
$ sudo apt install yarn
```

(for macOS)

```text
$ brew update
$ brew install yarn
```

#### Run the GUI:

```text
$ cd gui
$ yarn install
$ yarn start
```

The GUI will now be listening on port 3000.

## Hardware Emulation

To run the software without a functioning hardware environment, set the following configs:

In `/solderless-microlab/backend/config.py`:

```
celeryMode = 'test'
```

## API Spec

API spec is very flexible and will change as development goes on.

### Hardware Tests

#### GET /test/relays

Test the relay shield. All four relays are turned on and off.
