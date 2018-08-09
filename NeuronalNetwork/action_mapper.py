ACTION_SIZE = 5


def map_action(action):
    if action == 0:
        angular = 2.0
        linear = 0.5
    elif action == 1:
        angular = 1.0
        linear = 0.75
    elif action == 2:
        angular = 0.0
        linear = 1.0
    elif action == 3:
        angular = -1.0
        linear = 0.75
    elif action == 4:
        angular = -2.0
        linear = 0.5
    else:
        raise AttributeError("Invalid Action: {}".format(action))

    return linear, angular
