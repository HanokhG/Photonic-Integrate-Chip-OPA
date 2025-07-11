import gdsfactory as gf
import matplotlib.pyplot as plt
import numpy as np

def create_arc_polygon(
    x_center: float,
    y_center: float,
    inner_radius: float,
    outer_radius: float,
    theta_start: float,
    theta_stop: float,
    num_points: int = 100
):
    theta = np.linspace(np.radians(theta_start), np.radians(theta_stop), num_points)
    outer_x = x_center + outer_radius * np.cos(theta)
    outer_y = x_center + outer_radius * np.sin(theta)
    inner_x = x_center + inner_radius * np.cos(theta[::-1])
    inner_y = x_center + inner_radius * np.sin(theta[::-1])
    vertices = list(zip(outer_x, outer_y)) + list(zip(inner_x, inner_y))
    return vertices

@gf.cell
def custom_bend1(
    radius=30,
    angle_start=0,
    angle_stop=90,
    width=0.6,
    layer=(2, 0),
    cross_section="strip"
):
    c = gf.Component()
    inner_radius = radius - width / 2
    outer_radius = radius + width / 2

    vertices = create_arc_polygon(
        x_center=0,
        y_center=0,
        inner_radius=inner_radius,
        outer_radius=outer_radius,
        theta_start=angle_start,
        theta_stop=angle_stop
    )
    c.add_polygon(vertices, layer=layer)

    mid_radius = (inner_radius + outer_radius) / 2
    start_x = mid_radius * np.cos(np.radians(angle_start))
    start_y = mid_radius * np.sin(np.radians(angle_start))
    end_x = mid_radius * np.cos(np.radians(angle_stop))
    end_y = mid_radius * np.sin(np.radians(angle_stop))

    input_port = gf.Port(
        name="o1",
        center=(start_x, start_y),
        orientation=(angle_start + 180) % 360,
        width=width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o1", port=input_port)

    output_port = gf.Port(
        name="o2",
        center=(end_x, end_y),
        orientation=-angle_stop,
        width=width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o2", port=output_port)

    return c

def custom_bend2(
    radius=30,
    angle_start=0,
    angle_stop=90,
    width=0.6,
    layer=(2, 0),
    cross_section="strip"
):
    c = gf.Component()
    inner_radius = radius - width / 2
    outer_radius = radius + width / 2

    vertices = create_arc_polygon(
        x_center=0,
        y_center=0,
        inner_radius=inner_radius,
        outer_radius=outer_radius,
        theta_start=angle_start,
        theta_stop=angle_stop
    )
    c.add_polygon(vertices, layer=layer)

    mid_radius = (inner_radius + outer_radius) / 2
    start_x = mid_radius * np.cos(np.radians(angle_start))
    start_y = mid_radius * np.sin(np.radians(angle_start))
    end_x = mid_radius * np.cos(np.radians(angle_stop))
    end_y = mid_radius * np.sin(np.radians(angle_stop))

    input_port = gf.Port(
        name="o1",
        center=(start_x, start_y),
        orientation=(angle_start + 180) % 360,
        width=width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o1", port=input_port)

    output_port = gf.Port(
        name="o2",
        center=(end_x, end_y),
        orientation=angle_stop,
        width=width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o2", port=output_port)

    return c

def custom_bend3(
    radius=30,
    angle_start=0,
    angle_stop=90,
    width=0.6,
    layer=(2, 0),
    cross_section="strip"
):
    c = gf.Component()
    inner_radius = radius - width / 2
    outer_radius = radius + width / 2

    vertices = create_arc_polygon(
        x_center=0,
        y_center=0,
        inner_radius=inner_radius,
        outer_radius=outer_radius,
        theta_start=angle_start,
        theta_stop=angle_stop
    )
    c.add_polygon(vertices, layer=layer)

    mid_radius = (inner_radius + outer_radius) / 2
    start_x = mid_radius * np.cos(np.radians(angle_start))
    start_y = mid_radius * np.sin(np.radians(angle_start))
    end_x = mid_radius * np.cos(np.radians(angle_stop))
    end_y = mid_radius * np.sin(np.radians(angle_stop))

    input_port = gf.Port(
        name="o1",
        center=(start_x, start_y),
        orientation=(angle_start + 180) % 360,
        width=width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o1", port=input_port)

    output_port = gf.Port(
        name="o2",
        center=(end_x, end_y),
        orientation=angle_stop,
        width=width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o2", port=output_port)

    return c
def custom_bend4(
    radius=30,
    angle_start=0,
    angle_stop=90,
    width=0.6,
    layer=(2, 0),
    cross_section="strip"
):
    c = gf.Component()
    inner_radius = radius - width / 2
    outer_radius = radius + width / 2

    vertices = create_arc_polygon(
        x_center=0,
        y_center=0,
        inner_radius=inner_radius,
        outer_radius=outer_radius,
        theta_start=angle_start,
        theta_stop=angle_stop
    )
    c.add_polygon(vertices, layer=layer)

    mid_radius = (inner_radius + outer_radius) / 2
    start_x = mid_radius * np.cos(np.radians(angle_start))
    start_y = mid_radius * np.sin(np.radians(angle_start))
    end_x = mid_radius * np.cos(np.radians(angle_stop))
    end_y = mid_radius * np.sin(np.radians(angle_stop))

    input_port = gf.Port(
        name="o1",
        center=(start_x, start_y),
        orientation=(angle_start + 180) % 360,
        width=width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o1", port=input_port)

    output_port = gf.Port(
        name="o2",
        center=(end_x, end_y),
        orientation=angle_stop,
        width=width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o2", port=output_port)

    return c
def custom_bend(
    radius: float = 30,
    angle_start: float = 0,
    angle_stop: float = 90,
    width: float = 0.6,
    layer=(2, 0),
    cross_section="strip",
    # 下列两个可选参数，用于灵活微调输入、输出端口的朝向
    orientation_in_offset: float = 180,
    orientation_out_offset: float = 0,
    num_points: int = 100
):

    c = gf.Component()

    # 计算内外半径
    inner_radius = radius - width / 2
    outer_radius = radius + width / 2

    # 生成波导弧形区域的多边形
    vertices = create_arc_polygon(
        x_center=0,
        y_center=0,
        inner_radius=inner_radius,
        outer_radius=outer_radius,
        theta_start=angle_start,
        theta_stop=angle_stop,
        num_points=num_points
    )
    c.add_polygon(vertices, layer=layer)

    # 计算弧形起止端的中线坐标
    mid_radius = 0.5 * (inner_radius + outer_radius)

    start_x = mid_radius * np.cos(np.radians(angle_start))
    start_y = mid_radius * np.sin(np.radians(angle_start))
    end_x   = mid_radius * np.cos(np.radians(angle_stop))
    end_y   = mid_radius * np.sin(np.radians(angle_stop))

    # 根据 offset 计算端口朝向
    orientation_in  = (angle_start + orientation_in_offset) % 360
    orientation_out = (angle_stop + orientation_out_offset) % 360

    # 输入端口
    input_port = gf.Port(
        name="o1",
        center=(start_x, start_y),
        orientation=orientation_in,
        width=width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o1", port=input_port)

    # 输出端口
    output_port = gf.Port(
        name="o2",
        center=(end_x, end_y),
        orientation=orientation_out,
        width=width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o2", port=output_port)

    return c
def custom_straight(
    length: float = 20.0,
    width: float = 0.6,
    layer=(2, 0),
    cross_section: str = "strip",
    orientation_in: float = 180,
    orientation_out: float = 180
):
    """
    通用直波导。
    参数:
        length           : 波导长度 (y方向尺寸)
        width            : 波导宽度 (x方向)
        layer            : (layer, datatype)
        cross_section    : gdsfactory的端口剖面类型
        orientation_in   : 输入端口方向(度)
        orientation_out  : 输出端口方向(度)

    注意:
      如果想复用 "原先" 的 3 个 straight:
        - custom_straight1 相当于 custom_straight(..., orientation_in=180, orientation_out=180)
        - custom_straight2 相当于 custom_straight(..., orientation_in=0,   orientation_out=0)
        - custom_straight3 相当于 custom_straight(..., orientation_in=180, orientation_out=0)
    """
    c = gf.Component()

    # 构建矩形多边形 [(-w/2,0), (w/2,0), (w/2,length), (-w/2,length)]
    rect = gf.kdb.DPolygon([
        (-width / 2, 0),
        ( width / 2, 0),
        ( width / 2, length),
        (-width / 2, length)
    ])
    c.add_polygon(rect, layer=layer)

    # 输入端口
    input_port = gf.Port(
        name="o1",
        center=(0, 0),
        orientation=orientation_in,     # 可以灵活设定
        width=width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o1", port=input_port)

    # 输出端口
    output_port = gf.Port(
        name="o2",
        center=(0, length),
        orientation=orientation_out,    # 可以灵活设定
        width=width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o2", port=output_port)

    return c
@gf.cell
def custom_mmi(
    width_rect=1.87689,
    length_rect=2.67444,
    space=1.03561,
    layer_main=(2, 0),
    port_width=0.6,
    in_taper_L=1.30647,
    cross_section="strip"
):
    c = gf.Component()
    left_rect = gf.kdb.DPolygon([(-50, 0.3), (-in_taper_L, 0.3), (-in_taper_L, -0.3), (-50, -0.3)])
    left_tape = gf.kdb.DPolygon([
        (-in_taper_L, 0.3),
        (0, width_rect / 2),
        (0, -width_rect / 2),
        (-in_taper_L, -0.3)
    ])
    mid_rect = gf.kdb.DPolygon([
        (0, width_rect / 2),
        (0, -width_rect / 2),
        (length_rect, -width_rect / 2),
        (length_rect, width_rect / 2)
    ])
    right_tape1 = gf.kdb.DPolygon([
        (length_rect, space / 2 + 0.35),
        (length_rect, space / 2 - 0.35),
        (length_rect + 0.925, space / 2 - 0.3),
        (length_rect + 0.925, space / 2 + 0.3)
    ])
    right_tape2 = gf.kdb.DPolygon([
        (length_rect, space / 2 + 0.35),
        (length_rect, space / 2 - 0.35),
        (length_rect + 0.925, space / 2 - 0.3),
        (length_rect + 0.925, space / 2 + 0.3)
    ])
    right_tape2.move((0, -space))

    c.add_polygon(left_rect, layer=layer_main)
    c.add_polygon(left_tape, layer=layer_main)
    c.add_polygon(mid_rect, layer=layer_main)
    c.add_polygon(right_tape1, layer=layer_main)
    c.add_polygon(right_tape2, layer=layer_main)

    input_port = gf.Port(
        name="o1",
        center=(-50, 0),
        orientation=90,
        width=port_width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o1", port=input_port)

    output_port_top = gf.Port(
        name="o2",
        center=(length_rect + 0.925, space / 2),
        orientation=-90,
        width=port_width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o2", port=output_port_top)

    output_port_bottom = gf.Port(
        name="o3",
        center=(length_rect + 0.925, -space / 2),
        orientation=90,
        width=port_width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o3", port=output_port_bottom)

    return c

@gf.cell
def custom_straight1(
    length=20.0,
    width=0.6,
    layer=(2, 0),
    cross_section="strip"
):
    c = gf.Component()
    rect = gf.kdb.DPolygon([
        (-width / 2, 0),
        (width / 2, 0),
        (width / 2, length),
        (-width / 2, length)
    ])
    c.add_polygon(rect, layer=layer)

    input_port = gf.Port(
        name="o1",
        center=(0, 0),
        orientation=180,
        width=width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o1", port=input_port)

    output_port = gf.Port(
        name="o2",
        center=(0, length),
        orientation=180,
        width=width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o2", port=output_port)

    return c

def custom_straight2(
    length=20.0,
    width=0.6,
    layer=(2, 0),
    cross_section="strip"
):
    c = gf.Component()
    rect = gf.kdb.DPolygon([
        (-width / 2, 0),
        (width / 2, 0),
        (width / 2, length),
        (-width / 2, length)
    ])
    c.add_polygon(rect, layer=layer)

    input_port = gf.Port(
        name="o1",
        center=(0, 0),
        orientation=0,
        width=width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o1", port=input_port)

    output_port = gf.Port(
        name="o2",
        center=(0, length),
        orientation=0,
        width=width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o2", port=output_port)

    return c
def custom_straight3(
    length=50.0,
    width=0.6,
    layer=(2, 0),
    cross_section="strip"
):
    c = gf.Component()
    rect = gf.kdb.DPolygon([
        (-width / 2, 0),
        (width / 2, 0),
        (width / 2, length),
        (-width / 2, length)
    ])
    c.add_polygon(rect, layer=layer)

    input_port = gf.Port(
        name="o1",
        center=(0, 0),
        orientation=180,
        width=width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o1", port=input_port)

    output_port = gf.Port(
        name="o2",
        center=(0, length),
        orientation=0,
        width=width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o2", port=output_port)

    return c

@gf.cell
def build_single_mmi_with_bends(straight_length=30.0):
    c = gf.Component()

    # Create the MMI
    mmi = c << custom_mmi()

    # Add bends for the output ports
    bend_out1 = c << custom_bend3(radius=30, angle_start=-90, angle_stop=0, width=0.6)
    bend_out1.connect("o1", mmi.ports["o2"])

    bend_out2 = c << custom_bend4(radius=30, angle_start=90, angle_stop=0, width=0.6)
    bend_out2.connect("o1", mmi.ports["o3"])

    # Create a straight segment with variable length
    straight1 = c << custom_straight1(length=straight_length, width=0.6)
    straight1.connect("o1", bend_out1.ports["o2"])

    straight2 = c << custom_straight2(length=straight_length, width=0.6)
    straight2.connect("o1", bend_out2.ports["o2"])

    bend_out11 = c << custom_bend1(radius=30, angle_start=0, angle_stop=-90, width=0.6)
    bend_out11.connect("o1", straight1.ports["o2"])

    bend_out22 = c << custom_bend2(radius=30, angle_start=-90, angle_stop=0, width=0.6)
    bend_out22.connect("o1", straight2.ports["o2"])

    # Add ports to the component
    c.add_port("input", port=mmi.ports["o1"])
    c.add_port("output1", port=bend_out11.ports["o2"])
    c.add_port("output2", port=bend_out22.ports["o2"])

    return c
def build_single_mmi_with_bends2(straight_length=30.0):
    c = gf.Component()

    # Create the MMI
    mmi = c << custom_mmi()

    # Add bends for the output ports
    bend_out1 = c << custom_bend3(radius=30, angle_start=-90, angle_stop=-30, width=0.6)
    bend_out1.connect("o1", mmi.ports["o2"])

    bend_out2 = c << custom_bend4(radius=30, angle_start=90, angle_stop=30, width=0.6)
    bend_out2.connect("o1", mmi.ports["o3"])

    # Create a straight segment with variable length
    straight1 = c << custom_straight1(length=straight_length, width=0.6)
    straight1.connect("o1", bend_out1.ports["o2"])

    straight2 = c << custom_straight2(length=straight_length, width=0.6)
    straight2.connect("o1", bend_out2.ports["o2"])

    bend_out11 = c << custom_bend(radius=30, angle_start=60, angle_stop=0, width=0.6,orientation_out_offset=180)
    bend_out11.connect("o1", straight1.ports["o2"])

    bend_out22 = c << custom_bend(radius=30, angle_start=30, angle_stop=90, width=0.6)
    bend_out22.connect("o1", straight2.ports["o2"])

    # Add ports to the component
    c.add_port("input", port=mmi.ports["o1"])
    c.add_port("output1", port=bend_out11.ports["o2"])
    c.add_port("output2", port=bend_out22.ports["o2"])

    return c


def inverse_taper(output_width=0.1, input_width=0.6, taper_length=300.0, input_straight_length=10.0, output_straight_length=10.0, layer=(2, 0), cross_section="strip"):
    c = gf.Component()

    # Add a straight section before the taper
    input_straight_section = [
        (taper_length / 2, -input_width / 2),
        (taper_length / 2 + input_straight_length, -input_width / 2),
        (taper_length / 2 + input_straight_length, input_width / 2),
        (taper_length / 2, input_width / 2)
    ]
    c.add_polygon(input_straight_section, layer=layer)

    # Add the taper
    taper_vertices = [
        (-taper_length / 2, -output_width / 2),
        (taper_length / 2, -input_width / 2),
        (taper_length / 2, input_width / 2),
        (-taper_length / 2, output_width / 2)
    ]
    c.add_polygon(taper_vertices, layer=layer)

    # Add a straight section after the taper
    output_straight_section = [
        (-taper_length / 2 - output_straight_length, -output_width / 2),
        (-taper_length / 2, -output_width / 2),
        (-taper_length / 2, output_width / 2),
        (-taper_length / 2 - output_straight_length, output_width / 2)
    ]
    c.add_polygon(output_straight_section, layer=layer)
    trapezoid_vertices = [
        (-taper_length / 2 - output_straight_length - 10, -20 / 2),  # Bottom left
        (-taper_length / 2 - output_straight_length, -output_width / 2),  # Top left
        (-taper_length / 2 - output_straight_length, output_width / 2),  # Top right
        (-taper_length / 2 - output_straight_length - 10, 20 / 2)  # Bottom right
    ]
    c.add_polygon(trapezoid_vertices, layer=layer)
    # Add ports
    c.add_port("input", center=(taper_length / 2 + input_straight_length, 0), orientation=-90, cross_section=cross_section, width=input_width)
    c.add_port("output", center=(-taper_length / 2 - output_straight_length, 0), orientation=90, cross_section=cross_section, width=output_width)

    return c

def create_mmi_network(top, straight_lengths, final_spacing=160.0, bend_radius=30.0, output_width=0.1, taper_input_offset=(-500, 3000)):
    num_layers = len(straight_lengths)  # Total number of layers

    # Create the first inverse taper and position it
    taper_input = top << inverse_taper(output_width=output_width, input_width=0.6, taper_length=300.0,
                                       input_straight_length=100.0, output_straight_length=150)
    taper_input.dmove(taper_input_offset)

    mmi10 = top << build_single_mmi_with_bends2(straight_length=0)
    mmi10.connect("input", taper_input.ports["input"])
    taper_output = top << inverse_taper(output_width=output_width, input_width=0.6, taper_length=300.0,
                                       input_straight_length=8000.0, output_straight_length=150)
    taper_output.connect("input", mmi10.ports["output1"])
    straight1 = top << custom_straight(length=4000.0, width=0.6, orientation_out=0)
    straight1.connect("o1", mmi10.ports["output2"])

    bend1 = top << custom_bend(radius=bend_radius, angle_start=0, orientation_in_offset=0,
                               angle_stop=-90, width=0.6, orientation_out_offset=180)
    bend1.connect("o1", straight1.ports["o2"])

    # ---------- Start of fanout tree after bend1 ----------
    mmi_list = []

    # First MMI in tree after bend1
    mmi_root = top << build_single_mmi_with_bends(straight_length=straight_lengths[0])
    mmi_root.connect("input", bend1.ports["o2"])
    mmi_list.append((mmi_root, 0))  # Initial Y-position is 0

    # Build fanout tree from level 1 to num_layers - 1
    for level in range(1, num_layers):
        new_mmi_list = []
        current_spacing = final_spacing * (2 ** (num_layers - level - 1))

        for mmi, y_position in mmi_list:
            # Add short straight waveguides
            straight1 = top << custom_straight3(length=50.0, width=0.6)
            straight2 = top << custom_straight3(length=50.0, width=0.6)

            # Decide which MMI to use
            if level == num_layers - 1:
                mmi_builder = build_single_mmi_with_bends2
            else:
                mmi_builder = build_single_mmi_with_bends

            mmi_out1 = top << mmi_builder(straight_length=straight_lengths[level])
            mmi_out2 = top << mmi_builder(straight_length=straight_lengths[level])

            # Y positions
            new_y1 = y_position - current_spacing / 4
            new_y2 = y_position + current_spacing / 4

            # Connect straight waveguides
            straight1.connect("o1", mmi.ports["output1"])
            straight2.connect("o1", mmi.ports["output2"])

            # Connect new MMIs
            mmi_out1.connect("input", straight1.ports["o2"])
            mmi_out2.connect("input", straight2.ports["o2"])

            new_mmi_list.append((mmi_out1, new_y1))
            new_mmi_list.append((mmi_out2, new_y2))

        mmi_list = new_mmi_list

    # ---------- Add delay lines ----------
    delay_step = 56.436
    delay_offset = 20.0
    total_pre_post_length = 5000.0
    index = 0

    for mmi, _ in mmi_list:
        for port_name in ["output1", "output2"]:
            straight1_length = 100 + index * 65.0
            straight3_length = total_pre_post_length - straight1_length
            delay_length = delay_offset + index * delay_step

            straight1 = top << custom_straight3(length=straight1_length, width=0.6)
            bend1 = top << custom_bend(radius=bend_radius, angle_start=0, angle_stop=90, width=0.6)
            delay_line = top << custom_straight(length=delay_length, width=0.6)
            bend2 = top << custom_bend(radius=bend_radius, angle_start=0, angle_stop=-90, width=0.6, orientation_out_offset=180)
            straight3 = top << custom_straight(length=straight3_length, width=0.6)

            straight1.connect("o1", mmi.ports[port_name])
            bend1.connect("o1", straight1.ports["o2"])
            delay_line.connect("o1", bend1.ports["o2"])
            bend2.connect("o1", delay_line.ports["o2"])
            straight3.connect("o1", bend2.ports["o2"])

            index += 1

def mark(offsetx=0,offsety=150):
    c = gf.Component()
    straight1 = c << custom_straight(length= 300.0,  width= 5)
    straight2 = c << custom_straight(length=5, width=300)
    straight2.dmove((offsetx,offsety))
    straight1.dmove((offsetx, offsety-150))

    return c

if __name__ == "__main__":
    top = gf.Component()

    # Define straight lengths for two layers
    straight_lengths = [916.058, 427.77, 183.626,61.554, 0.518, 0]
    background_vertices = [
        (-7500, -10000),
        (7500, -10000),
        (7500, 10000),
        (-7500, 10000)
    ]
    top.add_polygon(background_vertices, layer=(1, 0))
    # Create the MMI network 4 times
    offsets = [(-4000, 3000)]
    for offset in offsets:
        create_mmi_network(top, straight_lengths, taper_input_offset=offset,output_width=0.2)

    mark1 = top << mark(offsetx=-5000,offsety=-3500)
    mark2 = top << mark(offsetx=-5050,offsety=3500)
    mark3 = top << mark(offsetx=6000,offsety=-3500)
    mark4 = top << mark(offsetx=6000,offsety=3500)


    # Export the GDS file
    top.write_gds("YNmmi10.gds")
    top.plot()
    plt.show()

