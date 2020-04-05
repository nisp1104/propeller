from __future__ import absolute_import

import os

import pytest

from . import ilm_util

@pytest.fixture
def ilm_daemon():
    """
    Run ILM daemon during a test.
    """
    p = ilm_util.start_daemon()
    try:
        ilm_util.wait_for_daemon(0.5)
        yield
    finally:
        # Killing sanlock allows terminating without reomving the lockspace,
        # which takes about 3 seconds, slowing down the tests.
        p.kill()
        p.wait()