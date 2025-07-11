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
    """
    生成“同心圆弧”之间的多边形顶点，用于画弯曲波导横截面。
    参数:
        x_center, y_center:  弧心坐标
        inner_radius:        内圆半径
        outer_radius:        外圆半径
        theta_start:         开始角度(度)
        theta_stop:          结束角度(度)
        num_points:          弧上插值点数
    返回:
        vertices: [(x1,y1), (x2,y2), ...] 组成的顶点list
    """
    # 以弧度为单位生成角度序列
    theta = np.linspace(np.radians(theta_start), np.radians(theta_stop), num_points)

    # 外弧顶点
    outer_x = x_center + outer_radius * np.cos(theta)
    outer_y = y_center + outer_radius * np.sin(theta)

    # 内弧顶点（注意反转顺序，方便拼成闭合多边形）
    inner_x = x_center + inner_radius * np.cos(theta[::-1])
    inner_y = y_center + inner_radius * np.sin(theta[::-1])

    # 合并得到多边形的定点序列
    vertices = list(zip(outer_x, outer_y)) + list(zip(inner_x, inner_y))
    return vertices


##############################################################################
# 2) 通用的弯曲波导
##############################################################################
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


##############################################################################
# 3) 其它辅助组件: custom_mmi、custom_straightX
##############################################################################

