import math
import random

import pytest

from notebook_loader import last_notebook

oppgave = last_notebook("oppgave")


@pytest.fixture(autouse=True)
def fast_seed():
    # Gjør simuleringene like fra kjøring til kjøring
    random.seed(2025)


def test_anslag_pi():
    assert abs(oppgave.anslag_pi(200_000) - math.pi) <= 0.02


def test_anslag_pi_er_tilfeldig():
    random.seed(1)
    a = oppgave.anslag_pi(1000)
    random.seed(2)
    b = oppgave.anslag_pi(1000)
    assert a != b, "anslag_pi skal bruke tilfeldige tall"


@pytest.mark.parametrize("personer,fasit", [(10, 0.117), (23, 0.507), (50, 0.970)])
def test_felles_bursdag(personer, fasit):
    assert abs(oppgave.felles_bursdag(personer, 20_000) - fasit) <= 0.02


@pytest.mark.parametrize("bytte,fasit", [(True, 2 / 3), (False, 1 / 3)])
def test_monty_hall(bytte, fasit):
    assert abs(oppgave.monty_hall(bytte, 20_000) - fasit) <= 0.02
