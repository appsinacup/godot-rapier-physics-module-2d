def can_build(env, platform):
    # Rapier doesn't support double precision
    if env.get("precision", "single") == "double":
        return False
    # Right now Rapier is disabled on web
    if platform == "web":
        return False
    return True


def configure(env):
    pass
