from enum import Enum

class NodeType(str, Enum):
    NOTE = "note"
    CONCEPT = "concept"
    PROJECT = "project"
    TASK = "task"
    DECISION = "decision"
    EPIPHANY = "epiphany"
    REFERENCE = "reference"
    FLEETING = "fleeting"

class EdgeType(str, Enum):
    REFERENCES = "references"
    DEPENDS_ON = "depends_on"
    PART_OF = "part_of"
    CONTRADICTS = "contradicts"
    DERIVED_FROM = "derived_from"
    SYNTHESIS = "synthesis"
    ASSOCIATED_WITH = "associated_with"
