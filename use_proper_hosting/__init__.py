import os
import sys

__version__ = "1.0.1"


class PleaseUseProperHosting(Exception):
    def __init__(self, platform: str, username: str = "there", extra_words: str = ""):
        super().__init__(f"Invalid Platform; see below for more information.\n"
                         f"Hey {username}, it seems that you are using {platform} to run this. Unfortunately, this doesn't support {platform}.\n"
                         f"If you can't afford paid hosting platforms and don't know any other hosting platforms, there actually is other great free hostings.\n"
                         f"For example, Oracle Cloud offers always free cloud services, and most services offer at least 1 year free tier services.\n"
                         f"Why not trying to find those?\n{extra_words}")


def detect_repl(safe: bool = False):
    """
    Detects if this platform is Replit.

    :param safe: Whether to just display text. Default False.

    :raises PleaseUseProperHosting: Yes, you are using Replit.
    """
    if [x for x in os.environ if x in ['REPL_SLUG', 'REPL_IMAGE', 'REPL_ID', 'REPL_OWNER', 'REPLIT_DB_URL', 'REPL_LANGUAGE', 'REPL_PUBKEYS']]:
        ex = PleaseUseProperHosting("Replit",
                                    os.environ.get("REPL_OWNER", "there"),
                                    "Oh, and since you are using Replit, if your plan is not hacker or above, using Replit as hosting is against their ToS.")
        if safe:
            return print(str(ex), file=sys.stderr)
        raise ex


if __name__ == "__main__":
    detect_repl()
