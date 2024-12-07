def max_panels(panelDim : tuple, roofDim : tuple) -> int:
    panelWidth, panelHeight = panelDim
    roofWidth ,roofHeight = roofDim

    max_tiles = 0
    width = max(panelWidth,panelHeight)
    # Strategy 1: First part of the roof with a x b, second part with b x a
    for width in range(roofWidth + 1):  # Try different widths for the first section
        section_1 = (width // panelWidth) * (roofHeight // panelHeight)  # First section with a x b
        section_2 = ((roofWidth - width) // panelHeight) * (roofHeight// panelWidth)  # Second section with b x a
        max_tiles = max(max_tiles, section_1 + section_2)

    return max_tiles

def max_panels_no_iter(panelDim : tuple, roofDim : tuple) -> int:
    panelWidth, panelHeight = panelDim
    roofWidth ,roofHeight = roofDim

    width = panelWidth

    section_1 = (width // panelWidth) * (roofHeight // panelHeight)  # First section with a x b
    section_2 = ((roofWidth - width) // panelHeight) * (roofHeight// panelWidth)  # Second section with b x a

    max_tiles = section_1 + section_2

    return max_tiles

if __name__ == "__main__":
    print(max_panels_no_iter((1,2),(2,4)))
    print(max_panels_no_iter((1,2),(3,5)))
    print(max_panels_no_iter((2,2),(1,10)))
    print(max_panels_no_iter((2,2),(3,5)))
    print(max_panels_no_iter((3,1),(3,5)))



