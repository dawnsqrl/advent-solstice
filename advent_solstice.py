from manim import *
from datetime import date, timedelta
from math import ceil
import numpy as np


def parse_date(time: tuple[int, int, int]) -> date:
    return date(time[0], time[1], time[2])


def get_quarter(month: int, day: int) -> int:
    if month < 1 or month > 12 or day < 1:
        return 0
    month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return (4 if day > month_length[month - 1]
            else ceil(4 * day / month_length[month - 1]))


def advance_month(time: date) -> date:
    return date(time.year, time.month + 1, 1) if time.month < 12 \
        else date(time.year + 1, 1, 1)


class AdventSolstice(Scene):
    def __init__(self, options: dict):
        super().__init__()
        self.today = date.today()
        self.birthday = parse_date(options['birthday'])
        self.events = []
        for event in options['events']:
            self.events.append((
                date(event[0][0], event[0][1], get_quarter(event[0][1], event[0][2])),
                event[1]
            ))
        self.epoch_length = options['epoch_length']
        self.epoch_year_length = options['epoch_year_length']
        self.epoch_extension = options['epoch_extension']
        self.stroke_width = options['stroke_width']
        self.stroke_opacity = options['stroke_opacity']
        self.none_stroke_color = options['none_stroke_color']
        self.none_stroke_opacity = self.stroke_opacity * options['none_stroke_opacity_modifier']
        self.block_opacity = options['block_opacity']
        self.block_scale = options['block_scale']
        self.block_buffer_depth = options['block_buffer_depth']
        self.text_font = options['text_font']
        self.text_color = options['text_color']
        self.text_opacity = options['text_opacity']
        self.text_size = options['text_size']
        self.text_buffer_depth = options['text_buffer_depth']
        self.text_right_buffer_modifier = options['text_right_buffer_modifier']
        self.global_scale = options['global_scale']
        self.use_hex_day_count = options['use_hex_day_count']
        self.is_birthday_marked = options['is_birthday_marked']
        self.do_row_kerning = options['do_row_kerning']
        self.max_row_length = -1

    def draw_block(self, q1: tuple[str, str] | None, q2: tuple[str, str] | None,
                   q3: tuple[str, str] | None, q4: tuple[str, str] | None,
                   is_birthday_marked) -> VGroup:
        this_block = VGroup()
        block_width = 2
        marker_radius = block_width / 4
        if q1 is not None:
            this_block.add(Square(block_width, fill_color=q1[0], fill_opacity=self.block_opacity,
                                  stroke_opacity=0).shift(np.array([-1, 1, 0])))
            this_block.add(Elbow(block_width, angle=PI / 2, stroke_width=self.stroke_width,
                                 stroke_color=q1[1], stroke_opacity=self.stroke_opacity))
            if q2 is None:
                this_block.add(Elbow(block_width, angle=PI, stroke_width=self.stroke_width,
                                     stroke_color=q1[1], stroke_opacity=self.stroke_opacity)
                               .shift(np.array([0, 2, 0])))
            if q3 is None:
                this_block.add(Elbow(block_width, angle=0, stroke_width=self.stroke_width,
                                     stroke_color=q1[1], stroke_opacity=self.stroke_opacity)
                               .shift(np.array([-2, 0, 0])))
        else:
            this_block.add(Elbow(block_width, angle=PI / 2, stroke_width=self.stroke_width,
                                 stroke_color=self.none_stroke_color,
                                 stroke_opacity=self.none_stroke_opacity))
        if q2 is not None:
            this_block.add(Square(block_width, fill_color=q2[0], fill_opacity=self.block_opacity,
                                  stroke_opacity=0).shift(np.array([-1, -1, 0])))
            this_block.add(Elbow(block_width, angle=PI, stroke_width=self.stroke_width,
                                 stroke_color=q2[1], stroke_opacity=self.stroke_opacity))
            if q1 is None:
                this_block.add(Elbow(block_width, angle=PI / 2, stroke_width=self.stroke_width,
                                     stroke_color=q2[1], stroke_opacity=self.stroke_opacity)
                               .shift(np.array([0, -2, 0])))
            if q4 is None:
                this_block.add(Elbow(block_width, angle=-PI / 2, stroke_width=self.stroke_width,
                                     stroke_color=q2[1], stroke_opacity=self.stroke_opacity)
                               .shift(np.array([-2, 0, 0])))
        else:
            this_block.add(Elbow(block_width, angle=PI, stroke_width=self.stroke_width,
                                 stroke_color=self.none_stroke_color,
                                 stroke_opacity=self.none_stroke_opacity))
        if q3 is not None:
            this_block.add(Square(block_width, fill_color=q3[0], fill_opacity=self.block_opacity,
                                  stroke_opacity=0).shift(np.array([1, 1, 0])))
            this_block.add(Elbow(block_width, angle=0, stroke_width=self.stroke_width,
                                 stroke_color=q3[1], stroke_opacity=self.stroke_opacity))
            if q1 is None:
                this_block.add(Elbow(block_width, angle=PI / 2, stroke_width=self.stroke_width,
                                     stroke_color=q3[1], stroke_opacity=self.stroke_opacity)
                               .shift(np.array([2, 0, 0])))
            if q4 is None:
                this_block.add(Elbow(block_width, angle=-PI / 2, stroke_width=self.stroke_width,
                                     stroke_color=q3[1], stroke_opacity=self.stroke_opacity)
                               .shift(np.array([0, 2, 0])))
        else:
            this_block.add(Elbow(block_width, angle=0, stroke_width=self.stroke_width,
                                 stroke_color=self.none_stroke_color,
                                 stroke_opacity=self.none_stroke_opacity))
        if q4 is not None:
            this_block.add(Square(block_width, fill_color=q4[0], fill_opacity=self.block_opacity,
                                  stroke_opacity=0).shift(np.array([1, -1, 0])))
            this_block.add(Elbow(block_width, angle=-PI / 2, stroke_width=self.stroke_width,
                                 stroke_color=q4[1], stroke_opacity=self.stroke_opacity))
            if q2 is None:
                this_block.add(Elbow(block_width, angle=PI, stroke_width=self.stroke_width,
                                     stroke_color=q4[1], stroke_opacity=self.stroke_opacity)
                               .shift(np.array([2, 0, 0])))
            if q3 is None:
                this_block.add(Elbow(block_width, angle=0, stroke_width=self.stroke_width,
                                     stroke_color=q4[1], stroke_opacity=self.stroke_opacity)
                               .shift(np.array([0, -2, 0])))
        else:
            this_block.add(Elbow(block_width, angle=-PI / 2, stroke_width=self.stroke_width,
                                 stroke_color=self.none_stroke_color,
                                 stroke_opacity=self.none_stroke_opacity))
        if self.is_birthday_marked and is_birthday_marked:
            birthday_quarter = get_quarter(self.birthday.month, self.birthday.day)
            if birthday_quarter == 1:
                if q1 is not None:
                    this_block.add(Circle(marker_radius, stroke_width=0, fill_color=q1[1],
                                          fill_opacity=self.stroke_opacity)
                                   .shift(np.array([-1, 1, 0])))
                else:
                    this_block.add(Circle(marker_radius, stroke_width=0, fill_color=self.none_stroke_color,
                                          fill_opacity=self.none_stroke_opacity)
                                   .shift(np.array([-1, 1, 0])))
            elif birthday_quarter == 2:
                if q2 is not None:
                    this_block.add(Circle(marker_radius, stroke_width=0, fill_color=q2[1],
                                          fill_opacity=self.stroke_opacity)
                                   .shift(np.array([-1, -1, 0])))
                else:
                    this_block.add(Circle(marker_radius, stroke_width=0, fill_color=self.none_stroke_color,
                                          fill_opacity=self.none_stroke_opacity)
                                   .shift(np.array([-1, -1, 0])))
            elif birthday_quarter == 3:
                if q3 is not None:
                    this_block.add(Circle(marker_radius, stroke_width=0, fill_color=q3[1],
                                          fill_opacity=self.stroke_opacity)
                                   .shift(np.array([1, 1, 0])))
                else:
                    this_block.add(Circle(marker_radius, stroke_width=0, fill_color=self.none_stroke_color,
                                          fill_opacity=self.none_stroke_opacity)
                                   .shift(np.array([1, 1, 0])))
            elif birthday_quarter == 4:
                if q4 is not None:
                    this_block.add(Circle(marker_radius, stroke_width=0, fill_color=q4[1],
                                          fill_opacity=self.stroke_opacity)
                                   .shift(np.array([1, -1, 0])))

                else:
                    this_block.add(Circle(marker_radius, stroke_width=0, fill_color=self.none_stroke_color,
                                          fill_opacity=self.none_stroke_opacity)
                                   .shift(np.array([1, -1, 0])))
        return this_block.scale(self.block_scale)

    def get_quarter_color(self, quarter_time: date) -> tuple[str, str] | None:
        for index in range(len(self.events) - 1):
            if self.events[index][0] <= quarter_time < self.events[index + 1][0]:
                return self.events[index][1]
        today_quarter_time = date(self.today.year, self.today.month,
                                  get_quarter(self.today.month, self.today.day))
        if self.events[-1][0] <= quarter_time <= today_quarter_time:
            return self.events[-1][1]
        return None

    def calendar_row(self, start_time: date, end_time: date, is_first_row: bool) -> VGroup:
        this_row = VGroup()
        start_quarter = 0 if start_time > self.today \
            else get_quarter(start_time.month, start_time.day)
        if not is_first_row and self.do_row_kerning:
            start_quarter += 1
        q1 = self.get_quarter_color(date(start_time.year, start_time.month, 1))
        q2 = self.get_quarter_color(date(start_time.year, start_time.month, 2))
        q3 = self.get_quarter_color(date(start_time.year, start_time.month, 3))
        q4 = self.get_quarter_color(date(start_time.year, start_time.month, 4))
        if start_quarter == 1:
            last_block = self.draw_block(q1, q2, q3, q4, start_time.month == self.birthday.month)
        elif start_quarter == 2:
            last_block = self.draw_block(None, q2, q3, q4, start_time.month == self.birthday.month)
        elif start_quarter == 3:
            last_block = self.draw_block(None, None, q3, q4, start_time.month == self.birthday.month)
        elif start_quarter == 4:
            last_block = self.draw_block(None, None, None, q4, start_time.month == self.birthday.month)
        else:
            last_block = self.draw_block(None, None, None, None, start_time.month == self.birthday.month)
        this_row.add(last_block)
        current_time = advance_month(start_time)
        while current_time.year < end_time.year or (current_time.year == end_time.year
                                                    and current_time.month < end_time.month):
            last_block = self.draw_block(
                self.get_quarter_color(date(current_time.year, current_time.month, 1)),
                self.get_quarter_color(date(current_time.year, current_time.month, 2)),
                self.get_quarter_color(date(current_time.year, current_time.month, 3)),
                self.get_quarter_color(date(current_time.year, current_time.month, 4)),
                current_time.month == self.birthday.month
            ).next_to(last_block, RIGHT, buff=self.block_buffer_depth)
            this_row.add(last_block)
            current_time = advance_month(current_time)
        end_quarter = get_quarter(end_time.month, end_time.day)
        q1 = self.get_quarter_color(date(end_time.year, end_time.month, 1))
        q2 = self.get_quarter_color(date(end_time.year, end_time.month, 2))
        q3 = self.get_quarter_color(date(end_time.year, end_time.month, 3))
        q4 = self.get_quarter_color(date(end_time.year, end_time.month, 4))
        if end_quarter == 1:
            last_block = self.draw_block(q1, None, None, None, end_time.month == self.birthday.month) \
                .next_to(last_block, RIGHT, buff=self.block_buffer_depth)
        elif end_quarter == 2:
            last_block = self.draw_block(q1, q2, None, None, end_time.month == self.birthday.month) \
                .next_to(last_block, RIGHT, buff=self.block_buffer_depth)
        elif end_quarter == 3:
            last_block = self.draw_block(q1, q2, q3, None, end_time.month == self.birthday.month) \
                .next_to(last_block, RIGHT, buff=self.block_buffer_depth)
        elif end_quarter == 4:
            last_block = self.draw_block(q1, q2, q3, q4, end_time.month == self.birthday.month) \
                .next_to(last_block, RIGHT, buff=self.block_buffer_depth)
        else:
            last_block = self.draw_block(None, None, None, None, end_time.month == self.birthday.month)
        this_row.add(last_block)
        return this_row

    def construct(self):
        if self.epoch_year_length > 0:
            row_count = self.epoch_extension
            current_time = self.birthday
            while current_time < self.today:
                row_count += 1
                current_time = date(current_time.year + self.epoch_year_length,
                                    current_time.month, current_time.day)
        else:
            duration_day = (self.today - self.birthday).days
            duration_epoch = ceil(duration_day / self.epoch_length)
            row_count = duration_epoch + self.epoch_extension
        calendar = VGroup()
        last_row = None
        epoch_start_times = []
        epoch_end_times = []
        legend_epoch_start = VGroup()
        legend_epoch_end = VGroup()
        for this_epoch in range(0, row_count):
            if self.epoch_year_length > 0:
                this_epoch_start_time = self.birthday if this_epoch == 0 \
                    else date(self.birthday.year + this_epoch * self.epoch_year_length,
                              self.birthday.month, self.birthday.day) + timedelta(days=1)
                this_epoch_end_time = date(self.birthday.year + (this_epoch + 1) * self.epoch_year_length,
                                           self.birthday.month, self.birthday.day)
            else:
                this_epoch_start_time = self.birthday if this_epoch == 0 \
                    else self.birthday + timedelta(days=this_epoch * self.epoch_length + 1)
                this_epoch_end_time = self.birthday + timedelta(days=(this_epoch + 1) * self.epoch_length)
            epoch_start_times.append(this_epoch_start_time)
            epoch_end_times.append(this_epoch_end_time)
            if last_row is None:
                last_row = self.calendar_row(this_epoch_start_time, this_epoch_end_time, True)
            else:
                last_row = self.calendar_row(this_epoch_start_time, this_epoch_end_time, False) \
                    .next_to(last_row, DOWN, self.block_buffer_depth, aligned_edge=LEFT)
            calendar.add(last_row)
            if len(last_row.submobjects) > self.max_row_length:
                self.max_row_length = len(last_row.submobjects)
        for row_index in range(row_count):
            this_row = calendar.submobjects[row_index]
            while len(this_row.submobjects) < self.max_row_length:
                this_row.add(self.draw_block(None, None, None, None, False).set_opacity(0)
                             .next_to(this_row.submobjects[-1], RIGHT, buff=self.block_buffer_depth))
            legend_epoch_start.add(
                Text(str(epoch_start_times[row_index]).replace('-', '.'),
                     font=self.text_font, font_size=self.text_size,
                     fill_color=self.text_color, fill_opacity=self.text_opacity)
                .next_to(this_row, LEFT, self.text_buffer_depth, aligned_edge=LEFT)
            )
            day_count = (epoch_end_times[row_index] - self.birthday).days
            if self.use_hex_day_count:
                day_count = hex(day_count)
            legend_epoch_end.add(
                Text(str(epoch_end_times[row_index]).replace('-', '.') +
                     f' \u2192 {day_count} days', font=self.text_font, font_size=self.text_size,
                     fill_color=self.text_color, fill_opacity=self.text_opacity)
                .next_to(this_row, RIGHT, self.text_buffer_depth * self.text_right_buffer_modifier,
                         aligned_edge=LEFT)
            )
        legend_title = VGroup(
            Text('today is ' + str(self.today).replace('-', '.'),
                 font=self.text_font, font_size=self.text_size,
                 fill_color=self.text_color, fill_opacity=self.text_opacity / 2)
            .next_to(calendar, UP, self.text_buffer_depth / 6, aligned_edge=LEFT),
            Text(f'day {(self.today - self.birthday).days} of existence',
                 font=self.text_font, font_size=self.text_size,
                 fill_color=self.text_color, fill_opacity=self.text_opacity / 2)
            .next_to(calendar, DOWN if self.epoch_length < 540 or self.epoch_year_length == 1 else UP,
                     self.text_buffer_depth / 6, aligned_edge=RIGHT)
        )
        advent_solstice = VGroup(calendar, legend_epoch_start, legend_epoch_end, legend_title)
        self.add(advent_solstice.scale(self.global_scale).move_to(ORIGIN))


