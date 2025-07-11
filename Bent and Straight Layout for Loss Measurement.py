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
    radius=20,
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
    radius=20,
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
    radius=20,
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
    radius=20,
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

def custom_bend5(
    radius=20,
    angle_start=0,
    angle_stop=0,
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
        orientation=0,
        width=width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o1", port=input_port)

    output_port = gf.Port(
        name="o2",
        center=(end_x, end_y),
        orientation=90,
        width=width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o2", port=output_port)

    return c
def custom_bend6(
    radius=20,
    angle_start=0,
    angle_stop=0,
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
        orientation=0,
        width=width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o1", port=input_port)

    output_port = gf.Port(
        name="o2",
        center=(end_x, end_y),
        orientation=180,
        width=width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o2", port=output_port)

    return c
@gf.cell
def custom_mmi(
    width_rect=1.8,
    length_rect=3.4,
    space=1,
    layer_main=(2, 0),
    port_width=0.6,
    cross_section="strip"
):
    c = gf.Component()
    left_rect = gf.kdb.DPolygon([(-50, 0.3), (-1.3, 0.3), (-1.3, -0.3), (-50, -0.3)])
    left_tape = gf.kdb.DPolygon([
        (-1.3, 0.3),
        (0, width_rect / 2),
        (0, -width_rect / 2),
        (-1.3, -0.3)
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
        (length_rect + 0.625, space / 2 - 0.3),
        (length_rect + 0.625, space / 2 + 0.3)
    ])
    right_tape2 = gf.kdb.DPolygon([
        (length_rect, space / 2 + 0.35),
        (length_rect, space / 2 - 0.35),
        (length_rect + 0.625, space / 2 - 0.3),
        (length_rect + 0.625, space / 2 + 0.3)
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
        center=(length_rect + 0.625, space / 2),
        orientation=-90,
        width=port_width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o2", port=output_port_top)

    output_port_bottom = gf.Port(
        name="o3",
        center=(length_rect + 0.625, -space / 2),
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

def custom_straight4(
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
    bend_out1 = c << custom_bend3(radius=20, angle_start=-90, angle_stop=0, width=0.6)
    bend_out1.connect("o1", mmi.ports["o2"])

    bend_out2 = c << custom_bend4(radius=20, angle_start=90, angle_stop=0, width=0.6)
    bend_out2.connect("o1", mmi.ports["o3"])

    # Create a straight segment with variable length
    straight1 = c << custom_straight1(length=straight_length, width=0.6)
    straight1.connect("o1", bend_out1.ports["o2"])

    straight2 = c << custom_straight2(length=straight_length, width=0.6)
    straight2.connect("o1", bend_out2.ports["o2"])

    bend_out11 = c << custom_bend1(radius=20, angle_start=0, angle_stop=-90, width=0.6)
    bend_out11.connect("o1", straight1.ports["o2"])

    bend_out22 = c << custom_bend2(radius=20, angle_start=-90, angle_stop=0, width=0.6)
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
    # Add port
    c.add_port("input", center=(taper_length / 2 + input_straight_length, 0), orientation=-90, cross_section=cross_section, width=input_width)
    c.add_port("output", center=(-taper_length / 2 - output_straight_length, 0), orientation=90, cross_section=cross_section, width=output_width)
    taper_input_offset = (-500, 3000)
    return c
def taper(top, bend_radius=20, taper_input_offset=(-500, 3000),output_width=0.1,output_l=150):

    # Create the first inverse taper and position it
    taper_input = top << inverse_taper(output_width=output_width, input_width=0.6, taper_length=300.0,
                                       input_straight_length=2000.0, output_straight_length=output_l)
    taper_input.dmove(taper_input_offset)  # Move taper_input to specified offset

    # Add a reverse inverse taper to the output of bend2
    reverse_taper = top << inverse_taper(output_width=output_width, input_width=0.6, taper_length=300.0,
                                         input_straight_length=2000.0, output_straight_length=output_l)
    reverse_taper.connect("input", taper_input.ports["input"])

def create_bend_6(top, bend_radius=30, taper_input_offset=(-500, 3000),output_width=0.1,output_l=150):

    # Create the first inverse taper and position it
    taper_input = top << inverse_taper(output_width=output_width, input_width=0.6, taper_length=300.0,
                                       input_straight_length=5000.0, output_straight_length=output_l)
    taper_input.dmove(taper_input_offset)  # Move taper_input to specified offset

    # Create bends and straight waveguides
    bend1 = top << custom_bend3(radius=bend_radius, angle_start=-90, angle_stop=90, width=0.6)
    straight1 = top << custom_straight1(length=10.0, width=0.6)
    straight2 = top << custom_straight4(length=10.0, width=0.6)
    bend2 = top << custom_bend1(radius=bend_radius, angle_start=0, angle_stop=-180, width=0.6)
    bend3 = top << custom_bend1(radius=bend_radius, angle_start=-90, angle_stop=0, width=0.6)
    bend4 = top << custom_bend1(radius=bend_radius, angle_start=0, angle_stop=-90, width=0.6)
    straight3 = top << custom_straight1(length=300.0, width=0.6)

    # Connect taper, bends, and straight waveguide
    bend1.connect("o1", taper_input.ports["input"])
    straight1.connect("o1", bend1.ports["o2"])
    bend2.connect("o1", straight1.ports["o2"])
    straight2.connect("o1", bend2.ports["o2"])
    bend3.connect("o1", straight2.ports["o2"])
    straight3.connect("o1", bend3.ports["o2"])
    bend4.connect("o1", straight3.ports["o2"])
    # Add a reverse inverse taper to the output of bend2
    reverse_taper = top << inverse_taper(output_width=output_width, input_width=0.6, taper_length=300.0,
                                         input_straight_length=5000.0, output_straight_length=output_l)
    reverse_taper.connect("input", bend4.ports["o2"])
def create_bend_4(top, bend_radius=30, taper_input_offset=(-500, 3000),output_width=0.1,output_l=150):

    # Create the first inverse taper and position it
    taper_input = top << inverse_taper(output_width=output_width, input_width=0.6, taper_length=300.0,
                                       input_straight_length=5000.0, output_straight_length=output_l)
    taper_input.dmove(taper_input_offset)  # Move taper_input to specified offset

    # Create bends and straight waveguides
    bend1 = top << custom_bend3(radius=bend_radius, angle_start=-90, angle_stop=90, width=0.6)
    straight1 = top << custom_straight1(length=10.0, width=0.6)
    bend2 = top << custom_bend1(radius=bend_radius, angle_start=0, angle_stop=-90, width=0.6)
    bend4 = top << custom_bend1(radius=bend_radius, angle_start=0, angle_stop=-90, width=0.6)
    straight3 = top << custom_straight1(length=300.0, width=0.6)

    # Connect taper, bends, and straight waveguide
    bend1.connect("o1", taper_input.ports["input"])
    straight1.connect("o1", bend1.ports["o2"])
    bend2.connect("o1", straight1.ports["o2"])
    straight3.connect("o1", bend2.ports["o2"])
    bend4.connect("o1", straight3.ports["o2"])
    # Add a reverse inverse taper to the output of bend2
    reverse_taper = top << inverse_taper(output_width=output_width, input_width=0.6, taper_length=300.0,
                                         input_straight_length=5060.0, output_straight_length=output_l)
    reverse_taper.connect("input", bend4.ports["o2"])
def create_bend_2(top, bend_radius=30, taper_input_offset=(-500, 3000),output_width=0.1,output_l=150):

    # Create the first inverse taper and position it
    taper_input = top << inverse_taper(output_width=output_width, input_width=0.6, taper_length=300.0,
                                       input_straight_length=5000.0, output_straight_length=output_l)
    taper_input.dmove(taper_input_offset)  # Move taper_input to specified offset

    # Create bends and straight waveguides
    bend1 = top << custom_bend3(radius=bend_radius, angle_start=-90, angle_stop=0, width=0.6)
    bend4 = top << custom_bend1(radius=bend_radius, angle_start=0, angle_stop=-90, width=0.6)
    straight3 = top << custom_straight1(length=300.0, width=0.6)

    # Connect taper, bends, and straight waveguide
    bend1.connect("o1", taper_input.ports["input"])
    straight3.connect("o1", bend1.ports["o2"])
    bend4.connect("o1", straight3.ports["o2"])
    # Add a reverse inverse taper to the output of bend2
    reverse_taper = top << inverse_taper(output_width=output_width, input_width=0.6, taper_length=300.0,
                                         input_straight_length=5000.0, output_straight_length=output_l)
    reverse_taper.connect("input", bend4.ports["o2"])

def create_straight_1(top, bend_radius=30, taper_input_offset=(-500, 3000),output_width=0.1,output_l=150):


    # Create the first inverse taper and position it
    taper_input = top << inverse_taper(output_width=output_width, input_width=0.6, taper_length=300.0,
                                       input_straight_length=5000.0, output_straight_length=output_l)
    taper_input.dmove(taper_input_offset)  # Move taper_input to specified offset

    # Create bends and straight waveguides
    bend1 = top << custom_bend3(radius=bend_radius, angle_start=-90, angle_stop=90, width=0.6)
    straight1 = top << custom_straight1(length=3000.0, width=0.6)
    straight2 = top << custom_straight4(length=3000.0, width=0.6)
    bend2 = top << custom_bend1(radius=bend_radius, angle_start=0, angle_stop=-180, width=0.6)
    bend3 = top << custom_bend1(radius=bend_radius, angle_start=-90, angle_stop=0, width=0.6)
    bend4 = top << custom_bend1(radius=bend_radius, angle_start=0, angle_stop=-90, width=0.6)
    straight3 = top << custom_straight1(length=300.0, width=0.6)

    # Connect taper, bends, and straight waveguide
    bend1.connect("o1", taper_input.ports["input"])
    straight1.connect("o1", bend1.ports["o2"])
    bend2.connect("o1", straight1.ports["o2"])
    straight2.connect("o1", bend2.ports["o2"])
    bend3.connect("o1", straight2.ports["o2"])
    straight3.connect("o1", bend3.ports["o2"])
    bend4.connect("o1", straight3.ports["o2"])
    # Add a reverse inverse taper to the output of bend2
    reverse_taper = top << inverse_taper(output_width=output_width, input_width=0.6, taper_length=300.0,
                                         input_straight_length=5000.0, output_straight_length=output_l)
    reverse_taper.connect("input", bend4.ports["o2"])


def create_straight_3(top, bend_radius=30, taper_input_offset=(-500, 3000),output_width=0.1,output_l=150):


    # Create the first inverse taper and position it
    taper_input = top << inverse_taper(output_width=output_width, input_width=0.6, taper_length=300.0,
                                       input_straight_length=5000.0, output_straight_length=output_l)
    taper_input.dmove(taper_input_offset)  # Move taper_input to specified offset

    # Create bends and straight waveguides
    bend1 = top << custom_bend3(radius=bend_radius, angle_start=-90, angle_stop=90, width=0.6)
    straight1 = top << custom_straight1(length=3000.0, width=0.6)
    straight2 = top << custom_straight4(length=6000.0, width=0.6)
    bend2 = top << custom_bend1(radius=bend_radius, angle_start=0, angle_stop=-180, width=0.6)
    bend3 = top << custom_bend1(radius=bend_radius, angle_start=-90, angle_stop=90, width=0.6)
    straight3 = top << custom_straight4(length=6000.0, width=0.6)
    straight4 = top << custom_straight4(length=3000.0, width=0.6)
    bend4 = top << custom_bend6(radius=bend_radius, angle_start=0, angle_stop=-180, width=0.6)
    bend5 = top << custom_bend1(radius=bend_radius, angle_start=-90, angle_stop=0, width=0.6)
    bend6 = top << custom_bend1(radius=bend_radius, angle_start=0, angle_stop=-90, width=0.6)
    straight5 = top << custom_straight1(length=300.0, width=0.6)

    # Connect taper, bends, and straight waveguide
    bend1.connect("o1", taper_input.ports["input"])
    straight1.connect("o1", bend1.ports["o2"])
    bend2.connect("o1", straight1.ports["o2"])
    straight2.connect("o1", bend2.ports["o2"])
    bend3.connect("o1", straight2.ports["o2"])
    straight3.connect("o1", bend3.ports["o2"])
    bend4.connect("o1", straight3.ports["o2"])
    straight4.connect("o1", bend4.ports["o2"])
    bend5.connect("o1", straight4.ports["o2"])
    straight5.connect("o1", bend5.ports["o2"])
    bend6.connect("o1", straight5.ports["o2"])
    # Add a reverse inverse taper to the output of bend2
    reverse_taper = top << inverse_taper(output_width=output_width, input_width=0.6, taper_length=300.0,
                                         input_straight_length=5000.0, output_straight_length=output_l)
    reverse_taper.connect("input", bend6.ports["o2"])

def create_straight_2(top, bend_radius=30, taper_input_offset=(-500, 3000),output_width=0.1,output_l=150):


    # Create the first inverse taper and position it
    taper_input = top << inverse_taper(output_width=output_width, input_width=0.6, taper_length=300.0,
                                       input_straight_length=5000.0, output_straight_length=output_l)
    taper_input.dmove(taper_input_offset)  # Move taper_input to specified offset

    # Create bends and straight waveguides
    bend1 = top << custom_bend3(radius=bend_radius, angle_start=-90, angle_stop=90, width=0.6)
    straight1 = top << custom_straight1(length=3000.0, width=0.6)
    straight2 = top << custom_straight4(length=6000.0, width=0.6)
    bend2 = top << custom_bend1(radius=bend_radius, angle_start=0, angle_stop=-180, width=0.6)
    bend3 = top << custom_bend1(radius=bend_radius, angle_start=-90, angle_stop=90, width=0.6)
    bend4 = top << custom_bend5(radius=bend_radius, angle_start=0, angle_stop=-90, width=0.6)
    bend5 = top << custom_bend1(radius=bend_radius, angle_start=0, angle_stop=-90, width=0.6)
    straight3 = top << custom_straight4(length=3000.0, width=0.6)
    straight4 = top << custom_straight1(length=300.0, width=0.6)

    # Connect taper, bends, and straight waveguide
    bend1.connect("o1", taper_input.ports["input"])
    straight1.connect("o1", bend1.ports["o2"])
    bend2.connect("o1", straight1.ports["o2"])
    straight2.connect("o1", bend2.ports["o2"])
    bend3.connect("o1", straight2.ports["o2"])
    straight3.connect("o1", bend3.ports["o2"])
    bend4.connect("o1", straight3.ports["o2"])
    straight4.connect("o1", bend4.ports["o2"])
    bend5.connect("o1", straight4.ports["o2"])
    # Add a reverse inverse taper to the output of bend2
    reverse_taper = top << inverse_taper(output_width=output_width, input_width=0.6, taper_length=300.0,
                                         input_straight_length=5060.0, output_straight_length=output_l)
    reverse_taper.connect("input", bend5.ports["o2"])

def mark(offsetx=0,offsety=150):
    c = gf.Component()
    straight1 = c << custom_straight1(length= 300.0,  width= 5)
    straight2 = c << custom_straight1(length=5, width=300)
    straight2.dmove((offsetx,offsety))
    straight1.dmove((offsetx, offsety-150))

    return c
if __name__ == "__main__":
    top = gf.Component()

    # Define background
    background_vertices = [
        (-7500, -6000),
        (7500, -6000),
        (7500, 6000),
        (-7500, 6000)
    ]
    top.add_polygon(background_vertices, layer=(1, 0))

    offsets = {
        1: [(-5000, 3800), (-5000, 3100)],
        2: [(-5000, 2400), (-5000, 1700)],
        3: [(-5000, 1000), (-5000, 300)],
        4: [(-5000, -400), (-5000, -1100)],
        5: [(-5000, -1800), (-5000, -2500)],
        6: [(-5000, -3200), (-5000, -3900)],
    }

    for taper_input_offset in offsets[1]:
        create_bend_2(top, taper_input_offset=taper_input_offset, output_width=0.20,output_l=150)
    for taper_input_offset in offsets[2]:
        create_bend_4(top, taper_input_offset=taper_input_offset, output_width=0.20,output_l=150)
    for taper_input_offset in offsets[3]:
        create_bend_6(top, taper_input_offset=taper_input_offset, output_width=0.20,output_l=150)
    for taper_input_offset in offsets[4]:
        create_straight_1(top, taper_input_offset=taper_input_offset, output_width=0.20,output_l=150)
    for taper_input_offset in offsets[5]:
        create_straight_2(top, taper_input_offset=taper_input_offset, output_width=0.20,output_l=150)
    for taper_input_offset in offsets[6]:
        create_straight_3(top, taper_input_offset=taper_input_offset, output_width=0.20,output_l=150)
    mark1 = top << mark(offsetx=-5400,offsety=4650)
    mark2 = top << mark(offsetx=-5400,offsety=-4300)
    mark3 = top << mark(offsetx=5800,offsety=4650)
    mark4 = top << mark(offsetx=5800,offsety=-4300)
top.write_gds("YNbend07.gds")
top.plot()
plt.show()