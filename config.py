def can_build(env, platform):
    # Rapier doesn't support double precision
    return env.get("precision", "single") != "double"


def configure(env):
    pass
