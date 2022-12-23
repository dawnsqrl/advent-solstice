# Advent Solstice: The vibrant calendar of life

<img src="https://github.com/dawnsqrl/advent-solstice/blob/master/advent_solstice.png">

> 今天是冬至，也刚好是我存在的第8000天<br>
> 事件纯属巧合，但感觉比过生日还要有仪式感。
>
> 这样就产生了一个问题：<br>
> 人到底为什么要根据地球的公转周期来过生日？<br>
> 为什么不能每到下午两点 / 星期四 / 25日 / 地球转两圈 / 800天 / 1000天 / 1111天 / 0x54A天就庆祝一次呢？

Advent Solstice是一个基于Manim Community（[官网](https://www.manim.community)，[GitHub仓库](https://github.com/ManimCommunity/manim)）的自定义日历生成程序，能够以任意周期计算并显示出“生日”所处的位置。日历中的每个方格都代表一个月；时间展示的粒度为1/4个月，通过方格的四个象限体现。

示例图的配色设计参考自[nipponcolors.com](https://nipponcolors.com)。

## 使用方法

1. 将本仓库克隆到本地，通过`pip install -r requirements.txt`安装依赖项。
2. 依照[参数说明](https://github.com/dawnsqrl/advent-solstice/edit/master/README.md#%E5%8F%82%E6%95%B0%E8%AF%B4%E6%98%8E)部分按需调整`advent_solstice.py`脚本末尾的渲染参数。
3. 运行`python advent_solstice.py`生成日历图片文件，默认位于当前目录的`images`文件夹内。

## 参数说明

### Manim渲染参数

能够传入Manim`tempconfig()`函数的所有参数可通过运行`manim cfg show`获取，也可直接参阅[Manim文档页面](https://docs.manim.community/en/stable/guides/configuration.html#a-list-of-all-config-options)。在`advent_solstice.py`中实际进行调整的参数仅占很少一部分，列举解释如下。

| 参数名 | 默认值[^1] | 解释 |
| - | - | - |
| `output_file` | `'advent_solstice'` | 输出文件名。 |
| `verbosity` | `'WARNING'` | 命令行输出日志等级。 |
| `disable_caching` | `True` | 是否关闭渲染过程缓存。 |
| `media_dir` | `'.'` | 输出目录位置。 |
| `background_color` | `'#212121'` | 输出图片背景颜色。 |
| `pixel_width` | `4000` | 输出图片宽（单位：像素）。 |
| `pixel_height` | `1000` | 输出图片高（单位：像素）。 |

### Advent Solstice渲染参数

下列参数应直接传入`AdventSolstice()`构造函数。

| 参数名 | 默认值[^1] | 解释 |
| - | - | - |
| `birthday` | `(2001, 1, 25)` | 生日日期，即日历计算的起始日期。 |
| `events` | `[((2001, 1, 25), ('#72636E', '#D3B7CB')), ...]` | 日历方格的颜色定义，以数组格式按时间顺序列举。定义的格式为`(起始日期, (填充色, 边框色))`，该种颜色会一直延伸至下个定义的起始日期（或今天）。 |
| `epoch_length` | `1e3` | 生日的周期长度（单位：天）。 |
| `epoch_year_length` | `0` | 生日的周期长度（单位：年）。若此值大于零，则会覆盖`epoch_length`中设置的周期值。 |
| `epoch_extension` | `2` | 在今天所处的生日周期之后附加计算的周期数量。 |
| `stroke_width` | `2` | 日历方格的边框宽度。 |
| `stroke_opacity` | `0.6` | 日历方格的边框不透明度。 |
| `none_stroke_color` | `GRAY` | 未填充方格的边框颜色。 |
| `none_stroke_opacity_modifier` | `0.5` | 未填充方格的边框不透明度与已填充方格该值的比例。 |
| `block_opacity` | `0.8` | 日历方格的填充不透明度。 |
| `block_scale` | `0.06` | 日历方格的缩放比例。 |
| `block_buffer_depth` | `0.1` | 日历方格的间距。 |
| `text_font` | [`'Comic Code Ligatures'`](https://tosche.net/fonts/comic-code) | 标题和图例的字体。 |
| `text_color` | `WHITE` | 标题和图例的文字颜色。 |
| `text_opacity` | `0.5` | 标题和图例的文字不透明度。 |
| `text_size` | `16` | 标题和图例的字号。 |
| `text_buffer_depth` | `1` | 标题和图例与日历的间距。 |
| `text_right_buffer_modifier` | `6` | 图例与日历右侧间距的调整比例。对不同宽度的日历和图例文字应作相应调整。 |
| `global_scale` | `0.8` | 整体缩放比例。 |
| `use_hex_day_count` | `False` | 是否使用十六进制显示日期计数。 |
| `is_birthday_marked` | `True` | 是否使用圆点显示现实生日所在的月份和象限。 |
| `do_row_kerning` | `False` | 是否调整每个周期开头的方格填充，使之能够和前一周期的最后一个方格互补。这种效果多数情况下不能自然产生。 |

[^1]: 指在仓库现有`advent_solstice.py`中使用的参数值，用于生成开头部分的示例图。
