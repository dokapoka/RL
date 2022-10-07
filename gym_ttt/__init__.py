from gym.envs.registration import register

register(
    id='ttt-v1',
    entry_point='gym_ttt.envs:TTTEnv',
)
