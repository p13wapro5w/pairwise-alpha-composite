# pairwise-alpha-composite

字幕边缘出现一圈黑边，非预乘 alpha 直接做双线性，透明像素的 RGB 被背景色污染；合成公式里背景项写反，叠上去反而变暗；在 sRGB 空间做 alpha 混合，半透明区域亮度塌陷；多轨道 blend mode 按图层数组顺序执行，正片叠底和滤色互相覆盖；alpha 累加后没 clamp，多次叠加溢出成白块；8bit 中间缓冲每层量化一次，十层后出现色带；遮罩羽化在低分辨率做，放大后边缘锯齿；色彩空间转换丢掉了 alpha 通道，抠像边缘变实心；缓存帧复用时没清 alpha，上一帧的残影叠进来；GPU 与 CPU 合成 rounding 规则不同，预览和导出差一档；rotoscope matte 收缩了一像素，人物边缘吃进背景。media/alpha_composite.py 是核心，tests/test_alpha_composite.py 15个红。要修的是：统一预乘 alpha；合成公式按预乘展开；线性空间混合；blend 顺序按图层栈；alpha 钳制；中间缓冲升到 16bit；羽化在高分辨率做；转换保留 alpha；复用帧清 alpha；统一 rounding；matte 按半像素对齐。

## 运行

```bash
python -m pytest tests -q
```

初始状态：15 个用例失败。修复实现使全部用例通过，不要修改 `tests/` 下的测试。

子方向：见平台；任务类型：Bugfix；语言/框架：Python 3, pytest；环境可复现等级：无外部依赖。
