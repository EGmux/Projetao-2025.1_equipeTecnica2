from _pytest import monkeypatch
import pandas as pd
# https://gist.github.com/boechat107/6f8f2511c7e8135824f0a55efff9c2d4

class MutableCounter:
    def __init__(self):
        self.n = 0

    def inc(self):
        self.n += 1

    def get(self):
        return self.n


def count_calls(monkeypatch, module, fn):
    cnt = MutableCounter()
    def mock_fn(*args, **kwargs):
        nonlocal cnt
        cnt.inc()
        return fn(*args, **kwargs)
    mock_fn.__name__ = fn.__name__
    monkeypatch.setattr(module, fn.__name__, mock_fn)
    return cnt


def total_frames(df):
    """
    count each unique frame number in the dataframe 
    """
    return df['frame_number'].nunique()


def filter_frames(df, target_frame, extras_frames):
    """
    filter the df to return rows in the range of target_frame to extra_frames, based on the filter_number label
    """
    filtered_df = df.filter(items=['frame_number'], like=target_frame)
    for frame_num in range(target_frame+extras_frames):
        to_append = df.filter(items=['frame_number'], like=frame_num)
        filtered_df.append(to_append, ignore_index=True)

    return filtered_df
