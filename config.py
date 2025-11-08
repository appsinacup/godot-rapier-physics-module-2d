def can_build(env, platform):
    # Rapier doesn't support double precision
    if env.get("precision", "single") == "double":
        return False
    return True


def configure(env):
    pass
