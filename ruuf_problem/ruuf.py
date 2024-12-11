def calculate_section_panels(total_length, section_length, panel_dimension1, panel_dimension2):
    panels = (section_length // panel_dimension1) * (total_length // panel_dimension2)

    return panels

def max_panels(panelDim : tuple, roofDim : tuple) -> int:
    x, y = roofDim
    a, b = panelDim

    max_panels = 0

    for i in range(x + 1):
        panels_first_section = calculate_section_panels(y, i, a, b)
        panels_second_section = calculate_section_panels(y, x - i, b, a)
        max_panels = max(max_panels, panels_first_section + panels_second_section)

    for j in range(y + 1):
        panels_first_section = calculate_section_panels(x, j, a, b)
        panels_second_section = calculate_section_panels(x, y - j, b, a)
        max_panels = max(max_panels, panels_first_section + panels_second_section)

    return max_panels


if __name__ == "__main__":
    print(max_panels((1,2),(2,4)))
    print(max_panels((1,2),(3,5)))
    print(max_panels((2,2),(1,10)))
