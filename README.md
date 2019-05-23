# gym-duet
Popular mobile game Duet by Kumobius, available [here](https://www.duetgame.com/), implemented as an OpenAI-gym environment.
Can be used to train reinforcement learning agents for the game, as done in [Duet DQN](https://github.com/josefmal/duet-DQN).

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

