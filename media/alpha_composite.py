import math

def premultiply(rgb, alpha):
    """预乘 alpha。"""
    raise NotImplementedError("TODO: premultiply")

def composite(fg, bg, alpha):
    """合成。"""
    raise NotImplementedError("TODO: composite")

def blend_space(space):
    """混合色彩空间。"""
    raise NotImplementedError("TODO: blend_space")

def layer_order(order):
    """图层顺序。"""
    raise NotImplementedError("TODO: layer_order")

def clamp_alpha(alpha):
    """alpha 钳制。"""
    raise NotImplementedError("TODO: clamp_alpha")

def intermediate_bits(bits):
    """中间缓冲位深。"""
    raise NotImplementedError("TODO: intermediate_bits")

def feather_scale(resolution, base):
    """羽化分辨率。"""
    raise NotImplementedError("TODO: feather_scale")

def preserve_alpha(alpha):
    """转换保留 alpha。"""
    raise NotImplementedError("TODO: preserve_alpha")

def clear_reused(alpha):
    """复用帧清理。"""
    raise NotImplementedError("TODO: clear_reused")

def rounding(mode):
    """舍入规则。"""
    raise NotImplementedError("TODO: rounding")

def matte_align(pixel):
    """matte 对齐。"""
    raise NotImplementedError("TODO: matte_align")

def composite_over(bg, fg, alpha):
    """over 合成。"""
    raise NotImplementedError("TODO: composite_over")

def alpha_sum(a, b):
    """alpha 累加。"""
    raise NotImplementedError("TODO: alpha_sum")

def sample_weights(t):
    """双线性权重。"""
    raise NotImplementedError("TODO: sample_weights")

def composite_id(seed, index):
    """合成 id。"""
    raise NotImplementedError("TODO: composite_id")
