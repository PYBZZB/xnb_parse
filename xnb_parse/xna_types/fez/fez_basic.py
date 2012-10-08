"""
FEZ basic types
"""

from xnb_parse.xna_types.xna_primitive import Enum


class FaceOrientation(Enum):
    enum_values = dict(enumerate(['Left', 'Down', 'Back', 'Right', 'Top', 'Front']))


class LevelNodeType(Enum):
    enum_values = dict(enumerate(['']))


class LevelNodeType(Enum):
    enum_values = dict(enumerate(['Node', 'Hub', 'Lesser']))


class CollisionType(Enum):
    enum_values = dict(enumerate(['AllSides', 'TopOnly', 'None', 'Immaterial', 'TopNoStraightLedge']))


class Viewpoint(Enum):
    enum_values = dict(enumerate(['None', 'Front', 'Right', 'Back', 'Left', 'Up', 'Down', 'Perspective']))


class NpcAction(Enum):
    enum_values = dict(enumerate(['None', 'Idle', 'Idle2', 'Idle3', 'Walk', 'Turn', 'Talk', 'Burrow', 'Hide', 'ComeOut',
                                  'TakeOff', 'Fly', 'Land']))


class ActorType(Enum):
    enum_values = dict(enumerate(['None', 'Ladder', 'Bouncer', 'Sign', 'GoldenCube', 'PickUp', 'Bomb', 'Destructible',
                                  'DestructiblePermanent', 'Vase', 'Door', 'Heart', 'Watcher', 'Crystal', 'BlackHole',
                                  'Vine', 'BigBomb', 'TntBlock', 'TntPickup', 'MotorBlock', 'Hurt', 'Checkpoint',
                                  'TreasureChest', 'CubeShard', 'BigHeart', 'SkeletonKey', 'ExploSwitch', 'PushSwitch',
                                  'EightBitDoor', 'PushSwitchSticky', 'PushSwitchPermanent', 'SuckBlock', 'WarpGate',
                                  'OneBitDoor', 'SpinBlock', 'PivotHandle', 'FourBitDoor', 'LightningPlatform',
                                  'LightningGhost', 'Tombstone', 'SplitUpCube', 'UnlockedDoor', 'Hole', 'Couch',
                                  'Valve', 'Rumbler', 'Waterfall', 'Trickle', 'Drips', 'Geyser', 'ConnectiveRail',
                                  'BoltHandle', 'BoltNutBottom', 'BoltNutTop', 'CodeMachine', 'NumberCube',
                                  'LetterCube', 'TriSkull', 'Tome', 'SecretCube', 'LesserGate', 'Crumbler',
                                  'LaserEmitter', 'LaserBender', 'LaserReceiver', 'RebuildingHexahedron', 'TreasureMap',
                                  'Timeswitch', 'TimeswitchMovingPart', 'Mail', 'Mailbox', 'Bookcase', 'TwoBitDoor',
                                  'SixteenBitDoor', 'ThirtyTwoBitDoor', 'SixtyFourBitDoor', 'Owl', 'Bell',
                                  'RotatingGroup', 'BigWaterfall', 'Telescope', 'SinkPickup', 'QrCode', 'FpsPost',
                                  'PieceOfHeart', 'SecretPassage', 'Piston']))


class SurfaceType(Enum):
    enum_values = dict(enumerate(['Grass', 'Metal', 'Stone', 'Wood']))


class LiquidType(Enum):
    enum_values = dict(enumerate(['None', 'Water', 'Blood', 'Lava', 'Sewer', 'Purple', 'Green']))


class PathEndBehavior(Enum):
    enum_values = dict(enumerate(['Bounce', 'Loop', 'Stop']))


class ComparisonOperator(Enum):
    enum_values = {-1: 'None', 0: 'Equal', 1: 'Greater', 2: 'GreaterEqual', 3: 'Less', 4: 'LessEqual', 5: 'NotEqual'}


class CodeInput(Enum):
    enum_values = {0: 'None', 1: 'Up', 2: 'Down', 4: 'Left', 8: 'Right', 16: 'SpinLeft', 32: 'SpinRight', 64: 'Jump'}


class VibrationMotor(Enum):
    enum_values = dict(enumerate(['None', 'LeftLow', 'RightHigh']))
