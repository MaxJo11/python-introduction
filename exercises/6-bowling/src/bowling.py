from .RegularFrame import RegularFrame

def jeu(frames_str: str) -> int:
    frame_string_list = frames_str.split()
    frame_list: list[RegularFrame] = []
    for frame_repr in frame_string_list:
        frame_list.append(RegularFrame(frame_repr))

    total_score = 0
    for frame in frame_list:
        total_score += frame.calc()
    return total_score







