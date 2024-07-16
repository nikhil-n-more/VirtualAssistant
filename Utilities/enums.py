from enum import Enum

class AccessibilityType(Enum):
    """
    Enum class representing the accessibility types.
    
    Attributes:
        OFFICE (int): Represents the office accessibility type.
        PERSONAL (int): Represents the personal accessibility type.
        PRIVATE (int): Represents the private accessibility type.
        OTHERS (int): Represents other accessibility types.
    """
    OFFICE = 1
    PERSONAL = 2
    PRIVATE = 3
    OTHERS = 4