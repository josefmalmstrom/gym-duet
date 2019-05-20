# gym-duet
Popular mobile game Duet implemented as an OpenAI-gym environment.

## Installation

Requires Python >=3.5.

First install gym and all its dependencies
```
pip install gym --user
```
Go to the installation path, and add the following lines to the file ```/gym/envs/__init__.py```
```
register(
   	id='Duet-v0',
   	entry_point='gym.envs.duet:DuetGame',
)
```

Download or clone this repo and copy the folder ```duet``` into ```gym/envs```.
