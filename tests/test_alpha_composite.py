import pytest
from media import alpha_composite as mod

CASES = [
    ("pre", 'm.premultiply((1, 2, 3), 0.5) == (0.5, 1.0, 1.5)'),
    ("comp", 'm.composite((1, 1, 1), (0, 0, 0), 0.5) == approx((0.5, 0.5, 0.5))'),
    ("space", 'm.blend_space("linear") is True'),
    ("order", 'm.layer_order([3, 1, 2]) == [3, 1, 2]'),
    ("clamp", 'm.clamp_alpha(2) == 1.0'),
    ("bits", 'm.intermediate_bits(8) == 16'),
    ("feather", 'm.feather_scale(4, 2) == 2.0'),
    ("alpha", 'm.preserve_alpha(0.5) == 0.5'),
    ("clear", 'm.clear_reused(0.7) == 0.0'),
    ("round", 'm.rounding("round_half_even") is True'),
    ("matte", 'm.matte_align(2) == 2.5'),
    ("over", 'm.composite_over(0.2, 0.8, 0.5) == approx(0.5)'),
    ("sum", 'm.alpha_sum(0.5, 0.7) == 1.0'),
    ("weights", 'm.sample_weights(0.25) == approx((0.75, 0.25))'),
    ("id", 'm.composite_id(3, 2) == "3:2"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
