...  # This actually accept any value
    def set_timing_threshold(
        self, time_ms: SupportsFloat
    ) -> None: ...  # This actually accept any value

class GroupSingle(AbstractGroup):
    sprite: Sprite
    def __init__(self, sprite: Optional[Sprite] = None) -> None: ...
    def copy(self) -> GroupSingle: ...

def spritecollide(
    sprite: Sprite,
    group: AbstractGroup,
    dokill: bool,
    collided: Optional[Callable[[Sprite, Sprite], bool]] = None,
) -> List[Sprite]: ...
def collide_rect(left: Sprite, right: Sprite) -> bool: ...

class collide_rect_ratio:
    ratio: float
    def __init__(self, ratio: float) -> None: ...
    def __call__(self, left: Sprite, right: Sprite) -> bool: ...

def collide_circle(left: Sprite, right: Sprite) -> bool: ...

class collide_circle_ratio:
    ratio: float
    def __init__(self, ratio: float) -> None: ...
    def __call__(self, left: Sprite, right: Sprite) -> bool: ...

def collide_mask(sprite1: Sprite, sprite2: Sprite) -> Tuple[int, int]: ...
def groupcollide(
    group1: AbstractGroup,
    group2: AbstractGroup,
    dokill: bool,
    dokill2: bool,
    collided: Optional[Callable[[Sprite, Sprite], bool]] = None,
) -> Dict[Sprite, Sprite]: ...
def spritecollideany(
    sprite: Sprite,
    group: AbstractGroup,
    collided: Optional[Callable[[Sprite, Sprite], bool]] = None,
) -> Sprite: ...