@gf.cell
def custom_mmi(
    width_rect=1.87689,           # slab_W = 1.8 µm
    length_rect=2.67444,      # slab_L = 2.80511 µm
    in_taper_L=1.30647,
    space=1.03561,            # space = 1.08408 µm
    layer_main=(2, 0),
    port_width=0.6,           # waveguide_width = 0.6 µm
    cross_section="strip"
):
    c = gf.Component()

    # 下面示例使用 gf.kdb.DPolygon 手动定义多边形
    left_rect = gf.kdb.DPolygon([
        (-50,  0.3),
        (-in_taper_L, 0.3),
        (-in_taper_L,-0.3),
        (-50, -0.3)
    ])
    left_tape = gf.kdb.DPolygon([
        (-in_taper_L,  0.3),
        (   0,  width_rect / 2),
        (   0, -width_rect / 2),
        (-in_taper_L, -0.3)
    ])
    mid_rect = gf.kdb.DPolygon([
        (0,               width_rect / 2),
        (0,              -width_rect / 2),
        (length_rect,    -width_rect / 2),
        (length_rect,     width_rect / 2)
    ])
    right_tape1 = gf.kdb.DPolygon([
        (length_rect,        space/2 + 0.35),
        (length_rect,        space/2 - 0.35),
        (length_rect + 0.925, space/2 - 0.3),
        (length_rect + 0.925, space/2 + 0.3)
    ])
    right_tape2 = gf.kdb.DPolygon([
        (length_rect,        space/2 + 0.35),
        (length_rect,        space/2 - 0.35),
        (length_rect + 0.925, space/2 - 0.3),
        (length_rect + 0.925, space/2 + 0.3)
    ])
    # 把 second tape 在 y 方向下移 space
    right_tape2.move((0, -space))

    # 添加到组件
    c.add_polygon(left_rect,   layer=layer_main)
    c.add_polygon(left_tape,   layer=layer_main)
    c.add_polygon(mid_rect,    layer=layer_main)
    c.add_polygon(right_tape1, layer=layer_main)
    c.add_polygon(right_tape2, layer=layer_main)

    # 输入端口
    input_port = gf.Port(
        name="o1",
        center=(-50, 0),
        orientation=90,
        width=port_width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o1", port=input_port)

    # 上方输出端口
    output_port_top = gf.Port(
        name="o2",
        center=(length_rect + 0.925, space / 2),
        orientation=-90,
        width=port_width,
        cross_section=cross_section,
        port_type="optical"
    )
    c.add_port("o2", port=output_port_top)

    # 下方输出端口
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
##############################################################################
# 4) 搭建一个包含 MMI + bends + straights 的示例组件
##############################################################################
@gf.cell
def build_single_mmi_with_bends(straight_length=0):
    c = gf.Component()

    # 1) 放置 MMI
    mmi = c << custom_mmi()

    # 2) 为 MMI 上方输出口(o2)连接一个弯曲波导 (原 custom_bend3)
    bend_out1 = c << custom_bend(
        angle_start=-90,
        angle_stop=-45,
        width=0.6,
        orientation_in_offset=180,  # 输入端口朝向=angle_start+180
        orientation_out_offset=90   # 输出端口朝向=angle_stop
    )
    bend_out1.connect("o1", mmi.ports["o2"])

    # 3) 为 MMI 下方输出口(o3)连接一个弯曲波导 (原 custom_bend4)
    bend_out2 = c << custom_bend(
        angle_start=90,
        angle_stop=45,
        width=0.6,
        orientation_in_offset=180,
        orientation_out_offset=-90
    )
    bend_out2.connect("o1", mmi.ports["o3"])


    bend_out11 = c << custom_bend(
        angle_start=45,
        angle_stop=0,
        width=0.6,
        orientation_in_offset=45,
        orientation_out_offset=0
    )
    bend_out11.connect("o1", bend_out1.ports["o2"])

    bend_out22 = c << custom_bend(
        angle_start=45,
        angle_stop=90,
        width=0.6,
        orientation_in_offset=-90,
        orientation_out_offset=0
    )
    bend_out22.connect("o1", bend_out2.ports["o2"])

    # 6) 给组件加上总的输入端口和输出端口
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

def mzi_same(straight_length=0,offset=(-500, 3000),output_width=0.1):
    c = gf.Component()
    taper_input = top << inverse_taper(output_width=output_width, input_width=0.6, taper_length=300.0,
                                       input_straight_length=4920.0, output_straight_length=150)
    taper_input.dmove(offset)  # Move taper_input to specified offset
    bendin= c << custom_bend(
        angle_start=90,
        angle_stop=180,
        width=0.6,
        orientation_in_offset=225,
        orientation_out_offset=0
    )
    bendin.connect("o1", taper_input.ports["input"])
    straightin = c << custom_straight(length=300.0, orientation_out=180)
    straightin.connect("o1", bendin.ports["o2"])

    bendout= c << custom_bend(
        angle_start=90,
        angle_stop=0,
        width=0.6,
        orientation_in_offset=225,
        orientation_out_offset=180
    )
    bendout.connect("o1", straightin.ports["o2"])
    straightout = c << custom_straight(length=100.0, orientation_out=0)
    straightout.connect("o1", bendout.ports["o2"])
    mzi1 = c << build_single_mmi_with_bends(straight_length=0)
    mzi1.connect("input", straightout.ports["o2"])
    straight1 = c << custom_straight(length=2 * np.sqrt(2) * 30.0, orientation_in=180)
    straight1.connect("o2", mzi1.ports["output1"])

    straight2 = c << custom_straight(length=2 * np.sqrt(2) * 30.0, orientation_out=180)
    straight2.connect("o1", mzi1.ports["output2"])
    mzi2 = c << build_single_mmi_with_bends()
    mzi2.connect("output1", straight2.ports["o2"])
    taper_output = c << inverse_taper(output_width=output_width, input_width=0.6, taper_length=300.0,
                                       input_straight_length=4700.0, output_straight_length=150)
    taper_output.connect("input", mzi2.ports["input"])

    return c

def mzi_diff(straight_length=0,offset=(-500, 3000),output_width=0.1):
    c = gf.Component()
    taper_input = top << inverse_taper(output_width=output_width, input_width=0.6, taper_length=300.0,
                                       input_straight_length=4920.0, output_straight_length=150)
    taper_input.dmove(offset)  # Move taper_input to specified offset
    bendin= c << custom_bend(
        angle_start=90,
        angle_stop=180,
        width=0.6,
        orientation_in_offset=225,
        orientation_out_offset=0
    )
    bendin.connect("o1", taper_input.ports["input"])
    straightin = c << custom_straight(length=300.0, orientation_out=180)
    straightin.connect("o1", bendin.ports["o2"])

    # 生成一个示例


    bendout= c << custom_bend(
        angle_start=90,
        angle_stop=0,
        width=0.6,
        orientation_in_offset=225,
        orientation_out_offset=180
    )
    bendout.connect("o1", straightin.ports["o2"])
    straightout = c << custom_straight(length=100.0, orientation_out=0)
    straightout.connect("o1", bendout.ports["o2"])
    mzi1 = c << build_single_mmi_with_bends(straight_length=0)
    mzi1.connect("input", straightout.ports["o2"])
    bend1 = c << custom_bend(
        angle_start=90,
        angle_stop=45,
        width=0.6,
        orientation_in_offset=225,
        orientation_out_offset=0
    )
    bend1.connect("o1", mzi1.ports["output1"])
    bend2 = c << custom_bend(
        angle_start=45,
        angle_stop=135,
        width=0.6,
        orientation_in_offset=0,
        orientation_out_offset=0
    )
    bend2.connect("o1", bend1.ports["o2"])
    bend3 = c << custom_bend(
        angle_start=45,
        angle_stop=0,
        width=0.6,
        orientation_in_offset=0,
        orientation_out_offset=180
    )
    bend3.connect("o1", bend2.ports["o2"])

    straight2 = c << custom_straight(length=2 * np.sqrt(2) * 30.0, orientation_out=180)
    straight2.connect("o1", mzi1.ports["output2"])
    mzi2 = c << build_single_mmi_with_bends()
    mzi2.connect("output1", straight2.ports["o2"])
    taper_output = top << inverse_taper(output_width=output_width, input_width=0.6, taper_length=300.0,
                                       input_straight_length=4700.0, output_straight_length=150)
    taper_output.connect("input", mzi2.ports["input"])

    return c

def mark(offsetx=0,offsety=150):
    c = gf.Component()
    straight1 = c << custom_straight(length= 300.0,  width= 5)
    straight2 = c << custom_straight(length=5, width=300)
    straight2.dmove((offsetx,offsety))
    straight1.dmove((offsetx, offsety-150))

    return c

if __name__ == "__main__":
    top = gf.Component()

    mzi1 = top << mzi_same(straight_length=0, offset=(-5000, -3000), output_width=0.2)
    mzi2 = top << mzi_same(straight_length=0, offset=(-5000, -3500), output_width=0.2)
    mzi3 = top << mzi_same(straight_length=0, offset=(-5000, -4000), output_width=0.2)
    mzi4 = top << mzi_diff(straight_length=0, offset=(-5000, -4500), output_width=0.2)
    mzi5 = top << mzi_diff(straight_length=0, offset=(-5000, -5000), output_width=0.2)
    mzi6 = top << mzi_diff(straight_length=0, offset=(-5000, -5500), output_width=0.2)

    # 导出 GDS
    top.write_gds("YNmzi09.gds")

    # 画在 matplotlib 窗口
    top.plot()
    plt.show()
