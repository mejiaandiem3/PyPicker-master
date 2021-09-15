def rgb_to_hex(r, g, b):
    # Conversión rapida de RGB a HEX
    # %x convierte a HEX y el 02 significa que si el valor es menor a 2 digitos se pondra un 0
    return "#%02x%02x%02x" % (r, g, b)


def rgb_to_cmyk(r, g, b):
    # Excepción en caso de RGB (0,0,0)
    if (r, g, b) == (0, 0, 0):
        return f'(0, 0, 0, 100)'
    else:
        # rgb [0,255] -> cmy [0,1]
        c = 1 - r / 255
        m = 1 - g / 255
        y = 1 - b / 255

        # Quitamos k de la escala [0, 1]
        min_cmy = min(c, m, y)
        c = (c - min_cmy) / (1 - min_cmy)
        m = (m - min_cmy) / (1 - min_cmy)
        y = (y - min_cmy) / (1 - min_cmy)
        k = min_cmy

        # Damos formato a los resultados para una mejor interpretación
        return f'({format(c * 100,".2f")}, {format(m * 100,".2f")}, {format(y * 100,".2f")}, {format(k * 100,".2f")})'


def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    v = mx*100
    return f'({format(h,".2f")}, {format(s,".2f")}, {format(v,".2f")})'


def rgb_to_hls(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    maxc = max(r, g, b)
    minc = min(r, g, b)
    # XXX Can optimize (maxc+minc) and (maxc-minc)
    l_code = (minc+maxc)/2.0
    if minc == maxc:
        return 0.0, l_code, 0.0
    if l_code <= 0.5:
        s = (maxc-minc) / (maxc+minc)
    else:
        s = (maxc-minc) / (2.0-maxc-minc)
    rc = (maxc-r) / (maxc-minc)
    gc = (maxc-g) / (maxc-minc)
    bc = (maxc-b) / (maxc-minc)
    if r == maxc:
        h = bc-gc
    elif g == maxc:
        h = 2.0+rc-bc
    else:
        h = 4.0+gc-rc
    h = (h/6.0) % 1.0
    return f'({round(360*h, 1)}, {format(s*100, "0.2f")}%, {format(l_code*100, "0.2f")}%)'