if __name__ == '__main__':
    with tempconfig({
        "output_file": "advent_solstice",
        "verbosity": "WARNING",
        "disable_caching": True,
        "media_dir": ".",
        "background_color": "#212121",
        "pixel_width": 4000,
        "pixel_height": 1000
    }):
        scene = AdventSolstice({
            'birthday': (2001, 1, 25),
            'events': [
                ((2001, 1, 25), ('#72636E', '#D3B7CB')),
                ((2004, 9, 1), ('#5E3D50', '#BF7CA2')),
                ((2007, 9, 1), ('#516E41', '#98CF7A')),
                ((2009, 9, 8), ('#939650', '#F2F784')),
                ((2013, 9, 1), ('#867835', '#E7CF5B')),
                ((2015, 2, 15), ('#904940', '#F1786B')),
                ((2016, 9, 1), ('#4F726C', '#92D3C8')),
                ((2018, 7, 31), ('#434343', '#A4A4A4')),
                ((2019, 9, 7), ('#376B6D', '#68CACE')),
                ((2021, 8, 31), ('#577C8A', '#94D3EB'))
            ],
            'epoch_length': 1e3,
            'epoch_year_length': 0,
            'epoch_extension': 2,
            'stroke_width': 2,
            'stroke_opacity': 0.6,
            'none_stroke_color': GRAY,
            'none_stroke_opacity_modifier': 0.5,
            'block_opacity': 0.8,
            'block_scale': 0.06,
            'block_buffer_depth': 0.1,
            'text_font': 'Comic Code Ligatures',
            'text_color': WHITE,
            'text_opacity': 0.5,
            'text_size': 16,
            'text_buffer_depth': 1,
            'text_right_buffer_modifier': 6,
            'global_scale': 0.8,
            'use_hex_day_count': False,
            'is_birthday_marked': True,
            'do_row_kerning': False
        })
        scene.render()
