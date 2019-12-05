Run tasks on external processes to overcome Python's global interpreter lock.

> Inspired by [google-research/batch-ppo](https://github.com/google-research/batch-ppo) [`ExternalProcess`](https://github.com/google-research/batch-ppo/blob/3d09705977bae4e7c3eb20339a3b384d2a5531e4/agents/tools/wrappers.py#L303)

## Installation

```sh
pip install external
```

## Usage

```py
import external

@external
class Counter():

    def __init__(self, count=0):
        self.count = count

    def increment(self):
        self.count += 1

with Counter(count=1) as c:
    assert c.count.get() == 1
    c.increment()
    assert c.count.get() == 2
    try:
        c.decrement()
    except AttributeError as e:
        print(e)  # 'Counter' object has no attribute 'decrement'
    assert c.count.get() == 2
```
