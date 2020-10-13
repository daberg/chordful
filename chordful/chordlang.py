def tohtml(chordl):
    out = []

    for line in chordl.split("\n"):
        out.append("<span>")
        out.append(line)
        out.append("</span>\n")

    return "".join(out)
