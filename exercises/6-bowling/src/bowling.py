from .RegularFrame import RegularFrame
from .SpareFrame import SpareFrame

def jeu(frames_str: str) -> int:
    frame_string_list = frames_str.split()
    frame_list: list[RegularFrame] = []
    for index, frame_repr in enumerate(frame_string_list) :
        if("/" in frame_repr):
            frame_list.append(SpareFrame(get_or_default(frame_string_list, index + 1)))
        frame_list.append(RegularFrame(frame_repr))

    total_score = 0
    for frame in frame_list:
        total_score += frame.calc()
    return total_score


def get_or_default(frame_string_list, index):
    try:
        return frame_string_list[index]
    except:
        return ""







